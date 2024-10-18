from flask import request
from flask_restful import Resource
from config import db
from models import Certificate
from datetime import datetime

class Certificates(Resource):
    def get(self):
        try:
            certificates = Certificate.query.all()

            serialized_certificates = [certificate.to_dict() for certificate in certificates]

            return {
                "message": "Certificates retrieved successfully.",
                "data": serialized_certificates
            }, 200

        except Exception as e:
            return {
                "message": "An error occurred while fetching certificates.",
                "error": str(e)
            }, 500
