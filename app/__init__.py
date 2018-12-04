#!/usr/bin/python3


from flask import Flask, make_response, redirect, render_template, request

__author__ = "@ivanleoncz"

app = Flask(__name__)


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


from app.views import index
from app.views import login
from app.views import panel
from app.views import template
