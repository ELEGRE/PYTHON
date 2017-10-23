import sqlite3
import random

def connect():
    conn=sqlite3.connect("app.db")#Connect To Database
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS app1 (id INTEGER PRIMARY KEY,FIRST_NAME text, LAST_NAME text, ADRESS text, TEL integer)")
    print ("Opened database successfully");
    conn.commit()
    conn.close()
    
def insert(FIRST_NAME,LAST_NAME,ADRESS,TEL):
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO app1 VALUES (NULL,?,?,?,?)",(FIRST_NAME,LAST_NAME,ADRESS,TEL)) 
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM app1")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(FIRST_NAME="",LAST_NAME="",ADRESS="",TEL=""):
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM app1 WHERE FIRST_NAME =? OR LAST_NAME=? OR ADRESS=? OR TEL=?", (FIRST_NAME,LAST_NAME,ADRESS,TEL))
    rows=cur.fetchall()
    conn.close()
    return rows
    
def delete(id):
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM app1 WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,FIRST_NAME,LAST_NAME,ADRESS,TEL):
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("UPDATE app1 SET FIRST_NAME =?, LAST_NAME =?,ADRESS =?, TEL=? WHERE id=?",(FIRST_NAME,LAST_NAME,ADRESS,TEL,id))
    conn.commit()
    conn.close()

connect()

