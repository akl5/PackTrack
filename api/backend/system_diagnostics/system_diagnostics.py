from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

system_diagnostics = Blueprint('system_diagnostics', __name__)

# RETRIEVE ALL SYSTEM DIAGNOSTICS
@system_diagnostics.route('/system_diagnostics', methods=['GET'])
def get_system_diagnostics():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM system_diagnostics;''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found in system diagostics.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response