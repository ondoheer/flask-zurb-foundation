# -*- coding: utf-8 -*-
"""
    flaskext.zurb_foundation
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Description of the module goes here...

    :copyright: (c) 2015 by ondoheer.
    :license: BSD, see LICENSE for more details.
"""

from flask import Blueprint

class Foundation(object):
    """
    :param: app: Flask aplication
    :param: local: Bolean Value, if True it will serve local files for Foundation, else CDN  ones.
    """
    
    def __init__(self, app=None, local=True):
        self.local = local

        if app:
            self.init_app(app)
        


    def init_app(self, app):
        blueprint = Blueprint(
            'foundation',
            __name__,
            static_folder='static',
            template_folder='templates',
            static_url_path=app.static_url_path + '/foundation',
        )

        app.register_blueprint(blueprint)

        app.jinja_env.globals['local'] = self.local
        

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        
