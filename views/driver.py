from flask import Blueprint, render_template

# Register routes blueprint
driver = Blueprint ('driver', __name__)

@driver.route('/driverapp')
def home():
    return render_template('driver.html')