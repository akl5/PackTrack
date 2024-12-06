from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

coop_postings = Blueprint('coop_posting', __name__)

# A ROUTE TO FETCH ALL CO-OP POSTINGS. THIS IS FOR THE HOME PAGE AS WELL AS PAGE 2 CO OP LISTINGS PAGE. 
@coop_postings.route('/coop_postings', methods=['GET'])
def get_coop_postings():
    try:
        cursor = db.get_db().cursor()
        cursor.execute('''SELECT cp.coopPosting_id as coopPosting_id, 
                       c.companyName as companyName, c.industry as companyIndustry, c.companySize as companySize, c.headquarters as companyHeadquarters,
                       c.company_id as company_id,
                       cp.hiringManager_id as hiringManager_id, 
                          cp.jobTitle as jobTitle, cp.jobDescription as jobDescription, cp.location as location, cp.jobType as jobType, cp.pay as pay,
                          cp.companyBenefits as companyBenefits, DATE(cp.startDate) as startDate, DATE(cp.endDate) as endDate, cp.linkToApply as linkToApply, 
                          cp.hiringManagerEmail as hiringManagerEmail, cp.requirements as requirements, cp.preferredSkills as preferredSkills,
                          cp.createdAT as createdAT, cp.updatedAT as updatedAT
                         FROM coop_postings cp JOIN companies c ON cp.company_id = c.company_id''')
        theData = cursor.fetchall()
        
        if not theData:
            current_app.logger.warning("No data found in coop_postings.")
        else:
            current_app.logger.info(f"Fetched {len(theData)} records.")
        
        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        current_app.logger.error(f"Error executing query: {str(e)}")
        return make_response(jsonify({"error": "Internal server error"}), 500)

