from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

coop_postings = Blueprint('coop_posting', __name__)

# A ROUTE TO FETCH ALL CO-OP POSTINGS. THIS IS FOR THE 2_COOP_LISTINGS.PY PAGE
@coop_postings.route('/coop_postings', methods=['GET'])
def get_coop_postings():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT coopPosting_id, company_id, jobTitle, jobDescription, location, jobType, pay, 
                           companyBenefits, startDate, endDate, linkToApply, requirements, hiringManagerEmail, 
                           createdAT, updatedAT 
                      FROM coop_postings;''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found in coop_postings.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# A ROUTE TO FETCH SINGULAR CO OP POSTING BASED ON ITS CO OP POSTING ID. THIS IS FOR INDIVIDUAL CO-OP LISTING PAGES 
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

# A ROUTE TO FETCH ALL CO-OP POSTINGS BY MOST RECENTLY UPDATED. THIS IS FOR THE 9_Listings_By_Date.py PAGE
@coop_postings.route('/coop_postings', methods=['GET'])
def get_coop_postings_by_date():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT coopPosting_id, company_id, jobTitle, jobDescription, location, jobType, pay, 
                           companyBenefits, startDate, endDate, linkToApply, requirements, hiringManagerEmail, 
                           createdAT, updatedAT 
                      FROM coop_postings 
                      ORDER BY updatedAT;''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found in coop_postings.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# A ROUTE TO FETCH ALL CO-OP POSTINGS BY WHICH RECEIVED THE LATEST REVIEW. THIS IS FOR THE 4_Coops_By_Latest.Reviews.py PAGE
@coop_postings.route('/coop_postings', methods=['GET'])
def get_coop_postings_by_latest_review():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT coopPosting_id, company_id, jobTitle, jobDescription, location, jobType, pay, 
                           companyBenefits, startDate, endDate, linkToApply, requirements, hiringManagerEmail, 
                           createdAT, updatedAT 
                      FROM coop_postings cp 
                      JOIN feedback_posts fp 
                           ON cp.coopPosting_id = fp.coopPosting.id ORDER BY fp.updatedAT;''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found in coop_postings.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response    