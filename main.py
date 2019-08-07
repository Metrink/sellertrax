import vbuild

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


def render(template, title, vue=(), **kwargs):
    """
    Helper function to render templates given a page title
    :param template: template to render
    :param title: title of the page
    :param vue: the vue components to render on this page
    :param kwargs:
    :return:
    """

    if not isinstance(vue, list):
        vue = [vue]

    vue_html = []
    vue_script = []
    vue_style = []

    for v in vue:
        if not str(v).endswith('.vue'):
            v = str(v) + '.vue'

        res = vbuild.render("static/vue/{}".format(v))

        vue_html.append(res.html)
        vue_script.append(res.script)
        vue_style.append(res.style)

    return render_template(
        template,
        page_title=title,
        vue_html=vue_html,
        vue_script=vue_script,
        vue_style=vue_style,
        **kwargs
    )

#
# Pages
#
@app.route('/')
def home():
    return render('home.html', 'Seller Trax', vue='prospect_card', python='Hello Python')


#
# Main
#
if __name__ == '__main__':
    set_debug()  # set the logging to debug
    app.run(debug=True)
