from sys import exception
from connections import connection
import json
import io
import base64

class User:
    def __init__(self, username, name,mobile, gender, age, typee , posts = []):
        self.username = username
        self.name = name
        self.mobile = mobile
        self.gender = gender
        self.age = age
        self.posts = self.get_posts()
        if typee == 'T':
            self.typee = 'Trainer'
            conn,cur = connection()
            cur.execute(f"SELECT TRAINEES FROM PROFILE WHERE USERNAME = '{self.username}'")
            
            try:
                self.trainees = cur.fetchall()[0][0]
            except Exception:
                self.trainees = []            
        else:
            self.typee = "General"
        print("type",self.typee)

    def get_posts(self):
        conn,cur = connection()
        cur.execute(f"SELECT POSTS FROM PROFILE WHERE USERNAME = '{self.username}'")
        try:
            posts = cur.fetchall()[0][0]
        except Exception:
            posts = None
        if posts:
            posts = [json.loads(post) for post in posts] 
            return posts
        else:
            return None

    def add_text_post(self,content):
            if self.posts == None:
                self.posts = []
            self.posts.append({"username" : self.username,"type": "text", "content": content, "likes": 0, "dislikes": 0})
            posts = [json.dumps(post) for post in self.posts]
            try:
                conn,cur = connection()
                cur.execute(f"UPDATE PROFILE SET posts = ARRAY{posts} WHERE USERNAME = '{self.username}' ")
                conn.commit()
                conn.close()
                return True
            except Exception:
                return False

    def add_post(self,path,content):
            if self.posts == None:
                self.posts = []
            self.posts.append({"username" : self.username,"type": "text_image", "img_content": path,"txt_content" : content, "likes": 0, "dislikes": 0})
            posts = [json.dumps(post) for post in self.posts]
            try:
                conn,cur = connection()
                cur.execute(f"UPDATE PROFILE SET posts = ARRAY{posts} WHERE USERNAME = '{self.username}' ")
                conn.commit()
                conn.close()
                return True
            except Exception:
                return False
   
    def add_image_post(self,path):
        if self.posts == None:
                 self.posts = []
        self.posts.append({"username" : self.username,"type": "image", "content": path, "likes": 0, "dislikes": 0})
        posts = [json.dumps(post) for post in self.posts]
        print(posts)
        
        try:
            conn,cur = connection()
            cur.execute(f"UPDATE PROFILE SET posts = ARRAY{posts} WHERE USERNAME = '{self.username}' ")
            conn.commit()
            conn.close()
            return True
        except Exception:
            return False
        
    def get_trainees(self):
        conn,curr = connection()
        curr.execute(f"SELECT TRAINEES FROM PROFILE WHERE USERNAME = '{self.username}' ")
        trainees = curr.fetchall()
        trainees = trainees[0][0]
        if trainees:
            trainees = list(trainees)
        else:
            trainees = []
        
        return trainees
    
    def add_trainees(self,username):
        conn,curr = connection()
        trainees = self.get_trainees()
        trainees.append(username)
        self.trainees = trainees
        curr.execute(f"UPDATE PROFILE SET TRAINEES = ARRAY{trainees} WHERE USERNAME = '{self.username}' ")
        conn.commit()
        conn.close()


class Description:
    def __init__(self,body_part, definition, benefits, techniques, duration, results, safety_Considerations):
        self.body_part = body_part
        self.definition = definition
        self.benefits = benefits
        self.techniques = techniques
        self.duration = duration
        self.results = results
        self.safety_Considerations = safety_Considerations
    
def get_yoga_data(part):
    conn,curr = connection()
    curr.execute(f"SELECT * FROM DESCRIPTION WHERE BODY_PART = '{part}'")
    data = curr.fetchall()[0]
    data = Description(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
    return data

def fetch_posts():
    conn,cur=connection()
    cur.execute("SELECT posts FROM Profile WHERE POSTS IS NOT NULL")
    posts = cur.fetchall()
    data=[]
    for post in posts:
        for i in post:
            data.extend(i)
    posts = [json.loads(post)  for post in data]
    return posts

def get_list(column,username):
    conn,curr = connection()
    curr.execute(f"SELECT {column} FROM PROFILE WHERE USERNAME='{username}'")
    try:
        data = curr.fetchall()[0][0]
    except Exception:
        data = []
    return data

class Profile(User):
    def __init__(self,user):
        super().__init__(user.username, user.name, user.mobile, user.gender, user.age, user.typee, user.posts)
        self.followers = self.get_list("FOLLOWERS")
        self.following = self.get_list("FOLLOWING")
        self.trainees = self.get_list("TRAINEES")

    def get_list(self,column):
        conn,curr = connection()
        curr.execute(f"SELECT {column} FROM PROFILE WHERE USERNAME='{self.username}'")
        try:
            data = curr.fetchall()[0][0]
            if not data:
                data = []
        except Exception:
            data = []
        return data
    
    # def add_followers(self,username):
    #     conn,curr = connection()
    #     trainees = self.get_trainees()
    #     trainees.append(username)
    #     self.trainees = trainees
    #     curr.execute(f"UPDATE PROFILE SET FOLLOWERS = ARRAY{trainees} WHERE USERNAME = '{self.username}' ")
    #     conn.commit()
    #     conn.close()



    # def get_followers(self):
    #     conn,curr = connection()
    #     curr.execute(f"SELECT FOLLOWERS FROM PROFILE WHERE USERNAME='{self.username}'")
    #     data = curr.fetchone()
    #     print("data",data)

    #     if data != []:
    #         data = data[0][0]
    #         data = list(data)
    #     else:
    #         data = []

    #     return list(data)
    
    # def get_following(self):
    #     conn,curr = connection()
    #     curr.execute(f"SELECT FOLLOWING FROM PROFILE WHERE USERNAME='{self.username}'")
    #     data = curr.fetchone()
    #     print("data",data)

    #     if data != []:
    #         data = data[0][0]
    #         data = list(data)
    #     else:
    #         data = []

    #     return list(data)