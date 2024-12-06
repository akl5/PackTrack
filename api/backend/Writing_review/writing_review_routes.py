from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from datetime import datetime

write_review = Blueprint('write_review', __name__)

@write_review.route('/create_feedback_post', methods=['POST'])
def get_write_review():
    # Parse JSON payload
    data = request.get_json()

    # Extract data from the request
    student_id = data.get('student_id')
    studentEmployee_id = data.get('studentEmployee_id')
    coopPosting_id = data.get('coopPosting_id')
    created_at = datetime.now
    writtenReview = data.get('writtenReview')
    skillsLearned = data.get('skillsLearned')
    challenges = data.get('challenges')
    roleSuggestions = data.get('roleSuggestions')
    returnOffer = data.get('returnOffer')

    # Validate required fields
    missing_fields = []
    for field in ['studentEmployee_id', 'coopPosting_id', 'writtenReview', 'skillsLearned', 'challenges', 'roleSuggestions', 'returnOffer']:
        if not data.get(field):
            missing_fields.append(field)
    
    if missing_fields:
        return make_response(jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400)
    
    # Get the current date and time for 'createdAT'
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a database cursor
    cursor = db.get_db().cursor()
    
    # Execute SQL Insert query
    try:
        cursor.execute('''INSERT INTO feedback_posts 
                          (student_id, studentEmployee_id, coopPosting_id, createdAT, writtenReview, skillsLearned, challenges, roleSuggestions, returnOffer)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', 
                       (student_id, studentEmployee_id, coopPosting_id, created_at, writtenReview, skillsLearned, challenges, roleSuggestions, returnOffer))
        
        # Commit the changes
        db.get_db().commit()
        
        # Send success response
        return make_response(jsonify({"message": "Review submitted successfully!"}), 201)
    
    except Exception as e:
        current_app.logger.error(f"Error inserting data into database: {e}")
        return make_response(jsonify({"error": "An error occurred while submitting your review."}), 500)