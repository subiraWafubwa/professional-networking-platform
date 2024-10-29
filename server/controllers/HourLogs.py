from flask import Blueprint, jsonify, request
from models import JobApplication, HourLog, db
from datetime import datetime

hour_log_bp = Blueprint('append_hour_log', __name__)

@hour_log_bp.route('/append-hour-log', methods=['PATCH'])
def get_hours_log():
    try:

        hours_to_add = request.json.get('hours')
        volunteer_id = request.json.get('volunteer_id')
        job_id = request.json.get('job_id')
        
        # Validate input
        if hours_to_add is None or volunteer_id is None:
            return jsonify({"message": "Missing required fields: 'hours' and 'volunteer_id'."}), 400
        if not isinstance(hours_to_add, int) or hours_to_add <= 0:
            return jsonify({"message": "Invalid value for 'hours'. Must be a positive integer."}), 400

        job_application = JobApplication.query.filter_by(job_id=job_id, volunteer_id=volunteer_id, status='Approved').first()

        if not job_application:
            return jsonify({"message": "No approved job application found for this job and volunteer."}), 404

        job_application.hours_worked += hours_to_add

        hour_log = HourLog(
            volunteer_id=volunteer_id,
            job_applications_id=job_application.id,
            hours=hours_to_add,
            logged_at=datetime.now()
        )

        db.session.add(hour_log)
        db.session.commit()

        return jsonify({
            "message": "Hours successfully added.",
            "job_application": {
                "job_application_id": job_application.id,
                "volunteer_id": job_application.volunteer_id,
                "job_id": job_application.job_id,
                "hours_worked": job_application.hours_worked
            },
            "hour_log": {
                "hour_log_id": hour_log.id,
                "volunteer_id": hour_log.volunteer_id,
                "job_application_id": hour_log.job_applications_id,
                "hours": hour_log.hours,
                "logged_at": hour_log.logged_at
            }
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "An error occurred while updating hours.", "error": str(e)}), 500
