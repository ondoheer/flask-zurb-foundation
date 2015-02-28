def test_can_import_package():
	import flask_zurb_foundation

def test_can_initialize_app_and_extesion():
    from flask import Flask
    from flask_zurb_foundation import Foundation

    app = Flask(__name__)
    Foundation(app)