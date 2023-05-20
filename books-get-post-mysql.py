from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)

#@app.route('/')
#def index():
#    return 'Hello World'

#this adds the /domain functionality
#called: Dynamic Routing
# the /name is a "dynamic argument"

#@app.route('/<name>')
#def print_name(name):
#    return 'Welcome , {}'.format(name)




def db_connection():

#external file to avoid hardcoding credentials
    credentials_file = open('mysql-credentials.json')
    cred_load = json.load(credentials_file)
    db_name = cred_load[0]['Database_name']
    db_user = cred_load[0]['Database_user']
    db_pass = cred_load[0]['Database_password']
    
    conn = None
    try:
        conn = pymysql.connect(
            host='sql10.freesqldatabase.com',
            database=db_name,
            user=db_user,
            password=db_pass,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.error as e:
      print(e)
    return conn

@app.route('/books', methods = ['GET','POST'])

def books():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor = cursor.execute("SELECT * FROM book")
        #For mysql we have to use dictionary keys
        books = [
            dict(id=row['id'], author=row['author'], language=row['language'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    
    if request.method == 'POST':

        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        
        #in pymysql we do not use ? placeholders, we use %s instead
        sql = """ INSERT INTO book (author, language, title)
                  VALUES (%s, %s, %s)"""
        cursor = cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created successfully",201


@app.route('/book/<int:id>', methods =['GET','PUT','DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book=None

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id=?",(id,))
        rows = cursor.fetchall()
        for r in rows:
            book = r
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something wrong 404"


    if request.method == 'PUT':
        sql = """UPDATE book
                 SET title=?,
                    author=?,
                    language=?
                 WHERE id=? """

        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        updated_book = {
            'id': id,
            'author': author,
            'language': language,
            'title': title
        }

        conn.execute(sql, (title,author,language,id))
        conn.commit()

        return jsonify(updated_book)
    
    if request.method == 'DELETE':
        sql = """DELETE FROM book WHERE id =?"""
        conn.execute(sql,(id,))
        conn.commit()
        return "The book with id: {} has been deleted.".format(id), 200
    

if __name__ == '__main__':
    app.run(debug=True)