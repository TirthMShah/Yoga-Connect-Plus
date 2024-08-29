import psycopg2

def connection():
    conn=psycopg2.connect(host="yogaconnect_user",port="5432",user="dpg-cr8cm2q3esus73b4sil0-a.oregon-postgres.render.co",password="ms2WdMIdUJ9fCh1JsMvXBOK6O93gozYn",database="yogaconnect")
    cur=conn.cursor()
    return conn,cur
