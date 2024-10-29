from flask import Blueprint, jsonify, request
from models import Job, JobApplication, Organization
from datetime import datetime
from sqlalchemy import and_
from config import db

jobs_bp = Blueprint('jobs', __name__)

def check_pending_status(volunteer_id, job_id):
    pending_application = (
        db.session.query(JobApplication)
        .filter(
            JobApplication.volunteer_id == volunteer_id,
            JobApplication.job_id == job_id,
            JobApplication.status == "Pending"
        )
        .first()
    )
    return pending_application is not None

@jobs_bp.route('/jobs/<int:volunteer_id>', methods=['GET'])
def get_jobs_by_volunteer(volunteer_id):
    excluded_job_ids = (
        db.session.query(JobApplication.job_id)
        .filter(
            JobApplication.volunteer_id == volunteer_id,
            JobApplication.status.in_(["Approved", "Rejected"])
        )
    ).subquery()

    jobs = (
        db.session.query(
            Job.id,
            Job.title,
            Job.description,
            Job.location,
            Job.date,
            Job.positionFilled,
            Job.total_hours,
            Organization.organization_name.label("organization_name")
        )
        .join(Organization, Job.organization_id == Organization.id)
        .outerjoin(JobApplication, and_(JobApplication.job_id == Job.id, JobApplication.volunteer_id == volunteer_id))
        .filter(Job.id.notin_(excluded_job_ids))
        .all()
    )

    if not jobs:
        return jsonify({"message": "No available jobs for this volunteer."}), 404

    job_data = [
        {
            "id": job.id,
            "title": job.title,
            "description": job.description,
            "location": job.location,
            "date": job.date.isoformat() if job.date else None,
            "positionFilled": job.positionFilled,
            "total_hours": job.total_hours,
            "organization_name": job.organization_name,
            "isPending": check_pending_status(volunteer_id, job.id)
        }
        for job in jobs
    ]

    return jsonify({
        "message": "Jobs retrieved successfully.",
        "jobs": job_data
    }), 200

@jobs_bp.route('/apply-for-job', methods=['POST'])
def apply_for_job():
    try:
        volunteer_id = request.json.get('volunteer_id')
        job_id = request.json.get('job_id')

        if volunteer_id is None or job_id is None:
            return jsonify({"message": "Missing required fields: 'volunteer_id' and 'job_id'."}), 400

        job = Job.query.get(job_id)
        if not job:
            return jsonify({"message": "Job not found."}), 404

        if check_pending_status(volunteer_id, job_id):
            return jsonify({
                "message": "You have already applied for this job.",
                "isPending": True
            }), 200

        new_application = JobApplication(
            volunteer_id=volunteer_id,
            job_id=job_id,
            signed_up_at=datetime.now(),
            hours_worked=0,
            status='Pending'
        )

        db.session.add(new_application)
        db.session.commit()
        
        return jsonify({
            "message": "Application submitted successfully.",
            "job_application": {
                "id": new_application.id,
                "volunteer_id": new_application.volunteer_id,
                "job_id": new_application.job_id,
                "status": new_application.status,
                "signed_up_at": new_application.signed_up_at,
                "isPending": True
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "An error occurred while submitting the application.", "error": str(e)}), 500
