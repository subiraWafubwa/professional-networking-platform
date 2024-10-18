# organization_resource.py
from pathlib import Path
from flask import request
from flask_restful import Resource
from config import db, bcrypt
from models import Organization

def save_password_to_file(organization_data):
    file_path = Path(__file__).parent.parent / 'seeded_passwords.txt'

    with open(file_path, 'a') as f:
        for organization_name, password in organization_data:
            f.write(f"{organization_name}-{password}\n")

class Organizations(Resource):
    def get(self):
        data = Organization.query.all()

        return {
            "organizations": [app.to_dict() for app in data]
        }, 200
    
    def post(self):
        data = request.get_json()

        organization_name = data.get('organization_name')
        email = data.get('email')
        password = data.get('password')
        website_url = data.get('website_url')
        
        if not organization_name or not email or not password or not website_url:
            return {'message': 'Organization name, email, password, and website URL are required.'}, 400

        if Organization.query.filter_by(organization_name=organization_name).first():
            return {'message': 'Organization name already exists.'}, 400

        if Organization.query.filter_by(email=email).first():
            return {'message': 'Email already exists.'}, 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_organization = Organization(
            organization_name=organization_name,
            email=email,
            password=hashed_password,
            website_url=website_url
        )

        try:
            db.session.add(new_organization)
            db.session.commit()

            organization_data = [(organization_name, password)]
            save_password_to_file(organization_data)

            return {
                'message': 'Organization created successfully.',
                'organization': new_organization.to_dict()
            }, 201

        except Exception as e:
            db.session.rollback()
            return {'message': 'An error occurred while creating the organization.', 'error': str(e)}, 500       

class OrganizationDetail(Resource):
    def get(self, id):
        organization = Organization.query.get(id)

        if not organization:
            return {'message': 'Organization not found.'}, 404

        return {
            'message': 'Organization retrieved successfully.',
            'organization': organization.to_dict()
        }, 200

    def delete(self, id):
        organization = Organization.query.get(id)

        if not organization:
            return {'message': 'Organization not found.'}, 404

        try:
            db.session.delete(organization)
            db.session.commit()

            return {
                'message': f'Organization deleted successfully.',
                'organization': organization.to_dict()   
            }, 200
        except Exception as e:
            db.session.rollback()
            return {'message': 'An error occurred while deleting the organization.', 'error': str(e)}, 500