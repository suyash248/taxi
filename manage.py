import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from taxi import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

# COMMANDS -
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade