import os
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskblog import db
from flaskblog.config import Config

app = Flask(__name__)
app.config.from_object(Config)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()