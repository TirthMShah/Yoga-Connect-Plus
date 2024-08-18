from models import User, get_list, Profile
from app import app, render_template, request, redirect, url_for
from explore import get_user_by_username
from connections import connection
from flask import jsonify

@app.route('/dashboard<username>',methods=["POST","GET"])
def dashboard(username):
    current_user = get_user_by_username(username)
    
    posts = current_user.get_posts()
    return render_template('Dashboard.html',current_user = current_user,posts = posts)


# @app.route('/image_post/<username>',methods=["GET","POST"])
# def image_post(username):
#     current_user = get_user_by_username(username)
#     if request.method == "POST":
#         image_data = request.json.get('image')
#         if image_data:
#             if image_data.endswith('.jpg') or image_data.endswith(".png"):
#                 current_user.add_image_post(image_data)
#         return jsonify({"status":"success"})
    
# @app.route('/text_post/<username>',methods=["GET","POST"])
# def text_post(username):
#     current_user = get_user_by_username(username)
#     if request.method == "POST":
#         text_data = request.json.get("text")
#         if text_data:
#             current_user.add_text_post(text_data)
#         return jsonify({"status":"success"})
    
@app.route('/post/<username>',methods=["GET","POST"])
def post(username):
    current_user = get_user_by_username(username)
    if request.method == "POST":
        image_data = request.json.get('image')
        text_data = request.json.get("text")

        if image_data and text_data :
             if image_data.endswith('.jpg') or image_data.endswith(".png"):
                current_user.add_post(image_data,text_data)

        elif image_data:
            if image_data.endswith('.jpg') or image_data.endswith(".png"):
                current_user.add_image_post(image_data)
        elif text_data:
            current_user.add_text_post(text_data)
        
        return jsonify({"status":"success"})

@app.route('/profile/<username>/<user>',methods=["GET","POST"])
def profile(user,username):

    user = get_user_by_username(user)
    current_user = get_user_by_username(username)
    
    if request.method=="POST":
        user.add_trainees(current_user.username)
        return render_template("Profile.html",user = user,current_user = current_user)

    return render_template("Profile.html",user = user,current_user = current_user)


@app.route("/del")
def del_account():
    conn,cur=connection()
    username=request.args.get("username")
    cur.execute(f"delete from profile where username='{username}';")
    cur.execute(f"delete from users where username='{username}';")
    conn.commit()
    conn.close()
    return redirect(url_for("home",delAccount_alert = True))


@app.route("/follow/<username>/<user_username>",methods=["GET","POST"])
def follow(username,user_username):
    current_user = get_user_by_username(username)
    profile = get_user_by_username(user_username)
    if request.method == "POST":

        con,cur=connection()

        if profile != current_user:

            if current_user not in profile.followers:
                profile.followers.append(current_user.username)
                current_user.following.append(profile.username)

                cur.execute(f"UPDATE PROFILE SET FOLLOWING = ARRAY{current_user.following} WHERE USERNAME ='{current_user.username}'")
                cur.execute(f"UPDATE PROFILE SET FOLLOWERS = ARRAY{profile.followers} WHERE USERNAME ='{profile.username}'")
                con.commit()
                con.close()

    return render_template("Profile.html",user = get_user_by_username(profile),current_user = get_user_by_username(current_user))


@app.route("/unfollow/<username>/<user_username>",methods=["GET","POST"])
def unfollow(username,user_username):
    current_user = get_user_by_username(username)
    profile = get_user_by_username(user_username)
    
    if request.method == "POST":
        con,cur=connection()

        if profile.username != current_user.username:
            if current_user.username in profile.followers:
                profile.followers.remove(current_user.username)
                current_user.following.remove(profile.username)
                if profile.followers == []:
                    cur.execute(f"UPDATE PROFILE SET FOLLOWERS = null WHERE USERNAME ='{profile.username}'")
                else :
                    cur.execute(f"UPDATE PROFILE SET FOLLOWERS = ARRAY{profile.followers} WHERE USERNAME ='{profile.username}'")

                if current_user.following == []:
                    cur.execute(f"UPDATE PROFILE SET FOLLOWING = null WHERE USERNAME ='{current_user.username}'")
                else:
                    cur.execute(f"UPDATE PROFILE SET FOLLOWING = ARRAY{current_user.following} WHERE USERNAME ='{current_user.username}'")
                con.commit()
                con.close()
    return render_template("Profile.html",user = get_user_by_username(profile),current_user = get_user_by_username(current_user))