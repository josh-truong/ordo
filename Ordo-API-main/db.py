#db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_movies():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM MOVIES;')
        movies = cursor.fetchall()
        if result > 0:
            movies = jsonify(movies)
        else:
            movies = 'Error'
    conn.close()
    return movies

def get_tweets(id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT
                TWEETID
            FROM
                TWEETS
            WHERE
                MOVIEID = %(id)s
            LIMIT
                10
        """, {
            'id': id
        })
        result = cursor.fetchall()
    
    if len(result) == 0:
        return {
                'message': "Invalid movie id.",
                'status': 400,
            }, 400

    conn.close()
    return jsonify(result)


def get_movie_tweet_percentage(id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT
                Sentiment
            FROM
                TWEETS
            WHERE
                MOVIEID = %(id)s
        """, {
            'id': id
        })
        result = cursor.fetchall()
    
    if len(result) > 0:
        N = len(result)
        neg_tweets = 0
        neu_tweets = 0
        pos_tweets = 0
        for row in result:
            if row['Sentiment'] == 'NEG':
                neg_tweets += 1
            elif row['Sentiment'] == 'NEU':
                neu_tweets += 1
            elif row['Sentiment'] == 'POS':
                pos_tweets += 1
        pos_percentage = int((pos_tweets / N) * 100) if pos_tweets != 0 else 0
        neu_percentage = int((neu_tweets / N) * 100) if neu_tweets != 0 else 0
        neg_percentage = int((neg_tweets / N) * 100) if neg_tweets != 0 else 0
        res = {
            'positive percentage': pos_percentage,
            'neutral percentage': neu_percentage,
            'negative percentage': neg_percentage,
            }
    else:
        return {
                'message': "Invalid movie id.",
                'status': 400,
            }, 400
    conn.close()
    return jsonify(res)
