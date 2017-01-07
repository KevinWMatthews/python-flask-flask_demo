Working through a flask tutorial from tutorialspoint.

https://www.tutorialspoint.com/flask

Start by running hello.py and then browsing to 127.0.0.1:5000. That will get your feet wet.
This covers the basics of running the webserver, browsing to a URL, and binding URLs to methods.

Next, login.py and login.html cover parsing data from forms using POST and GET.
After running login.py, be sure to browse to the file login.html!
Do not browse to 127.0.0.1/login.

Next, dynamically generate HTML using generate_html.py.
This is done using the Jinja2 template engine and its render_template() method.
Templates are traditionally located in the /templates directory.

More complex templates can be found in loops.py and templates/loops.html.

During development, CSS and JS are traditionally read from a /static directory.
During run time, these are provided by the server.
An example of this is provided by js_and_css.py. This uses a template and javascript.

