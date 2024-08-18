from connections import connection
from app import app,request,render_template,url_for,redirect
from models import User,fetch_posts,Profile
import random

def get_data():
    conn,cur = connection()
    cur.execute(f"SELECT USERNAME,NAME,TYPE FROM USERS")
    users = cur.fetchall()

    data = [{'username':user[0],'name':user[1],'type':user[2]} for user in users]
    return data

def get_user_by_username(username):
    conn,cur = connection()
    cur.execute(f"SELECT * FROM USERS WHERE USERNAME = '{username}' ")
    data = cur.fetchall()

    if data != []:
        data = data[0]
        cur.execute(f"SELECT POSTS FROM PROFILE WHERE USERNAME = '{username}'")
        posts = cur.fetchall()[0][0]
        return Profile(User(data[1],data[0],data[3],data[5],data[4],data[6], posts))
    else:
        return None  

@app.route('/explore',methods=["GET","POST"])
def explore():
    data = get_data()
    posts = fetch_posts()
    random.shuffle(posts)
    posts = posts[:15]
    
    current_user = get_user_by_username(request.args.get("username"))
    if current_user:
        posts = [post for post in posts if post["username"] != current_user.username]
        for details in data:
            if details["username"] == current_user.username:
                data.remove(details)
    else:
        posts = [post for post in posts if post["username"]]

    

    if request.method=="POST":
        conn,curr = connection()
        data = get_data()
        posts = fetch_posts()
        random.shuffle(posts)
        posts = posts[:15]
        curr.execute(f"SELECT * FROM users WHERE username LIKE '%{request.form.get("search")}%'")
        search_results = curr.fetchall()
        if current_user:    
            return render_template('Explore.html',data = data,posts = posts,search_results=search_results,username=current_user.username)
        else:
            return render_template('Explore.html',data = data,posts = posts,search_results=search_results)

    if current_user:
        return render_template('Explore.html',username=current_user.username,data = data,posts=posts)
    else:
        return render_template('Explore.html',username=None,data = data,posts=posts)



@app.route('/search/<username>/<search>',methods=["GET","POST"])
def search(username,search):
        ...