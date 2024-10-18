from flask import request
from flask_restful import Resource
from models import JobApplication, Job, Volunteer
from config import db
from datetime import datetime

class JobApplications(Resource):
    def get(self):
        data = JobApplication.query.all()

        return {
            "jobs_applications": [app.to_dict() for app in data]
        }, 200
    
    def post(self):
        data = request.get_json()

        volunteer_id = data.get('volunteer_id')
        job_id = data.get('job_id')

        volunteer = Volunteer.query.get(volunteer_id)
        job = Job.query.get(job_id)

        if not volunteer:
            return {"message": "Volunteer not found."}, 404

        if not job:
            return {"message": "Job not found."}, 404

        existing_data = JobApplication.query.filter_by(volunteer_id=volunteer_id, job_id=job_id).first()
        if existing_data:
            return {"message": "Volunteer has already applied for this job."}, 400

        try:
            new_application = JobApplication(
                volunteer_id=volunteer_id,
                job_id=job_id,
                signed_up_at=datetime.now(),
                status='Pending'
            )

            db.session.add(new_application)
            db.session.commit()

            return {
                "message": "Job application created successfully.",
                "data": new_application.to_dict()
            }, 201

        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while applying for the job.", "error": str(e)}, 500
        
class JobApplicationDetail(Resource):
    def get(self, id):
        data = JobApplication.query.get(id)

        if not data:
            return {"message": "Job application not found."}, 404

        return {
            "message": "Job found",
            "data": data.to_dict()
        }, 200

    def delete(self, id):
        data = JobApplication.query.get(id)

        if not data:
            return {"message": "Job application not found."}, 404

        try:
            db.session.delete(data)
            db.session.commit()

            return {
                "message": "Job application deleted successfully.",
                "data": data.to_dict()
            }, 200
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while deleting the job application.", "error": str(e)}, 500

    def patch(self, id):
        job_application = JobApplication.query.get(id)

        if not job_application:
            return {"message": "Job application not found."}, 404

        request_data = request.get_json()
        status = request_data.get('status')

        if status not in ['Approved', 'Rejected']:
            return {"message": "Status must be either 'Approved' or 'Rejected'."}, 400

        try:
            job_application.status = status
            db.session.commit()

            return {
                "message": "Job application status updated successfully.",
                "data": job_application.to_dict()
            }, 200
        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while updating the job application status.", "error": str(e)}, 500