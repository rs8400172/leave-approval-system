from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection function
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',  
        password='Ravi',  
        database='leavedatabase', 
        port='3306'
    )
 
# Function to get all leave requests
@app.route('/leave_requests', methods=['GET']) 
def get_leave_requests():
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM leave_requests")
        results = cursor.fetchall()
        
        return jsonify(results)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to create a leave request
@app.route('/leave_requests', methods=['POST'])
def create_leave_request():
    data = request.get_json()
    try:
        connection = create_connection()
        cursor = connection.cursor()
        sql = """INSERT INTO leave_requests (userid, leave_type_id, start_date, end_date, status, approver_id, remark) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (
            data['userid'],
            data['leave_type_id'],
            data['start_date'],
            data['end_date'],
            'pending',
            data.get('approver_id'),
            data.get('remark')
        ))
        connection.commit()
        return jsonify({'message': 'Leave request created successfully!'}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to update a leave request
@app.route('/leave_requests/<int:requestid>', methods=['PUT'])
def update_leave_request(requestid):
    data = request.get_json()
    try:
        connection = create_connection()
        cursor = connection.cursor()
        sql = """UPDATE leave_requests SET 
                    status = %s,
                    approver_id = %s,
                    remark = %s,
                    approval_time = NOW() 
                 WHERE requestid = %s"""
        cursor.execute(sql, (
            data.get('status', 'pending'),
            data.get('approver_id'),
            data.get('remark'),
            requestid
        ))
        connection.commit()
        return jsonify({'message': 'Leave request updated successfully!'})
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to delete a leave request
@app.route('/leave_requests/<int:requestid>', methods=['DELETE'])
def delete_leave_request(requestid):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM leave_requests WHERE requestid = %s"
        cursor.execute(sql, (requestid,))
        connection.commit()
        return jsonify({'message': 'Leave request deleted successfully!'})
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)

