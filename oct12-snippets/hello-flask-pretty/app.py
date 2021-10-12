import mysql.connector
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for


app = Flask(__name__)
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == "POST":
#         details = request.form
#         title = details['title']
#         length = details['length']
#         genre = details['genre']
#         cur = cnx.cursor()
#         cur.execute("INSERT INTO MyMovies(title, length, genre) VALUES (%s, %s, %s)", (title, length, genre))
#         cnx.commit()
#         cur.close()
#         return 'success'
#     return render_template('index.html')


@app.route('/', methods=['GET'])
def index():
    title = 'CS411: Sample Project 2'
    return render_template('index.html', title=title)


@app.route('/query', methods=['POST'])
def process_query():
    print(request)
    sql = request.form['query_string']
    return {
        "query_string": sql,
        "data": {
            "labels": [['col1'], ['col2']],
            "values": [
                [1], 
                [2]
            ]
        }
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10001)

