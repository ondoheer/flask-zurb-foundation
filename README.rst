Flask-zurb-foundation
=======================



.. image:: https://travis-ci.org/ondoheer/flask-zurb-foundation.png?branch=master
   :target: https://travis-ci.org/ondoheer/flask-zurb-foundation


Flask-Zurb-Foundation packages `Foundation 5
<http://foundation.zurb.com/>`_ (*5.5.1*) into an extension as a blueprint called foundation.
So far it justs wrappes a project in the basic `Foundation 5
<http://foundation.zurb.com/>`_ styles and scripts.


Note:
--------

*I'm working on a few methods and macros that will allow to implement some of Foundation components quickly. Until they work I'll clean the master branch, it was getting kind of bloated with code that wasn't documented yet.*



Usage
------

In Flask
***********

Just wrapp your aplication like this::

    from flask_zurb_foundation import Foundation

    [...] # your initiation code here

    Foundation(app)


Now you will have a "*foundation/base.html*" template at your disposition to start developing your project fast enough.


Config Variables
******************

**config["FOUNDATION_MINIFIED"]** - *defaults to True* - Will load most libraries and css minified

**config["FOUNDATION_CDN"]** - *defaults to False* - Will load most libraries from CDN 

**config["FOUNDATION_ICONS"]** - *defaults to True* - will load the foundation icons css.

**config["FOUNDATION_TEXT_DIRECTION"]** - *defaults to 'ltr'* - if set to 'rtl' will switch text reading orientation for languages that are read from right to left.

**config["FOUNDATION_LANG"]** - *defaults to "en"* - accepts a string, will set the html attribute language.


In your templates
*******************

	{% extends "foundation/base.html" %}

	<!-- your html/jinja2 code goes here -->

Template Blocks
******************

Here are the template blocks you can build upon.
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

block head_scripts
+++++++++++++++++++

includes **modernizr.js**

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

block footer_scripts
+++++++++++++++++++++

JavaScript files should be linked here.
it loads jquery, jquery.cookie, modernizr, placeholder, fastclick and foundation JavaScript files.
It should be used with **super()**

Foundation components
***********************

There are a few built-in Foundation components macros.

The macros add the basic Foundation markup for them to work. So, basically they are just macros that wrap a **call**.

to use them just open a **call block** importing the component like so::

	{% call   components.topbar(class="fixed") %}

		<li>item1</li>
		<li>item2</li>
		<li>item3</li>
		<li>item4</li>
		<li>item5</li>

	{%	endcall %}

components.topbar
++++++++++++++++++

components.sidenav
++++++++++++++++++++

components.iconbar
+++++++++++++++++++

components.offcanvas
++++++++++++++++++++++
