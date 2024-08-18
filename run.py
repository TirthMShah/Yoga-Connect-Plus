import explore,gate,VC,description,dashboard
from app import app,request,render_template

@app.route('/')
def home():
    username = request.args.get("username")
    login_alert = request.args.get('login_alert')
    logout_alert = request.args.get('logout_alert')
    delAccount_alert = request.args.get('delAccount_alert')
    if username:
        return render_template("Home.html",username = username,login_alert=login_alert)
    else:
        return render_template("Home.html",logout_alert=logout_alert,delAccount_alert = delAccount_alert)

app.run(host='0.0.0.0', port=5000, debug=True)