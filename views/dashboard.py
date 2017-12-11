from flask import Blueprint, render_template
# Register routes blueprint
dashboard = Blueprint ('dashboard', __name__)

@dashboard.route('/dashboard')
def home():
    """
    Homepage for the dashboard app.
    :return:
    """
    from services import taxi_service
    requests = taxi_service.get_requests()
    return render_template('dashboard.html', data=requests)