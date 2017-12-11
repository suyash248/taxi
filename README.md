# taxi - Basic cab/taxi booking app

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
export APP_SETTINGS=config.DevelopmentConfig # For ```Development``` mode.
```

#### PostgreSQL configuration - 
Database - taxi

3. Add project to ```PYTHONPATH``` as 

```sh 
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)
```

3. Under ```<project-dir>``` install requirements/dependencies as 

```sh 
$ pip install -r requirements.txt
```

4. Then run ```app.py``` as  

```sh
$ python app.py
```

5. Run postgreSQL migrations as - 
```sh
$ python manage.py db init    # Only once.
$ python manage.py db migrate # Every time, in order to generate new migration.
$ python manage.py db upgrade # Every time, when migration(s) needs to be applied.
```
> Now you can access the application by visiting ```{protocol}://{host}:{port}```. For localhost it is ```http://localhost:5000```.


### Applications & Endpoints

- There are three applications. ```Customer app```, ```Driver app``` and ```Dashboard app```

> Assumption: Assuming that metar endpoint will return reponse in foillowing format - 
1. There will be only 5 drivers. It can be configured under ```config.py``` as ```DRIVER_THRESHOLD```.
2. All the drivers are available all the time but they can serve one request at a time.
3. A customer can make any number of rides.
4. A ride will automatically be completed in 5 minutes. It can be configured under ```config.py``` as ```RIDE_COMPLETION_DURATION_IN_SEC```.
