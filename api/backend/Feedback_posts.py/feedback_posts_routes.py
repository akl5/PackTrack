from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

feedback_posts = Blueprint('feedback_post', __name__)

@feedback_posts.route('/feedback_posts', methods=['GET'])
def get_feedback_posts():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT coopPosting_id, company_id, jobTitle, jobDescription, location, jobType, pay, 
                           companyBenefits, startDate, endDate, linkToApply, requirements, hiringManagerEmail, 
                           createdAt, updatedAt FROM coop_postings;''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found in feedback_posts.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response