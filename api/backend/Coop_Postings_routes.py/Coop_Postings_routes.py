from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

coop_postings = Blueprint('coop_posting', __name__)

@coop_postings.route('/coop_postings', methods=['GET'])
def get_customers():

    cursor = db.get_db().cursor()
    cursor.execute('''SELECT id, company, last_name,
                    first_name, job_title, business_phone FROM customers
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response