from flask import Flask, render_template
import os
import psycopg2
import ssl

#Make sure to adjust the password to pass you wish.
conn = psycopg2.connect(database="mydatabase",
                    host="flaskdb",
                    user="postgres",
                    password="MYDATABASEPASSWORD",
                    port="5432")

app = Flask(__name__)

#To enable HTTPS for your app
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('./server.crt', './server.key')


@app.route('/')
def home():
  
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    result = cur.fetchall()
    

    return str(result)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    #Remove ssl_context to remove https, or keep it if you wish to enable https
    app.run(debug=True, host='0.0.0.0', port=port, ssl_context=context)
