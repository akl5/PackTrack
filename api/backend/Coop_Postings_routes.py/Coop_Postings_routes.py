from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

coop_postings = Blueprint('coop_posting', __name__)

@coop_postings.route('/Coop_Listings', methods=['GET'])
def get_all_coop_postings():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT coopPosting_id, company_id, jobTitle, jobDescription, location, jobType, pay, 
                            companyBenefits, startDate, endDate, linkToApply, requirements, hiringManagerEmail, 
                            createdAt, updatedAt FROM coop_postings;''')
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@coop_postings.route('/coop_postings/<int:coopPosting_id>', methods=['GET'])
def get_single_coop_posting(coopPosting_id):
    # Connect to the database and fetch the coop posting by its ID
    cursor = db.get_db().cursor()
    query = '''SELECT coopPosting_id, company_id, hiringManager_id, jobTitle, jobDescription, location, jobType, pay,
                      companyBenefits, startDate, endDate, linkToApply, hiringManagerEmail, requirements, preferredSkills,
                      createdAT, updatedAT
               FROM coop_postings 
               WHERE coopPosting_id = %s;'''
    cursor.execute(query, (coopPosting_id,))
    theData = cursor.fetchone()  # Fetch a single record

    # If no data is found for the given ID, return a 404 response
    if not theData:
        current_app.logger.warning(f"No data found for coopPosting_id {coopPosting_id}.")
        return make_response(jsonify({"error": "Not found"}), 404)
    else:
        current_app.logger.info(f"Fetched record for coopPosting_id {coopPosting_id}.")

    # Return the fetched data as JSON
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response