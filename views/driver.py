from flask import Blueprint, render_template, request
from services.commons import json_response
# Register routes blueprint
driver = Blueprint ('driver', __name__)

@driver.route('/driverapp')
def home():
    """
    Starting point/homepage for the driver app.
    :return:
    """
    from services import taxi_service
    from models.request import ReqStatus
    req_status = request.args.get('req_status', ReqStatus.WAITING)
    driver_id = request.args.get('id')
    xhr = request.args.get('xhr', False)

    if driver_id is None:
        return "Unknown driver"
    from models.request import ReqStatus
    requests = []
    if taxi_service.validate_and_register_driver(driver_id):
        if req_status == ReqStatus.WAITING.name:
            requests = taxi_service.get_requests_by_status(req_status)
        else:
            requests = taxi_service.get_requests_by_status(req_status, driver_id)

        template = 'driver/driver.html'
        if xhr:
            template = 'driver/{req_status}.html'.format(req_status=req_status.lower())
        return render_template(template, data=requests)
    else:
        return "Driver(s) limit exceeded!"

@driver.route('/driver/serve/<driver_id>/<request_id>')
def serve(driver_id, request_id):
    """
    Endpoint responsible for serving/selecting a request which is in waiting state.
    :param driver_id:
    :param request_id:
    :return:
    """
    from services import taxi_service
    if taxi_service.validate_and_register_driver(driver_id):
        from services import taxi_service
        res = taxi_service.serve_request(driver_id, request_id)
        return json_response(res)
    else:
        return json_response({"status": "error", "message": "Driver(s) limit exceeded."})
