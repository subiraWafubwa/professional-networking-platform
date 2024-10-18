from pathlib import Path
from flask import request
from flask_restful import Resource
from config import db
from models import Job, Organization
from datetime import datetime

class Jobs(Resource):
    def get(self):
        data = Job.query.all()

        return {
            "jobs": [app.to_dict() for app in data]
        }, 200
    
    def post(self):
        data = request.get_json()

        organization_id = data.get('organization_id')
        title = data.get('title')
        description = data.get('description', "")
        location = data.get('location', "")
        total_hours = data.get('total_hours', 0)

        # Check if the organization exists
        organization = Organization.query.get(organization_id)
        if not organization:
            return {"message": "Organization not found."}, 404

        existing_job = Job.query.filter_by(organization_id=organization_id, title=title).first()
        if existing_job:
            return {"message": "This job already exists."}, 400

        try:
            new_job = Job(
                organization_id=organization_id,
                title=title,
                description=description,
                location=location,
                date=datetime.today().date(),
                total_hours=total_hours,
            )

            db.session.add(new_job)
            db.session.commit()

            return {
                "message": "Job added successfully",
                "job": new_job.to_dict()
            }, 201

        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while adding the job.", "error": str(e)}, 500
        
class JobDetail(Resource):
    def delete(self, id):
        job = Job.query.get(id)

        if not job:
            return {"message": "Job not found."}, 404

        try:
            db.session.delete(job)
            db.session.commit()
            return {
                "message": "Job deleted successfully.",
                "job_deleted": job.to_dict()                
            }, 200

        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while deleting the job.", "error": str(e)}, 500

    def patch(self, id):
        job = Job.query.get(id)

        if not job:
            return {"message": "Job not found."}, 404

        try:
            job.positionFilled = True
            db.session.commit()
            return {"message": "Job updated successfully.", "job": job.to_dict()}, 200

        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the job.", "error": str(e)}, 500