from flask import request
from flask_restful import Resource
from config import db
from models import HourLog, Volunteer, JobApplication
from datetime import datetime

class HourLogs(Resource):
    def get(self):
        try:
            hour_logs = HourLog.query.all()
            if not hour_logs:
                return {"message": "No hour logs found."}, 404

            return {
                "message": "Hour logs retrieved successfully.",
                "hour_logs": [log.to_dict() for log in hour_logs]
            }, 200

        except Exception as e:
            return {"message": "An error occurred while retrieving hour logs.", "error": str(e)}, 500
        
    def post(self):
        data = request.get_json()

        volunteer_id = data.get('volunteer_id')
        job_application_id = data.get('job_application_id')
        hours = data.get('hours')

        volunteer = Volunteer.query.get(volunteer_id)
        job_application = JobApplication.query.get(job_application_id)

        if not volunteer:
            return {"message": "Volunteer not found."}, 404

        if not job_application:
            return {"message": "Job application not found."}, 404

        if not hours or hours <= 0:
            return {"message": "Please provide valid hours worked."}, 400

        try:
            new_hour_log = HourLog(
                volunteer_id=volunteer_id,
                job_applications_id=job_application_id,
                hours=hours,
                logged_at=datetime.now()
            )

            db.session.add(new_hour_log)
            db.session.commit()

            total_hours_worked = db.session.query(db.func.sum(HourLog.hours)).filter_by(job_applications_id=job_application_id).scalar()

            job_application.hours_worked = total_hours_worked or 0

            db.session.commit()

            return {
                "message": "Hour log created and hours worked updated successfully.",
                "hour_log": new_hour_log.to_dict(),
                "updated_hours_worked": job_application.hours_worked
            }, 201

        except Exception as e:
            db.session.rollback()
            return {"message": "An error occurred while creating the hour log.", "error": str(e)}, 500
        
class HourLogDetail(Resource):
    def get(self, id):
        hour_log = HourLog.query.get(id)

        if not hour_log:
            return {"message": "Hour log not found."}, 404

        return {
            "message": "Hour log retrieved successfully.",
            "hour_log": hour_log.to_dict()
        }, 200