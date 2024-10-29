# login.py
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from config import bcrypt
from models import Organization, Volunteer

class LogIn(Resource):
    def post(self):
        data = request.get_json()

        usernameororganizationnameoremail = data.get('usernameororganizationnameoremail')
        password = data.get('password')

        if not usernameororganizationnameoremail or not password:
            return {'message': 'Username, organization_name, or email; and password are required.'}, 400

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

        # Authenticate Volunteer
        if volunteer and bcrypt.check_password_hash(volunteer.password, password):
            access_token = create_access_token(identity={'type': 'Volunteer', 'id': volunteer.id})
            return {
                'message': 'Login successful.',
                'type': 'Volunteer',
                'token': access_token,
            }, 200

        # Authenticate Organization
        if organization and bcrypt.check_password_hash(organization.password, password):
            access_token = create_access_token(identity={'type': 'Organization', 'id': organization.id})
            return {
                'message': 'Login successful.',
                'type': 'Organization',
                'token': access_token,
            }, 200

        return {'message': 'Invalid credentials. Please try again.'}, 401
