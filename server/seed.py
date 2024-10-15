#!/usr/bin/env python3

# Standard library imports
from random import randint, choices
from pathlib import Path
from datetime import datetime

# Remote library imports
from faker import Faker
import bcrypt

# Local imports
from app import app
from models import db, Volunteer, Organization, Job, JobApplication, HourLog, Certificate

def save_passwords_to_file(volunteer_data, organization_data):
    """Appends volunteer and organization username-password details to the seeded_passwords.txt file."""
    file_path = Path(__file__).parent / 'seeded_passwords.txt'

    # Clear the file if it exists
    with open(file_path, 'w') as f:
        f.write("Volunteer Passwords\n\n")
        for username, password in volunteer_data:
            f.write(f"{username}-{password}\n")

        f.write("\nOrganization Passwords\n\n")
        for username, password in organization_data:
            f.write(f"{username}-{password}\n")

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        # Clear existing data
        Volunteer.query.delete()
        Organization.query.delete()
        Job.query.delete()  # Clear existing jobs
        JobApplication.query.delete()  # Clear existing job applications
        HourLog.query.delete()  # Clear existing hour logs
        Certificate.query.delete()  # Clear existing certificates

        # Seed volunteers
        volunteers = []
        volunteer_data = []
        for _ in range(7):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            jobs_done = 0
            overall_rating = 0.0
            
            volunteer = Volunteer(
                username=username,
                email=email,
                password=hashed_password,
                jobs_done=jobs_done,
                overall_rating=overall_rating
            )
            volunteers.append(volunteer)
            volunteer_data.append((username, password))

        db.session.add_all(volunteers)
        db.session.commit()

        # Seeding organizations
        organizations = []
        organization_data = []
        for _ in range(4):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            organization_name = fake.company()
            
            organization = Organization(
                username=username,
                email=email,
                password=hashed_password,
                organization_name=organization_name,
            )
            organizations.append(organization)

            # Append the unhashed password data
            organization_data.append((username, password))

        db.session.add_all(organizations)
        db.session.commit()

        # Seed jobs
        jobs = []
        for organization in organizations:
            for _ in range(3):  # Each organization will have 3 jobs
                job = Job(
                    organization_id=organization.id,
                    title=fake.job(),
                    field_id=randint(1, 5),  # Assuming field IDs are between 1 and 5
                    description=fake.text(max_nb_chars=200),
                    location=fake.city(),
                    date=fake.date_this_year(),
                    current_volunteers=randint(0, 5),
                    max_volunteers=randint(5, 10),
                    total_hours=randint(1, 40)
                )
                jobs.append(job)

        db.session.add_all(jobs)
        db.session.commit()

        # Seed job applications
        job_applications = []
        for job in jobs:
            # Randomly select a volunteer to apply for each job
            num_applications = randint(1, 3)  # Each job can have 1 to 3 applications
            selected_volunteers = choices(volunteers, k=num_applications)
            for volunteer in selected_volunteers:
                job_application = JobApplication(
                    volunteer_id=volunteer.id,
                    job_id=job.id,
                    signed_up_at=datetime.now(),
                    isApproved=choices([True, False])[0]  # Randomly approve or not
                )
                job_applications.append(job_application)

        db.session.add_all(job_applications)
        db.session.commit()

        # Seed hour logs
        hour_logs = []
        for job_application in job_applications:
            hours_logged = randint(1, 8)  # Log between 1 to 8 hours
            hour_log = HourLog(
                volunteer_id=job_application.volunteer_id,
                job_applications_id=job_application.id,
                hours=hours_logged,
                logged_at=datetime.now()
            )
            hour_logs.append(hour_log)

        db.session.add_all(hour_logs)
        db.session.commit()

        # Seed certificates
        certificates = []
        for job_application in job_applications:
            # Randomly decide if the volunteer received a certificate
            has_received = choices([True, False], weights=[0.7, 0.3])[0]  # 70% chance of receiving a certificate
            rating = randint(1, 5) if has_received else 0  # Assign a rating only if the certificate was received
            certificate = Certificate(
                volunteer_id=job_application.volunteer_id,
                job_id=job_application.job_id,
                hasReceived=has_received,
                rating=rating
            )
            certificates.append(certificate)

        db.session.add_all(certificates)
        db.session.commit()

        # Save the unhashed passwords to the file
        save_passwords_to_file(volunteer_data, organization_data)

        print("Seed completed!")