# A ROUTE TO FETCH SINGULAR CO OP POSTING BASED ON ITS CO OP POSTING ID. THIS IS FOR INDIVIDUAL CO-OP LISTING PAGES 
@coop_postings.route('/coop_postings/<int:coopPosting_id>', methods=['GET'])
def get_single_coop_posting(coopPosting_id):
    # Connect to the database and fetch the coop posting by its ID
    cursor = db.get_db().cursor()
    query ='''SELECT cp.coopPosting_id as coopPosting_id, 
                       c.companyName as companyName, c.industry as companyIndustry, c.companySize as companySize, c.headquarters as companyHeadquarters,
                       c.company_id as company_id,
                       cp.hiringManager_id as hiringManager_id, 
                          cp.jobTitle as jobTitle, cp.jobDescription as jobDescription, cp.location as location, cp.jobType as jobType, cp.pay as pay,
                          cp.companyBenefits as companyBenefits, DATE(cp.startDate) as startDate, DATE(cp.endDate) as endDate, cp.linkToApply as linkToApply, 
                          cp.hiringManagerEmail as hiringManagerEmail, cp.requirements as requirements, cp.preferredSkills as preferredSkills,
                          cp.createdAT as createdAT, cp.updatedAT as updatedAT
                         FROM coop_postings cp JOIN companies c ON cp.company_id = c.company_id
               WHERE cp.coopPosting_id = %s;'''
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
@coop_postings.route('/coop_postings_by_recently_updated', methods=['GET'])
def get_coop_postings_by_date():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT cp.coopPosting_id as coopPosting_id, 
                       c.companyName as companyName, c.industry as companyIndustry, c.companySize as companySize, c.headquarters as companyHeadquarters,
                       c.company_id as company_id,
                       cp.hiringManager_id as hiringManager_id, 
                          cp.jobTitle as jobTitle, cp.jobDescription as jobDescription, cp.location as location, cp.jobType as jobType, cp.pay as pay,
                          cp.companyBenefits as companyBenefits, DATE(cp.startDate) as startDate, DATE(cp.endDate) as endDate, cp.linkToApply as linkToApply, 
                          cp.hiringManagerEmail as hiringManagerEmail, cp.requirements as requirements, cp.preferredSkills as preferredSkills,
                          cp.createdAT as createdAT, cp.updatedAT as updatedAT
                         FROM coop_postings cp JOIN companies c ON cp.company_id = c.company_id
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
@coop_postings.route('/coop_postings_by_latest_review', methods=['GET'])
def get_coop_postings_by_latest_review():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT cp.coopPosting_id AS coopPosting_id, 
                             c.companyName AS companyName, 
                             cp.jobTitle AS jobTitle, 
                             cp.location AS location, 
                             cp.jobType AS jobType, 
                             cp.jobDescription AS jobDescription, 
                             cp.coopPosting_id AS coopPosting_id,
                             MAX(fp.updatedAT) AS lastUpdatedReviewDate
                      FROM coop_postings cp 
                      JOIN companies c ON cp.company_id = c.company_id 
                      JOIN feedback_posts fp 
                          ON cp.coopPosting_id = fp.coopPosting_id
                      GROUP BY cp.coopPosting_id, c.companyName, cp.jobTitle, cp.location, cp.jobType, cp.jobDescription
                      ORDER BY lastUpdatedReviewDate DESC;''')
    
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found in coop_postings.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response 

# A ROUTE TO DELETE A CERTAIN CO-OP POSTING
@coop_postings.route('/delete_coop_posting/<int:coopPosting_id>', methods=['DELETE'])
def delete_coop_posting(coopPosting_id):
    try:
        # Get database cursor
        cursor = db.get_db().cursor()
        
        # Check if the record exists
        cursor.execute('SELECT * FROM coop_postings WHERE coopPosting_id = %s;', (coopPosting_id))
        record = cursor.fetchone()
        
        if not record:
            # If no record is found, return a 404 response
            current_app.logger.warning(f"Co-op posting with ID {coopPosting_id} not found.")
            return make_response(jsonify({"error": "Co-op posting not found"}), 404)
        
        # Delete the record
        cursor.execute('DELETE FROM coop_postings WHERE coopPosting_id = %s;', (coopPosting_id))
        db.get_db().commit()
        
        # Log and respond with success
        current_app.logger.info(f"Co-op posting with ID {coopPosting_id} successfully deleted.")
        return make_response(jsonify({"message": "Co-op posting deleted successfully"}), 200)
    
    except Exception as e:
        # Log any errors
        current_app.logger.error(f"Error deleting co-op posting: {e}")
        return make_response(jsonify({"error": "Internal server error"}), 500)

# A ROUTE TO RETRIEVE BY POPULARITY
@coop_postings.route('/coop_postings_by_popularity', methods=['GET'])
def get_coop_postings_by_popularity():
    cursor = db.get_db().cursor()

    try:
        # Execute the query to get co-ops by popularity (based on the number of applications)
        cursor.execute('''
        SELECT  cp.coopPosting_id as coopPosting_id, 
                cp.hiringManager_id as hiringManager_id, 
                cp.jobTitle as jobTitle, cp.jobDescription as jobDescription, cp.location as location, cp.jobType as jobType, cp.pay as pay,
                cp.companyBenefits as companyBenefits, DATE(cp.startDate) as startDate, DATE(cp.endDate) as endDate, cp.linkToApply as linkToApply, 
                cp.hiringManagerEmail as hiringManagerEmail, cp.requirements as requirements, cp.preferredSkills as preferredSkills,
                cp.createdAT as createdAT, cp.updatedAT as updatedAT,
            COUNT(a.application_id) AS application_count
        FROM 
            coop_postings cp
        LEFT JOIN 
            applications a 
            ON cp.coopPosting_id = a.coopPosting_id
        GROUP BY 
            cp.coopPosting_id, 
            cp.jobTitle, 
            cp.jobDescription, 
            cp.location, 
            cp.jobType, 
            cp.pay, 
            cp.companyBenefits,
            cp.startDate, 
            cp.endDate, 
            cp.linkToApply,
            cp.hiringManagerEmail
        ORDER BY 
            application_count DESC;
        ''')

        theData = cursor.fetchall()
        
        if not theData:
            current_app.logger.warning("No data found in coop_postings.")
        else:
            current_app.logger.info(f"Fetched {len(theData)} records.")
        
        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        current_app.logger.error(f"Error executing query: {str(e)}")
        return make_response(jsonify({"error": "Internal server error"}), 500)

#FETCH A ROUTE BASED ON A COMPANY ID
@coop_postings.route('/coop_postings/company/<int:company_id>', methods=['GET'])
def get_company_coop_postings(company_id):
    # Connect to the database and fetch the coop posting by its ID
    cursor = db.get_db().cursor()
    query ='''SELECT cp.coopPosting_id as coopPosting_id, 
                       c.companyName as companyName, c.industry as companyIndustry, c.companySize as companySize, c.headquarters as companyHeadquarters,
                       c.company_id as company_id,
                       cp.hiringManager_id as hiringManager_id, 
                          cp.jobTitle as jobTitle, cp.jobDescription as jobDescription, cp.location as location, cp.jobType as jobType, cp.pay as pay,
                          cp.companyBenefits as companyBenefits, DATE(cp.startDate) as startDate, DATE(cp.endDate) as endDate, cp.linkToApply as linkToApply, 
                          cp.hiringManagerEmail as hiringManagerEmail, cp.requirements as requirements, cp.preferredSkills as preferredSkills,
                          cp.createdAT as createdAT, cp.updatedAT as updatedAT
                         FROM coop_postings cp JOIN companies c ON cp.company_id = c.company_id
               WHERE cp.company_id = %s;'''
    cursor.execute(query, (company_id,))
    theData = cursor.fetchall()  
    # If no data is found for the given ID, return a 404 response
    if not theData:
        current_app.logger.warning(f"No data found for company_id {company_id}.")
        return make_response(jsonify({"error": "Not found"}), 404)
    else:
        current_app.logger.info(f"Fetched record for company_id {company_id}.")
    # Return the fetched data as JSON
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#FETCH A ROUTE BASED ON A COMPANY ID, SORTED BY LATEST DATE 
@coop_postings.route('/coop_postings_by_date/company/<int:company_id>', methods=['GET'])
def get_company_coop_postings_by_date(company_id):
    # Connect to the database and fetch the coop posting by its ID
    cursor = db.get_db().cursor()
    query ='''SELECT cp.coopPosting_id as coopPosting_id, 
                       c.companyName as companyName, c.industry as companyIndustry, c.companySize as companySize, c.headquarters as companyHeadquarters,
                       c.company_id as company_id,
                       cp.hiringManager_id as hiringManager_id, 
                          cp.jobTitle as jobTitle, cp.jobDescription as jobDescription, cp.location as location, cp.jobType as jobType, cp.pay as pay,
                          cp.companyBenefits as companyBenefits, DATE(cp.startDate) as startDate, DATE(cp.endDate) as endDate, cp.linkToApply as linkToApply, 
                          cp.hiringManagerEmail as hiringManagerEmail, cp.requirements as requirements, cp.preferredSkills as preferredSkills,
                          cp.createdAT as createdAT, cp.updatedAT as updatedAT
                         FROM coop_postings cp JOIN companies c ON cp.company_id = c.company_id
               WHERE cp.company_id = %s
               ORDER BY updatedAT DESC;'''
    cursor.execute(query, (company_id,))
    theData = cursor.fetchall()  
    # If no data is found for the given ID, return a 404 response
    if not theData:
        current_app.logger.warning(f"No data found for company_id {company_id}.")
        return make_response(jsonify({"error": "Not found"}), 404)
    else:
        current_app.logger.info(f"Fetched record for company_id {company_id}.")
    # Return the fetched data as JSON
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@coop_postings.route('/update_pay', methods=['PUT'])
def update_pay():
    cursor = db.get_db().cursor()
    data = request.get_json()
    new_pay = data.get('pay')
    coop_posting_id = data.get('coop_posting_id')

    if new_pay is None:
        return jsonify({"error": "Missing required field: pay"}), 400

    cursor.execute('''
        UPDATE coop_postings
        SET pay = %s
        WHERE coopPosting_id = %s
        ''', (new_pay, coop_posting_id))  # Ensure variable names match

    if cursor.rowcount == 0:
        return jsonify({"error": f"Co-op posting with ID {coop_posting_id} not found."}), 404

    db.get_db().commit()
    return jsonify({"message": f"Pay for coopPosting_id {coop_posting_id} updated successfully."}), 200