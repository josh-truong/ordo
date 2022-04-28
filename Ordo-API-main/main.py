#main.py
from flask import Flask, request
from db import get_movies, get_tweets, get_movie_tweet_percentage
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS, cross_origin

app = Flask(__name__)
limiter = Limiter(
  app,
  key_func=get_remote_address,
  default_limits=["1000/day", "200/hour"]
)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/movies')
@cross_origin()
@limiter.limit("10/second", override_defaults=False)
def movies():
    return get_movies()


@app.route('/tweets')
@cross_origin()
@limiter.limit("10/second", override_defaults=False)
def tweets():
    movieId = request.args.get('movieId')
    return get_tweets(movieId)

@app.route('/movie_tweet_percentage')
@cross_origin()
@limiter.limit("10/second", override_defaults=False)
def movie_tweet_percentage():
    movieId = request.args.get('movieId')
    return get_movie_tweet_percentage(movieId)

if __name__ == '__main__':
  app.run()
