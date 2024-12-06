from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

feedback_posts = Blueprint('feedback_posts', __name__)

# ROUTE TO RETRIEVE ALL THE FEEDBACK POSTS FOR A SPECIFIED CO-OP POST
@feedback_posts.route('/feedback_posts/<int:coopPosting_id>', methods=['GET'])
def get_feedback_posts_on_coop_posting_id(coopPosting_id):
    cursor = db.get_db().cursor()
    query ='''SELECT f.coopPosting_id as coopPosting_id,
                    u.firstName as firstName, u.lastName as lastName, s.graduationYear as graduationYear, 
                   f.writtenReview as writtenReview, f.skillsLearned as skillsLearned, f.challenges as challenges,
                   f.returnOffer as returnOffer,
                   f.createdAT as createdAT, f.updatedAT as updatedAT
                   FROM feedback_posts f JOIN students s ON f.student_id = s.student_id JOIN users u ON s.student_id = u.id
                   WHERE f.coopPosting_id = %s;'''
    cursor.execute(query, (coopPosting_id,))
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
        data = request.get_json()
        cursor = db.get_db().cursor()
    
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
        if not all([student_id, studentEmployee_id, coopPosting_id, writtenReview, skillsLearned, challenges, roleSuggestions, returnOffer]):
            return jsonify({"error": "Missing required fields"}), 400

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
        db.commit()

        # Log success and return a success response
        current_app.logger.info("New feedback post created successfully.")
        return jsonify({"message": "Feedback post created successfully"}), 201

    except Exception as e:
        # Log the error and return an error response
        current_app.logger.error(f"Error creating feedback post: {e}")
        return jsonify({"error": "Internal server error"}), 500
 
    
from datetime import datetime    
# UPDATE A FEEDBACK POST    
@feedback_posts.route('/update_feedback/<int:feedback_id>', methods=['PUT'])
def update_feedback(feedback_id):
    # Parse JSON payload
    data = request.get_json()

    # Get the current date and time for 'updatedAT'
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a database cursor
    cursor = db.get_db().cursor()

    # Prepare the SQL update query
    update_query = "UPDATE feedback_posts SET updatedAT = %s"
    update_params = [updated_at]

    # Check which fields are provided in the request and add them to the query
    if 'writtenReview' in data:
        update_query += ", writtenReview = %s"
        update_params.append(data['writtenReview'])
    if 'skillsLearned' in data:
        update_query += ", skillsLearned = %s"
        update_params.append(data['skillsLearned'])
    if 'challenges' in data:
        update_query += ", challenges = %s"
        update_params.append(data['challenges'])
    if 'roleSuggestions' in data:
        update_query += ", roleSuggestions = %s"
        update_params.append(data['roleSuggestions'])
    if 'returnOffer' in data:
        update_query += ", returnOffer = %s"
        update_params.append(data['returnOffer'])

    # Add the WHERE clause to update the specific feedback post
    update_query += " WHERE feedbackPost_id = %s"
    update_params.append(feedback_id)

    # Execute SQL Update query
    try:
        cursor.execute(update_query, update_params)
        db.get_db().commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            return jsonify({"error": "Feedback post not found"}), 404

        # Send success response
        return jsonify({"message": "Feedback updated successfully!"}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": f"An error occurred while updating your feedback: {str(e)}"}), 500

# A ROUTE TO DELETE A CERTAIN FEEBACK POST
@feedback_posts.route('/delete_feedback_post/<int:feedbackPost_id>', methods=['DELETE'])
def delete_feedback_posting(feedbackPost_id):
    try:
        # Get database cursor
        cursor = db.get_db().cursor()
        
        # Check if the record exists
        cursor.execute('SELECT * FROM feedback_posts WHERE feedbackPost_id = %s;', (feedbackPost_id))
        record = cursor.fetchone()
        
        if not record:
            # If no record is found, return a 404 response
            current_app.logger.warning(f"Feedback post with ID {feedbackPost_id} not found.")
            return make_response(jsonify({"error": "Feedback post not found"}), 404)
        
        # Delete the record
        cursor.execute('DELETE FROM feedback_posts WHERE feedbackPost_id = %s;', (feedbackPost_id))
        db.get_db().commit()
        
        # Log and respond with success
        current_app.logger.info(f"Feedback post with ID {feedbackPost_id} successfully deleted.")
        return make_response(jsonify({"message": "Feedback post deleted successfully"}), 200)
    
    except Exception as e:
        # Log any errors
        current_app.logger.error(f"Error deleting feedback post: {e}")
        return make_response(jsonify({"error": "Internal server error"}), 500)