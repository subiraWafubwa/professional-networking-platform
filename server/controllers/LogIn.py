from flask import request
from flask_restful import Resource
from config import bcrypt
from models import Organization, Volunteer

class LogIn(Resource):
    def post(self):
        data = request.get_json()

        usernameororganizationnameoremail = data.get('usernameororganizationnameoremail')
        password = data.get('password')

        if not usernameororganizationnameoremail or not password:
            return {'message': 'Username, organization_name or email; and password are required.'}, 400

        volunteer = None
        organization = None

        if '@' in usernameororganizationnameoremail:
            volunteer = Volunteer.query.filter_by(email=usernameororganizationnameoremail).first()
            organization = Organization.query.filter_by(email=usernameororganizationnameoremail).first()
        else:
            volunteer = Volunteer.query.filter_by(username=usernameororganizationnameoremail).first()
            organization = Organization.query.filter_by(organization_name=usernameororganizationnameoremail).first()

        if not volunteer and not organization:
            return {'message': 'This organization or volunteer does not exist.'}, 404

        if volunteer:
            if bcrypt.check_password_hash(volunteer.password, password):
                volunteer_data = volunteer.to_dict()
                return {
                    'message': 'Login successful',
                    'type': 'Volunteer',
                    'volunteer': volunteer_data,
                }, 200
            else:
                return {'message': 'Incorrect password.'}, 401

        if organization:
            if bcrypt.check_password_hash(organization.password, password):
                organization_data = organization.to_dict()
                return {
                    'message': 'Login successful.',
                    'type': 'Organization',
                    'organization': organization_data,
                }, 200
            else:
                return {'message': 'Incorrect password.'}, 401

        return {'message': 'Invalid credentials. Please try again.'}, 401
