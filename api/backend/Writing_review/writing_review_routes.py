from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

write_review = Blueprint('write_review', __name__)

@write_review.route('/write_review/<int:coopPosting_id>', methods=['POST'])
def post_review():
    cursor = db.get_db().cursor()
    cursor.execute('''INSERT INTO feedback_posts (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
;''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found in feedback_posts.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response