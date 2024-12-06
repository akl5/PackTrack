from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

write_review = Blueprint('write_review', __name__)

@write_review.route('/write_review', methods=['POST'])
def get_write_review():
    # Parse JSON payload
    data = request.get_json()
    
    # Extract data from request
    coopPosting_id = data.get('coopPosting_id')
    student_Name = data.get('student_Name')
    student_id = data.get('student_id', None)  # Optional
    studentEmployee_id = data.get('studentEmployee_id')
    returnOffer = data.get('returnOffer')
    skillsLearned = data.get('skillsLearned')
    challenges = data.get('challenges')
    writtenReview = data.get('writtenReview')

    # Validate required fields
    missing_fields = []
    for field in ['coopPosting_id', 'studentEmployee_id', 'returnOffer', 'skillsLearned', 'challenges', 'writtenReview']:
        if not data.get(field):
            missing_fields.append(field)
    
    if missing_fields:
        return make_response(jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400)
    
    # Create database cursor
    cursor = db.get_db().cursor()
        
    # Execute SQL Insert query
    cursor.execute('''INSERT INTO feedback_posts 
                          (coopPosting_id, student_Name, student_id, studentEmployee_id, returnOffer, 
                           skillsLearned, challenges, writtenReview)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', 
                       (coopPosting_id, student_Name, student_id, studentEmployee_id, returnOffer, 
                        skillsLearned, challenges, writtenReview))
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("Review not complete.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response