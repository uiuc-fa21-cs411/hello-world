from flask import Flask, render_template, request
import mysql.connector
from signal import SIGINT, signal

app = Flask(__name__)
cnx = mysql.connector.connect(user='dm42', password='', host='localhost', database='dm42_database')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        title = details['title']
        length = details['length']
        genre = details['genre']
        cur = cnx.cursor()
        cur.execute("INSERT INTO MyMovies(title, length, genre) VALUES (%s, %s, %s)", (title, length, genre))
        cnx.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


@app.route('/showall', methods=['GET'])
def showall():
    cur = cnx.cursor()
    cur.execute("SELECT * FROM MyMovies")
    res = '\n'.join([str(tid) + ', ' + title + ', ' + genre + ', ' + str(length) for tid, title, genre, length in cur])
    cur.close()
    return res


def sigint_handler(signal_received, frame):
    global cnx
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    cnx.close()
    exit(0)


if __name__ == '__main__':
    signal(SIGINT, sigint_handler)
    app.run()
