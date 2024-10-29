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
    file_path = Path(__file__).parent / 'seeded_passwords.txt'

    # Clear the file if it exists
    with open(file_path, 'w') as f:
        for username, password in volunteer_data:
            f.write(f"{username}-{password}\n")

        for organization_name, password in organization_data:
            f.write(f"{organization_name}-{password}\n")

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        # Clear existing data
        Volunteer.query.delete()
        Organization.query.delete()
        Job.query.delete()
        JobApplication.query.delete()
        HourLog.query.delete()
        Certificate.query.delete()  # Clear existing certificates

        # Seed volunteers
        volunteers = []
        volunteer_data = []
        for _ in range(7):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            volunteer = Volunteer(
                username=username,
                email=email,
                password=hashed_password,
                jobs_done=0,  # Initialize jobs_done as 0 for now
                total_ratings_given=0.0  # Placeholder for the total ratings sum
            )
            volunteers.append(volunteer)
            volunteer_data.append((username, password))

        db.session.add_all(volunteers)
        db.session.commit()

        # Seeding organizations
        organizations = []
        organization_data = []
        for _ in range(4):
            organization_name = fake.company()
            email = fake.email()
            password = fake.password()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            website_url = fake.domain_name()

            organization = Organization(
                organization_name=organization_name,
                email=email,
                password=hashed_password,
                website_url=website_url
            )
            organizations.append(organization)
            organization_data.append((organization_name, password))

        db.session.add_all(organizations)
        db.session.commit()

        # Seed jobs
        jobs = []
        for organization in organizations:
            for _ in range(3):
                job = Job(
                    organization_id=organization.id,
                    title=fake.job(),
                    description=fake.text(max_nb_chars=200),
                    location=fake.city(),
                    date=fake.date_this_year(),
                    positionFilled=False,
                    total_hours=randint(1, 40)
                )
                jobs.append(job)

        db.session.add_all(jobs)
        db.session.commit()

        # Seed job applications and certificates based on jobs done
        job_applications = []
        certificates = []

        for volunteer in volunteers:
            # Randomly assign jobs done for each volunteer
            jobs_done = randint(1, 3)  # Each volunteer can complete between 1 and 3 jobs
            volunteer.jobs_done = jobs_done  # Update the jobs_done count for the volunteer

            # Assign job applications and certificates for each job completed
            completed_jobs = choices(jobs, k=jobs_done)
            total_ratings_sum = 0

            for job in completed_jobs:
                job_application = JobApplication(
                    volunteer_id=volunteer.id,
                    job_id=job.id,
                    signed_up_at=datetime.now(),
                    status="Approved"  # Set to approved since it's completed
                )
                job_applications.append(job_application)

                # Create a certificate with a rating for each completed job
                rating = randint(1, 5)
                certificate = Certificate(
                    volunteer_id=volunteer.id,
                    job_id=job.id,
                    rating=rating
                )
                certificates.append(certificate)
                total_ratings_sum += rating

            # Update total_ratings_given as the sum of all ratings
            volunteer.total_ratings_given = total_ratings_sum

        db.session.add_all(job_applications)
        db.session.add_all(certificates)
        db.session.commit()

        # Save the unhashed passwords to the file
        save_passwords_to_file(volunteer_data, organization_data)

        print("Seed completed!")
