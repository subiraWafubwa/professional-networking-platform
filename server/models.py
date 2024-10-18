# models.py
from sqlalchemy_serializer import SerializerMixin
from config import db
from datetime import datetime

class Volunteer(db.Model, SerializerMixin):
    __tablename__ = 'volunteers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    jobs_done = db.Column(db.Integer, nullable=False)
    overall_rating = db.Column(db.Float, nullable=False)

    # Serialization rules
    serialize_only = ('id', 'username', 'email', 'password', 
                      'created_at', 'jobs_done', 'overall_rating',)

    # Relationships
    certificates = db.relationship('Certificate', back_populates='volunteer', cascade='all, delete-orphan')
    job_applications = db.relationship('JobApplication', back_populates='volunteer', cascade='all, delete-orphan')
    hour_logs = db.relationship('HourLog', back_populates='volunteer', cascade='all, delete-orphan')

class Organization(db.Model, SerializerMixin):
    __tablename__ = 'organizations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    organization_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    website_url = db.Column(db.String, nullable=False)

    # Serialization rules
    serialize_only = ('id', 'organization_name', 'email', 
                      'password', 'website_url',)

    # Relationships
    jobs = db.relationship('Job', back_populates='organization', cascade='all, delete-orphan')

class Job(db.Model, SerializerMixin):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organizations.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String)
    date = db.Column(db.Date)
    positionFilled = db.Column(db.Boolean, default=False)
    total_hours = db.Column(db.Integer)

    # Serialization rules
    serialize_only = ('id', 'organization_id', 'title', 
                      'description', 'location', 'date', 
                      'positionFilled', 'total_hours',)

    # Relationships
    organization = db.relationship('Organization', back_populates='jobs')
    job_applications = db.relationship('JobApplication', back_populates='job', cascade='all, delete-orphan')
    certificates = db.relationship('Certificate', back_populates='job', cascade='all, delete-orphan')


class JobApplication(db.Model, SerializerMixin):
    __tablename__ = 'job_applications'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id', ondelete='CASCADE'), nullable=False)
    signed_up_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    hours_worked = db.Column(db.Integer, default=0)
    status = db.Column(db.Text, nullable=False)

    # Serialization rules
    serialize_only = ('id', 'volunteer_id', 'job_id', 'signed_up_at', 'hours_worked', 'status',)

    # Relationships
    job = db.relationship('Job', back_populates='job_applications')
    volunteer = db.relationship('Volunteer', back_populates='job_applications')
    hour_logs = db.relationship('HourLog', back_populates='job_application', cascade='all, delete-orphan')
    
class HourLog(db.Model, SerializerMixin):
    __tablename__ = 'hourlogs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'), nullable=False)
    job_applications_id = db.Column(db.Integer, db.ForeignKey('job_applications.id', ondelete='CASCADE'), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    logged_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    serialize_only = ('id', 'volunteer_id', 'job_applications_id', 'hours', 'logged_at')

    # Relationships
    job_application = db.relationship('JobApplication', back_populates='hour_logs')
    volunteer = db.relationship('Volunteer', back_populates='hour_logs')

class Certificate(db.Model, SerializerMixin):
    __tablename__ = 'certificates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    rating = db.Column(db.Integer, default=0)

    serialize_only = ('id', 'volunteer_id', 'job_id', 'rating',)

    # Relationships
    volunteer = db.relationship('Volunteer', back_populates='certificates')
    job = db.relationship('Job', back_populates='certificates')