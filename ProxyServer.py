from flask import Flask, render_template, request, jsonify, redirect
from requests import get, post

app = Flask(__name__)

SITE_NAME = "http://192.168.43.114/"


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
  return get(f'{SITE_NAME}{path}').content


if __name__ == '__main__':
    app.run()