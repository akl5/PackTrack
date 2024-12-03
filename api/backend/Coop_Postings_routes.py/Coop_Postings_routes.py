from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

coop_postings = Blueprint('coop_posting', __name__)

@coop_postings.route('/coop_postings', methods=['GET'])
def get_coop_postings():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT coopPosting_id, company_id, jobTitle, jobDescription, location, jobType, pay, 
                            companyBenefits, startDate, endDate, linkToApply, requirements, hiringManagerEmail, 
                            createdAt, updatedAt FROM coop_postings;''')
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response