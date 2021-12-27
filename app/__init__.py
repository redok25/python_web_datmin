# Import flask and template operators 
from flask import Flask, render_template

# Define the WSGI application object 
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable 
from app.modul.upload.controllers import mod_upload as upload_module
from app.modul.upload.controllers import mod_uploader as uploader_module

# Register blueprint(s)
app.register_blueprint(upload_module)
app.register_blueprint(uploader_module)