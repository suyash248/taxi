from flask import Blueprint, render_template
from services import taxi_service
# Register routes blueprint
dashboard = Blueprint ('dashboard', __name__)

@dashboard.route('/dashboard')
def home():
    requests = taxi_service.get_requests()
    return render_template('dashboard.html', data=requests)