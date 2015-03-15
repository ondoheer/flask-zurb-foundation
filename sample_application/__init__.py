from flask import Flask, render_template
from flask_zurb_foundation import Foundation


def create_app():
    app = Flask(__name__)
    Foundation(app, local=False, navigation="off_canvas")

    app.config['secret'] = 'mytoughsecret'

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    create_app().run(debug=True)

