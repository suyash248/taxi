from threading import Timer

def schedule(seconds, func, args): # args = (1, "hello")
    """
    Schedule a task which will execute `func` after `seconds` seconds from now.
    :param seconds: `func` will execute at now + `seconds`
    :param func: Function to be executed
    :param args: Tuple containing arguments to the `func`
    :return:
    """
    print "Scheduling a job, will execute {seconds} later with {args}".format(seconds=seconds, args=args)
    Timer(seconds, func, args).start()