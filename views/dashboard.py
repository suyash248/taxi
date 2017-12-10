from flask import Blueprint, render_template

# Register routes blueprint
dashboard = Blueprint ('dashboard', __name__)

@dashboard.route('/dashboard')
def home():
    return render_template('dashboard.html')