import logging

from flask import Flask, render_template
from flask_basicauth import BasicAuth


app = Flask(__name__)


stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)

app.config.update({
    'BASIC_AUTH_USERNAME': 'foo',
    'BASIC_AUTH_PASSWORD': 'bar',
})

auth = BasicAuth(app)


@app.route('/')
@auth.required
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
