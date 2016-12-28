import psycopg2
import sys
import time
from flask import Flask, jsonify, request

app = Flask(__name__)

retries = 0
cur = None
while not cur and retries < 5:
    print('Connecting to database...')
    try:
        conn = psycopg2.connect(
            host='db',
            database='app',
            user='app',
            password='password',
        )
        cur = conn.cursor()
    except psycopg2.OperationalError as e:
        retries += 1
        sleep(5)

if not cur:
    print('Unable to connect to database after 5 retries')
    exit(1)

result = cur.execute('''
    SELECT EXISTS(
        SELECT 1
        FROM information_schema.tables
        WHERE table_name = 'app_user'
    )
    ''')

if not result:
    cur.execute('''
        CREATE TABLE "app_user" (
            id serial PRIMARY KEY,
            username varchar
        )
    ''')
    conn.commit()


@app.route('/')
def root():
    return jsonify({})


@app.route('/ping')
def ping():
    return jsonify(result='pong')


@app.route('/users/', methods=['POST'])
def create_user():
    username = request.args.get('username') if request.args.get('username') else 'username'
    cur.execute('''
        INSERT INTO app_user (username) VALUES (%s)
    ''', (username,))
    conn.commit()
    return jsonify(result='Successfully inserted user')


app.run(host='0.0.0.0')
