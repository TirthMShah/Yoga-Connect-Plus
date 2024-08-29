from flask import Flask, render_template, request, redirect, url_for,Response,session
# Create a flask app instance.
app = Flask(__name__)

app.secret_key = 'tirth' # For OTP rest API purpose.
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://yogaconnect_user:ms2WdMIdUJ9fCh1JsMvXBOK6O93gozYn@dpg-cr8cm2q3esus73b4sil0-a.oregon-postgres.render.com/yogaconnect'
