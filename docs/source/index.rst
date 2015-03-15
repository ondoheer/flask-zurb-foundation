.. Zurb-Foundation-Flask documentation master file, created by
   sphinx-quickstart on Fri Feb 27 14:22:40 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Zurb-Foundation-Flask's documentation!
=================================================



Flask-Zurb-Foundation packages `Foundation 5
<http://foundation.zurb.com/>`_ (*5.5.1*) into an extension as a blueprint called foundation.
So far it justs wrappes a project in the basic `Foundation 5
<http://foundation.zurb.com/>`_ styles and scripts.


Note:
--------

*There was a problem when downloading it from pypi, it's corrected now. As of version 0.1.3 it does work when installing from pipy.*



Usage
------

In Flask
***********

Just wrapp your aplication like this::

    from fask_zurb_foundation import Foundation

    [...] # your initiation code here

    Foundation(app)


Now you will have a "*foundation/base.html*" template at your disposition to start developing your project fast enough.

In your templates
*******************

add this at the top of your jinja2 html files::

	{% extends "foundation/base.html" %}

 		<!-- your html/jinja2 code goes here -->


Template Blocks
******************

Here are the template blocks yoou can build upon.
To use them just call::

	{% block <blockname> %}
		...your code...
	{% endblock %}


block doc
++++++++++

Starts before declaring the <!DOCTYPE>, can be used to overwrite everything.

block html_attribs
+++++++++++++++++++

opening <html> tag, used to add attributes to it.


block html
+++++++++++

includes everything inside the <html> tag.


block head
+++++++++++

includes everything inside the <head> tag. This includes the <title>, <meta> and <link> tags, it should be used with **super()** so it keeps calling the foundation CSS

like so::

	{% block head %}
		{{ super() }}
		...your code...
	{% endblock head %}


block metas
++++++++++++

it just includes::

	<meta name="viewport" content="width=device-width, initial-scale=1.0">

it should be called with **super()** unless you want to overwritte this behaviour.

block styles
++++++++++++

this includes the foundation css and the foundation-icons css. 

it should be used with **super()**

block body_attributes
++++++++++++++++++++++

block inside the opening <body> tag. Used to add classes, id or data attributes to it.


block navbar
+++++++++++++++

Goes before block content, just a way to organize your code.

block content
+++++++++++++++

main web content should go here

block footer
+++++++++++++

goes before the scripts block 

block scripts
++++++++++++++

JavaScript files should be linked here.
it loads jquery, jquery.cookie, modernizr, placeholder, fastclick and foundation JavaScript files.
It should be used with **super()**

Defaults
----------

By default it loads all the libraries locally, you can change it by 

setting the local parameter to False::

	
	from fask_zurb_foundation import Foundation

    [...] # your initiation code here

    Foundation(app, local=False)



What it loads locally
----------------------

It loads different libraries automatically (support for choosing might be added in the future). Some of these come with Foundation 5

1. `HTML5 shiv
<https://github.com/aFarkas/html5shiv>`_ - The HTML5 Shiv enables use of HTML5 sectioning elements in legacy Internet Explorer and provides basic HTML5 styling for Internet Explorer 6-9, Safari 4.x (and iPhone 3.x), and Firefox 3.x.

2. `RespondJS
<https://github.com/scottjehl/Respond>`_ - A fast & lightweight polyfill for min/max-width CSS3 Media Queries

3. `FastClick
<https://github.com/ftlabs/fastclick>`_ - FastClick is a simple, easy-to-use library for eliminating the 300ms delay between a physical tap and the firing of a click event on mobile browsers.

4. `jQuery
<http://jquery.com/>`_ - v 2.1.3

5. `Modernizer
<http://modernizr.com/>`_ - JavaScript library that detects HTML5 and CSS3 features in the user’s browser


What it loads when you set local to False
------------------------------------------

1. Foundation 5.5 from a CDN

