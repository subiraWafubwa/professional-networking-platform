from flask import Blueprint, jsonify
from models import Certificate, Job, Organization
from config import db

certificates_bp = Blueprint('certificates', __name__)

@certificates_bp.route('/certificates/<int:volunteer_id>', methods=['GET'])
def get_certificates(volunteer_id):
    certificates = (
        db.session.query(
            Certificate.id,
            Certificate.volunteer_id,
            Certificate.job_id,
            Certificate.rating,
            Job.title.label("job_title"),
            Job.description.label("job_description"),
            Organization.organization_name.label("organization_name")
        )
        .join(Job, Certificate.job_id == Job.id)
        .join(Organization, Job.organization_id == Organization.id)
        .filter(Certificate.volunteer_id == volunteer_id)
        .all()
    )

    if not certificates:
        return jsonify({"message": "No certificates found for this volunteer."}), 404

    certificate_data = [
        {
            "id": certificate.id,
            "volunteer_id": certificate.volunteer_id,
            "job_id": certificate.job_id,
            "rating": certificate.rating,
            "job_title": certificate.job_title,
            "job_description": certificate.job_description,
            "organization_name": certificate.organization_name,
        }
        for certificate in certificates
    ]

    return jsonify({
        "message": "Certificates retrieved successfully.",
        "certificates": certificate_data
    }), 200
