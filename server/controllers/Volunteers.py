# volunteers_resource.py
from pathlib import Path
from flask import request
from flask_restful import Resource
from config import db, bcrypt
from models import Volunteer

def save_password_to_file(volunteer_data):
    file_path = Path(__file__).parent.parent / 'seeded_passwords.txt'

    with open(file_path, 'a') as f:
        for username, password in volunteer_data:
            f.write(f"{username}-{password}\n")

class Volunteers(Resource):
    def get(self):
        data = Volunteer.query.all()

        return {
            "volunteers": [app.to_dict() for app in data]
        }, 200
    
    def post(self):
        data = request.get_json()

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return {'message': 'Username, email and password are required.'}, 400

        if Volunteer.query.filter_by(username=username).first():
            return {'message': 'Username already exists.'}, 400

        if Volunteer.query.filter_by(email=email).first():
            return {'message': 'Email already exists.'}, 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_volunteer = Volunteer(
            username=username,
            email=email,
            password=hashed_password,
            jobs_done=0,
            overall_rating=0.0
        )

        try:
            db.session.add(new_volunteer)
            db.session.commit()

            volunteer_data = [(username, password)]
            save_password_to_file(volunteer_data)

            volunteer_data = new_volunteer.to_dict()

            return {
                'message': 'Volunteer created successfully.',
                'volunteer': volunteer_data
            }, 201

        except Exception as e:
            db.session.rollback()
            return {'message': 'An error occurred while creating the volunteer.', 'error': str(e)}, 500
        
class VolunteerDetail(Resource):
    def get(self, id):
        volunteer = Volunteer.query.get(id)

        if not volunteer:
            return {'message': 'Volunteer not found.'}, 404

        return {
            'message': 'Volunteer retrieved successfully.',
            'volunteer': volunteer.to_dict()
        }, 200
        

    def delete(self, id):
        volunteer = Volunteer.query.get(id)

        if not volunteer:
            return {'message': 'Volunteer not found.'}, 404

        try:
            db.session.delete(volunteer)
            db.session.commit()

            return {
                'message': f'Volunteer deleted successfully.',
                'volunteer': volunteer.to_dict()   
            }, 200
        except Exception as e:
            db.session.rollback()
            return {'message': 'An error occurred while deleting the volunteer.', 'error': str(e)}, 500