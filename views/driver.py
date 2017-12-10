from flask import Blueprint, render_template, request

# Register routes blueprint
driver = Blueprint ('driver', __name__)

@driver.route('/driverapp')
def home():
    driver_id = request.args.get('id')
    if driver_id is None:
        return "Unknown driver"
    return render_template('driver.html')