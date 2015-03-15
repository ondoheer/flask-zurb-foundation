# -*- coding: utf-8 -*-
"""
    flaskext.zurb_foundation
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Adds Foundation framework functionalities to flask

    :copyright: (c) 2015 by ondoheer.
    :license: BSD, see LICENSE for more details.
"""


__version__ = '0.1.6'
__version_info__ = __version__.split('.')
__author__ = 'Pedro Baumann'
__license__ = 'Apache'
__copyright__ = '(c) 2015 - Pedro Baumann.'

from flask import Blueprint


class Foundation(object):

    """
    :param: app: Flask aplication
    :param: local: Bolean Value, if True it will serve local files for Foundation, else CDN  ones.
    """

    def __init__(self,
                 app=None,
                 local=True,
                 **kwargs
                 ):
        self.local = local
        self._dir = kwargs.get("_dir", "ltr")
        self.lang = kwargs.get("lang", "en")

        if app:
            self.init_app(app)

    def offCanvasMenu(self, tab_bar=False, menu_toggle=True, menu=(True, False)):
        """
        Includes the markup and jinja blocks for Foundation off-canvas menu.
        param: tab_bar: makes the basic template use a Foundation Tab_bar and it's 
                        predefined blocks
        param: menu_toggle: makes the basic template use a menu toggle functionality
                            and it's predefined blocks.
        """
        self.off_canvas = True
        self.off_canvas_left, self.off_canvas_right = menu
        self.off_canvas_tab_bar = tab_bar
        self.off_canvas_menu_toggle = menu_toggle

        self.app.jinja_env.globals['off_canvas'] = self.off_canvas
        self.app.jinja_env.globals['off_canvas_left'] = self.off_canvas_left
        self.app.jinja_env.globals['off_canvas_right'] = self.off_canvas_right
        self.app.jinja_env.globals['off_canvas_tab_bar'] = self.off_canvas_tab_bar
        self.app.jinja_env.globals['off_canvas_menu_toggle'] = self.off_canvas_menu_toggle

    def topBarMenu(self):
        """
        Includes the markup and jinja blocks for Foundation top bar menu.
        """
        self.top_bar = True
        self.app.jinja_env.globals["top_bar"] = self.top_bar

    def iconBarMenu(self):
        """
        Includes the markup and jinja blockks for Foundation iconbar menu.
        """
        self.icon_bar = True
        self.app.jinja_env.globals['icon_bar'] = self.icon_bar

    def sideNav(self):
        """
        Includes the markup and jinja blocks for Foundation iconbar menu.
        """
        self.side_nav = True
        self.app.jinja_env.globals['side_nav'] = self.side_nav

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
        
        app.jinja_env.globals['_dir'] = self._dir
        app.jinja_env.globals['lang'] = self.lang

        self.app = app

        if not hasattr(app, 'extensions'):
            app.extensions = {}
