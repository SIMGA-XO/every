from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__, instance_relative_config=True)


app.config.from_pyfile('config.py',silent=False)

csrf=CSRFProtect(app)
db=SQLAlchemy(app)

from projectapp import myforms
from projectapp import mymodels
from projectapp.myroutes import user