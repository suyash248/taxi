from threading import Timer

def schedule(seconds, func, args): # args = (1, "hello")
    print "Scheduling a job, will execute {seconds} later with {args}".format(seconds=seconds, args=args)
    Timer(seconds, func, args).start()