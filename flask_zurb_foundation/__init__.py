# -*- coding: utf-8 -*-
"""
    flaskext.zurb_foundation
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Adds Foundation framework functionalities to flask

    :copyright: (c) 2015 by ondoheer.
    :license: BSD, see LICENSE for more details.
"""

from flask import Blueprint

class Foundation(object):
    """
    :param: app: Flask aplication
    :param: local: Bolean Value, if True it will serve local files for Foundation, else CDN  ones.
    """
    
    def __init__(self, app=None, local=True, navigation="off_canvas",  **kwargs):
        self.local = local
        self.navigation = navigation
        self._dir = kwargs.get("_dir", "ltr")
        self.lang = kwargs.get("lang", "en")
        
        if self.navigation is "off_canvas":
            self.tab_bar = kwargs.get("tab_bar", False)
            self.menu_toggle = kwargs.get("menu_toggle", True)

        elif self.navigation is "top_bar":
            pass
        elif self.navigation is "icon_bar":
            pass
        elif self.navigation is "side_nav":
            pass

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
        app.jinja_env.globals['navigation'] = self.navigation
        app.jinja_env.globals['_dir'] = self._dir
        app.jinja_env.globals['lang'] = self.lang


        

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        
