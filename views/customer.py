import json
from flask import Blueprint, request, render_template
from services.commons import json_response

# Register routes blueprint
customer = Blueprint ('customer', __name__)

@customer.route('/customerapp')
def home():
    return render_template('customer.html')

@customer.route('/ride', methods=['POST'])
def ride():
    from services import taxi_service
    customer_id = request.form['customer_id']
    print "Customer Id", customer_id
    res = taxi_service.ride(customer_id)
    return json_response(res)
