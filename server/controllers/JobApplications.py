from flask import Blueprint, jsonify
from models import JobApplication, Job
from sqlalchemy import and_

job_applications_bp = Blueprint('job_applications', __name__)

@job_applications_bp.route('/job-applications/rejected/<int:volunteer_id>', methods=['GET'])
def get_rejected_job_applications(volunteer_id):
    rejected_jobs = (
        JobApplication.query
        .join(Job, JobApplication.job_id == Job.id)
        .filter(and_(JobApplication.volunteer_id == volunteer_id, JobApplication.status == 'Rejected'))
        .all()
    )

    if not rejected_jobs:
        return jsonify({"message": "No rejected job applications found for this volunteer."}), 404

    rejected_jobs_data = [
        {
            "job_application_id": app.id,
            "job_id": app.job.id,
            "job_title": app.job.title,
            "job_description": app.job.description,
            "job_date": app.job.date,
            "hours_worked": app.hours_worked,
            "total_hours": app.job.total_hours,
            "status": app.status
        }
        for app in rejected_jobs
    ]

    return jsonify({
        "message": "Rejected job applications retrieved successfully.",
        "rejected_jobs": rejected_jobs_data
    }), 200

@job_applications_bp.route('/job-applications/approved/<int:volunteer_id>', methods=['GET'])
def get_approved_job_applications(volunteer_id):
    approved_jobs = (
        JobApplication.query
        .join(Job, JobApplication.job_id == Job.id)
        .filter(and_(JobApplication.volunteer_id == volunteer_id, JobApplication.status == 'Approved'))
        .all()
    )

    if not approved_jobs:
        return jsonify({"message": "No approved job applications found for this volunteer."}), 404

    approved_jobs_data = [
        {
            "job_application_id": app.id,
            "job_id": app.job.id,
            "job_title": app.job.title,
            "job_description": app.job.description,
            "job_date": app.job.date,
            "hours_worked": app.hours_worked,
            "total_hours": app.job.total_hours,
            "status": app.status
        }
        for app in approved_jobs
    ]

    return jsonify({
        "message": "Approved job applications retrieved successfully.",
        "approved_jobs": approved_jobs_data
    }), 200
