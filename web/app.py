from flask import Flask, render_template, url_for, redirect, make_response


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def pages(name):
    if '..' in name or '//' in name or '~' in name:
            response = make_response(render_template('403.html'), 403)
            return response
    return redirect(url_for('static', filename=name))

@app.errorhandler(404)
def page_not_found(error):
    response = make_response(render_template('404.html'), 404)
    return response



if __name__ == "__main__":
     app.run(debug=True,host='0.0.0.0')
