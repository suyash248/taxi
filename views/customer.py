from flask import Blueprint, render_template

# Register routes blueprint
customer = Blueprint ('customer', __name__)

@customer.route('/customerapp')
def home():
    return render_template('customer.html')