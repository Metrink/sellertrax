from flask import Flask, render_template, jsonify, send_from_directory, session, redirect, request, make_response, g, url_for
from flask_sitemap import Sitemap

from logger import set_debug

app = Flask(__name__)

# have to update the Jinja template strings so they don't conflict w/Vue
jinja_options = app.jinja_options.copy()  # immutable dict
jinja_options['variable_start_string'] = '(('
jinja_options['variable_end_string'] = '))'
app.jinja_options = jinja_options


sitemap = Sitemap(app=app)


@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request(exception):
    pass


def render(template, title, **kwargs):
    """
    Helper function to render templates given a page title
    :param template:
    :param title:
    :param kwargs:
    :return:
    """
    return render_template(template, page_title=title, **kwargs)

#
# Pages
#
@app.route('/')
def home():
    return render('home.html', 'Seller Trax', python='Hello Python')


#
# Main
#
if __name__ == '__main__':
    set_debug()  # set the logging to debug
    app.run(debug=True)
