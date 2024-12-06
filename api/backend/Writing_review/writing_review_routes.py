from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

write_review = Blueprint('write_review', __name__)

@write_review.route('/write_review', methods=['POST'])
def get_write_review():
    cursor = db.get_db().cursor()
    cursor.execute('''INSERT INTO feedback_posts (coopPosting_id, student_Name, student_id, studentEmployee_id, returnOffer, 
                   skillsLearned, challenges, writtenReview)
                    VALUES (value1, value2, value3, ...);''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("Review not complete.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response