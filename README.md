# TAXI - Basic cab/taxi booking app

### Requirements
Python 2.7+, pip, Redis, postgreSQL

### How to run?
1. Move to ```<project-dir>```, create virual environment and then activate it as


```sh
$ cd <project-dir>
$ virtualenv .environment
$ source .environment/bin/activate
```

2. Edit configuration under ```config.py```. i.e. provide configuration/settings related to DBs(PostgreSQL, Redis) and other constants. And depending upon the environment(Development, Staging, Testing, 
Production) set environment variable as - 

```sh
$ export APP_SETTINGS=config.DevelopmentConfig # For ```Development``` mode.
```

> If you are using PyCharm then environment variables can be specified under `run configuration`.

3. Add project to ```PYTHONPATH``` as 

```sh 
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)
```

4. Under ```<project-dir>``` install requirements/dependencies as 

```sh 
$ pip install -r requirements.txt
```

5. Then run ```taxi.py``` as  

```sh
$ python taxi.py
```

6. Run postgreSQL migrations as - 
```sh
$ python manage.py db init    # Only once.
$ python manage.py db migrate # Every time, in order to generate new migration.
$ python manage.py db upgrade # Every time, when migration(s) needs to be applied.
```
> Now you can access the application by visiting ```{protocol}://{host}:{port}```. For localhost it is ```http://localhost:5000```.


### Applications & Endpoints

> There are three applications. ```Customer app```, ```Driver app``` and ```Dashboard app```

#### Customer app - 

* It can be accessed via ```{host}:{port}/customerapp```.
* Customer can make any number of requests to ride. Customer needs to enter ```customer_id``` while making the request, ```customer_id``` can be string/integer.

#### Driver app - 

* It can be accessed via ```{host}:{port}/driverapp?id=<driver_id>```. Where ```id``` is driver's id & it can be string/integer.
* Driver app contains three tabs -

> Waiting - Shows all the ```waiting``` request(s) that needs to be served. Driver can choose to serve any request from here.

> Ongoing - Shows the ```ongoing``` request(s) that are being served currently by this driver(```<driver_id>```).

> Completed - Shows the ```completed``` request(s) that are served in the past by this driver(```<driver_id>```).

#### Dashboard app - 

* It can be accessed via ```{host}:{port}/dashboard```.
* It shows all the request(s) along with their status, driver_id, customer_id, picked_up time, request_creation_time, completion_time etc.

### Assumptions - 

> There will be only 5 drivers. It can be configured under ```config.py``` as ```DRIVER_THRESHOLD```.

> All the drivers are available all the time but they can serve one request at a time.

> A customer can make any number of rides.

> A ride will automatically be completed in 5 minutes. It can be configured under ```config.py``` as ```RIDE_COMPLETION_DURATION_IN_SEC```.

### Application Overview - 

#### Overview

![alt text](https://github.com/suyash248/taxi/blob/master/static/images/architecture/ovierview.jpg "Overview")

#### Driver app

![alt text](https://github.com/suyash248/taxi/blob/master/static/images/architecture/driver.jpg "Driver app")

#### Customer app

![alt text](https://github.com/suyash248/taxi/blob/master/static/images/architecture/customer.jpg "Customer app")

#### Dashboard

![alt text](https://github.com/suyash248/taxi/blob/master/static/images/architecture/dashboard.jpg "Dashboard")


