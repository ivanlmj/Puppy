#!/usr/bin/python3


from flask import (
    Flask,
    abort,
    make_response,
    redirect,
    render_template,
    request,
    session
)

__author__ = "@ivanleoncz"

app = Flask(__name__)


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

from app.views import api
from app.views import index
from app.views import login
from app.views import panel_actions
from app.views import panel
from app.views import template
