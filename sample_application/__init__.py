from flask import Flask, render_template
from flask_zurb_foundation import Foundation


def create_app():
    app = Flask(__name__)
    
    Foundation(app)
    
    app.config['secret'] = 'mytoughsecret'
    app.config["FOUNDATION_CDN"]

    #app.config["FOUNDATION_TEXT_DIRECTION"] = "rtl"


    @app.route('/')
    def index():
        return render_template('index.html')    

    return app


if __name__ == '__main__':
    create_app().run(debug=True)

