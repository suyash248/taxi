def ride(customer_id):
    from models.request import Request
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