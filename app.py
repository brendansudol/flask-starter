import logging

from flask import Flask, render_template


app = Flask(__name__)


stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
