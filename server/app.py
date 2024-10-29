# app.py
#!/usr/bin/env python3

from config import app, api, db
from controllers.LogIn import LogIn
from controllers.Volunteers import VolunteerDetail, Volunteers
from controllers.Organizations import Organizations, OrganizationDetail
from controllers.Jobs import jobs_bp
from controllers.JobApplications import job_applications_bp
from controllers.HourLogs import hour_log_bp
from controllers.Cerficates import certificates_bp

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

app.register_blueprint(certificates_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(job_applications_bp)
app.register_blueprint(hour_log_bp)

if __name__ == '__main__':
    app.run(port=5555, debug=True)