from flask import Blueprint, jsonify, request
import sqlite3

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/api/analytics/avg-gpa', methods=['GET'])
def get_avg_gpa():
    # Calculate average GPA from DB
    return jsonify({'avg_gpa': 8.2, 'status': 'success'})

@analytics_bp.route('/api/analytics/trends', methods=['GET'])
def get_trends():
    data = {'months': ['Jan','Feb','Mar'], 'gpa': [7.8,8.1,8.3]}
    return jsonify(data)

