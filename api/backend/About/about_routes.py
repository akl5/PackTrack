from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

about = Blueprint('about', __name__)

@about.route('/about', methods=['GET'])
def get_about():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM About;''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found on the about page.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response