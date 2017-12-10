from models.request import Request, ReqStatus
from datetime import datetime

def ride(customer_id):
    try:
        Request(customer_id).create()
    except Exception as e:
        print e
        res = {"status": "error", "message": "Couldn't submit request for this ride."}
        return res
    res = {
        "status": "success",
        "message": "Request for the ride has been submitted successfully."
    }
    return res

def get_requests():
    from models.request import Request
    requests = Request.all()
    return map(lambda r: r.as_dict(), requests)

def get_requests_by_status(status=ReqStatus.WAITING,driver_id=None):
    filter_criteria = {
        "req_status": status
    }
    if driver_id is not None:
        filter_criteria['driver_id'] = driver_id

    requests = Request.filter(filter_criteria)
    return map(lambda r: r.as_dict(), requests)

def serve_request(driver_id, request_id):
    from services.taxi_scheduler import schedule
    from taxi import app

    try:
        updated_args = {
            "req_status": ReqStatus.ONGOING,
            "driver_id": driver_id,
            "picked_up": datetime.utcnow()
        }
        request = Request.filter_and_update(filter_args={"id": request_id, "req_status": ReqStatus.WAITING}, updated_args=updated_args)
        if request:
            schedule(app.config['RIDE_COMPLETION_DURATION_IN_SEC'], complete_ride, (request_id,))
        else:
            res = {"status": "warning", "message": "No such request found or request may already be selected/served."}
            return res
    except Exception as e:
        print e
        res = {"status": "error", "message": "Couldn't serve request."}
        return res
    res = {
        "status": "success",
        "message": "Accepted request successfully."
    }
    return res

def complete_ride(request_id):
    print "Going to mark the ride with request id {request_id} as COMPLETED".format(request_id=request_id)
    updated_args = {
        "req_status": ReqStatus.COMPLETED,
        "completed_at": datetime.utcnow()
    }
    Request.filter_and_update(filter_args={"id": request_id}, updated_args=updated_args)

def validate_and_register_driver(driver_id):
    if is_driver_exist(driver_id):
        return True
    else:
        if not is_driver_threshold_reached():
            register_driver(driver_id)
            return True
        return False


def is_driver_threshold_reached():
    from redisutil import redis_connection
    from taxi import app
    driver_count = redis_connection.get('TAXI_DRIVER_COUNT') or 0
    return int(driver_count) >= app.config['DRIVER_THRESHOLD']

def register_driver(driver_id):
    from redisutil import redis_connection
    redis_connection.sadd('TAXI_DRIVERS', driver_id)
    redis_connection.incr('TAXI_DRIVER_COUNT')

def is_driver_exist(driver_id):
    from redisutil import redis_connection
    return redis_connection.sismember('TAXI_DRIVERS', driver_id)