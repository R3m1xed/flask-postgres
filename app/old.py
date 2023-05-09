from flask import Flask, render_template
import os
import json
import mysql.connector
#import mariadb

app = Flask(__name__)

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '11#cheesyCake',
    'database': 'demo'
}

# conn = mariadb.connect(
#     host='127.0.0.1',
#     port='3306',
#     user='root',
#     password='11#cheesyCake',
#     database='demo')

# cur = conn.cursor()

@app.route('/')
def home():
    import mysql.connector
    #conn = mysql.connector.connect(host = '127.0.0.1', user = 'root', password = '11#cheesyCake', port = 3306)
    conn = mysql.connector.connect(**config)
    #conn = mariadb.connect(**config)
    #conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM people")

    # serialize results into JSON
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    # return the results!
    return json.dumps(json_data)




    #return "connected to database"
    #return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)