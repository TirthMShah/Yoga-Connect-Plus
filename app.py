from flask import Flask, render_template, request, redirect, url_for,Response,session
# Create a flask app instance.
app = Flask(__name__)

app.secret_key = 'hetu' # For OTP rest API purpose.
