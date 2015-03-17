from flask import Flask, render_template
from flask_zurb_foundation import Foundation


def create_app():
    app = Flask(__name__)
    # foundation = Foundation(app, local=False)
    Foundation(app).iconBarMenu(5, "large-vertical")
    # Foundation(app)
    # Foundation(app).offCanvasMenu(menu=(True,True))
    app.config['secret'] = 'mytoughsecret'
    app.config["FOUNDATION_CDN"]
    app.config["FOUNDATION_TEXT_DIRECTION"] = "rtl"

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/test')
    def test():
    	return render_template("test.html")

    return app


if __name__ == '__main__':
    create_app().run(debug=True)

