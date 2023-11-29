import flask
from flask import Flask, request

app = Flask(__name__)

from forms import GreetingForm

import config

app.config.from_object(config.Config)


@app.route('/')
def hello_world():
    form = GreetingForm()
    return flask.render_template('index.html', form=form)


@app.route('/greeting', methods=['POST'])
def greeting_post():
    form = GreetingForm()
    if not form.validate_on_submit():
        return flask.redirect('/')
    return flask.redirect('/hello?name=' + form.username.data)


@app.route('/hello', methods=['GET'])
def greeting():
    return flask.render_template("greeting.html", name=request.args['name'])


if __name__ == '__main__':
    app.run()
