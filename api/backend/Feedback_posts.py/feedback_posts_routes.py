from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

feedback_posts = Blueprint('feedback_post', __name__)

@feedback_posts.route('/feedback_posts/<int:coopPosting_id>', methods=['GET'])
def get_feedback_posts_on_coop_posting_id():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM feedback_posts
                   WHERE coopPosting_id = %s''')
    theData = cursor.fetchone()  
    
    if not theData:
        current_app.logger.warning("No data found in feedback_posts.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@feedback_posts.route('/feedback_posts', methods=['GET'])
def get_feedback_posts():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM feedback_posts;''')
    theData = cursor.fetchall()
    
    if not theData:
        current_app.logger.warning("No data found in feedback_posts.")
    else:
        current_app.logger.info(f"Fetched {len(theData)} records.")
        
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# ROUTE TO CREATE A FEEDBACK POST
@feedback_posts.route('/create_feedback_post', methods=['POST'])
def create_feedback_post():
    try:
        # Get JSON data from the request body
        data = request.json
        
        # Extract the required fields from the request
        student_id = data.get('student_id')  # Optional based on your table definition
        studentEmployee_id = data.get('studentEmployee_id')
        coopPosting_id = data.get('coopPosting_id')
        writtenReview = data.get('writtenReview')
        skillsLearned = data.get('skillsLearned')
        challenges = data.get('challenges')
        roleSuggestions = data.get('roleSuggestions')
        returnOffer = data.get('returnOffer')

        # Validate required fields
        if not all([studentEmployee_id, coopPosting_id, writtenReview, skillsLearned, challenges, roleSuggestions, returnOffer]):
            return jsonify({"error": "Missing required fields"}), 400

        # Get a database cursor
        cursor = get_db().cursor()

        # Insert the new review into the feedback_posts table
        cursor.execute('''
            INSERT INTO feedback_posts (
                student_id, 
                studentEmployee_id, 
                coopPosting_id, 
                writtenReview, 
                skillsLearned, 
                challenges, 
                roleSuggestions, 
                returnOffer
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        ''', (
            student_id, 
            studentEmployee_id, 
            coopPosting_id, 
            writtenReview, 
            skillsLearned, 
            challenges, 
            roleSuggestions, 
            returnOffer
        ))

        # Commit the transaction
        get_db().commit()

        # Log success and return a success response
        current_app.logger.info("New feedback post created successfully.")
        return jsonify({"message": "Feedback post created successfully"}), 201

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error creating feedback post: {e}")
        return jsonify({"error": "Internal server error"}), 500