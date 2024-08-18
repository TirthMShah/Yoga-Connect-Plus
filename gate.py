from connections import connection
from models import User
import re
from app import app,redirect,request,url_for,render_template,session

# Get user by username and password(For sign in purpose).
def get_user(username,password):
    conn,cur = connection()
    cur.execute(f"SELECT * FROM USERS WHERE USERNAME = '{username}' AND PASSWORD = '{password}'")
    data = cur.fetchall()

    if data != []:
        data = data[0]
        cur.execute(f"SELECT POSTS FROM PROFILE WHERE USERNAME = '{username}'")
        posts = cur.fetchall()[0][0]
        if not posts:
            posts = []
        print(posts)
        return User(data[1],data[0],data[3],data[5],data[4],data[6], posts)
    else:
        return False


# Add a user to database(After Signing Up) if detailes are verified.
def add_user(name,username,password,mobile,age,gender,type):
    conn,cur = connection()
    cur.execute(f"INSERT INTO USERS VALUES('{name}','{username}','{password}','{mobile}',{age},'{gender}','{type}')")
    cur.execute(f"INSERT INTO Profile(USERNAME) VALUES('{username}')")
    conn.commit()
    conn.close()
    return User(username,name,mobile,gender,age,type)


# Validate User at time of Sign Up and add the user to DB using add_user() if all details are verified.
def validate_and_add_user(username,name,password,password2,mobile,gender,age,type):
    conn,cur = connection()
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[_$])[a-zA-Z_$0-9]{6,}$"

    if not re.search(pattern,username):
        return None

    cur.execute(f"SELECT USERNAME FROM USERS WHERE USERNAME = '{username}' ")
    try:
        existing_username=cur.fetchall()[0]
    except Exception:
        existing_username=[]

    if username in existing_username:
        return None
    if len(password) not in range(6,13):
        return None
    if password != password2:
        return None
    if len(str(mobile)) != 10:
        return None
    user = add_user(name,username,password,mobile,age,gender,type)
    conn.commit()
    conn.close()
    
    return user


@app.route('/signup',methods=['GET','POST'])
def signUp():
    if request.method == "POST":
        mobile = request.form["mobile"]
        username = request.form["username"]
        password = request.form["password1"]
        password2 = request.form["password2"]
        name = request.form["name"]
        gender = request.form["gender"]
        age = request.form["age"]
        type = request.form.get('type') 

        current_user = validate_and_add_user(username,name,password,password2,mobile,gender,age,type)

        if current_user:
            return redirect(url_for('home', username = username,login_alert = "True"))
        else:
            return render_template('SignUp.html', error = "Invalid Details.")

    return render_template('SignUp.html')


# SignIn
@app.route('/signin', methods=['GET', 'POST'])
def signIn():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        current_user = get_user(username,password)

        if current_user:
            return redirect(url_for('home', username = username,login_alert = True))
        else:
            return render_template('SignIn.html', error = "Invalid Credentials.")
    return render_template('SignIn.html')