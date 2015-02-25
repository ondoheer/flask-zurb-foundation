from flask import Flask, render_template
from foundation import Foundation
from flask_appconfig import AppConfig



def create_app(configfile=None):
	app = Flask(__name__)
	AppConfig(app, configfile)
	Foundation(app)

	app.config['SECRET_KEY'] = 'bdsakjerrr'

	@app.route('/')
	def index():
		return render_template('index.html')

	return app



if __name__ == '__main__':
	create_app().run(debug=True)