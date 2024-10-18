# app.py
#!/usr/bin/env python3

from config import app, api, db
from controllers.Volunteers import VolunteerDetail, Volunteers
from controllers.LogIn import LogIn
from controllers.Organizations import Organizations, OrganizationDetail
from controllers.Jobs import Jobs, JobDetail
from controllers.JobApplications import JobApplications, JobApplicationDetail
from controllers.HourLogs import HourLogs, HourLogDetail
from controllers.Cerficates import Certificates

# API endpoints
@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# Registering resources with API
api.add_resource(Volunteers, '/volunteers')
api.add_resource(VolunteerDetail, '/volunteers/<int:id>')
api.add_resource(LogIn, '/login')
api.add_resource(Organizations, '/organizations')
api.add_resource(OrganizationDetail, '/organizations/<int:id>')
api.add_resource(Jobs, '/jobs')
api.add_resource(JobDetail, '/jobs/<int:id>')
api.add_resource(JobApplications, '/job-applications')
api.add_resource(JobApplicationDetail, '/job-applications/<int:id>')
api.add_resource(HourLogs, '/hour-logs')
api.add_resource(HourLogDetail, '/hour-logs/<int:id>')
api.add_resource(Certificates, '/certificates')

if __name__ == '__main__':
    app.run(port=5555, debug=True)