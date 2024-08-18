import psycopg2

def connection():
    conn=psycopg2.connect(host="localhost",port="5432",user="postgres",password="hetu",database="YogaConnect+")
    cur=conn.cursor()
    return conn,cur
