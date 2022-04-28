from CloudSQLConnection import CloudSQLConnection
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

def tokenize_tweets(str):
    return tokenize.sent_tokenize(str.decode('utf-8'))

def sentiment_analysis_vader(sentences):
    summ = 0
    for sentence in sentences:
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)
        summ += ss['compound']
    return summ

def OrdoRating():
    cnx = CloudSQLConnection()
    cursor = cnx.cursor()

    query = (f"SELECT MovieId FROM MOVIES;")
    cursor.execute(query)
    MovieIdLst = [id[0] for id in cursor.fetchall()]
    
    for MovieId in MovieIdLst:
        try:
            query = (f"""
                UPDATE
                    MOVIES
                SET
                    ORDORATING = (
                    SELECT
                        FORMAT(T1.RATING,0) AS RATING
                    FROM (
                        SELECT(
                            ((SELECT
                                COUNT(*)
                            FROM
                                TWEETS
                            WHERE
                                (Sentiment='POS' or Sentiment='NEU') AND MOVIEID='{MovieId}')
                            / COUNT(*)) * 10) AS RATING
                        FROM
                            TWEETS
                        WHERE
                            MOVIEID='{MovieId}'
                    ) AS T1)
                WHERE MOVIEID='{MovieId}';
                """)
            cursor.execute(query)
            cnx.commit()
        except:
            continue
    cursor.close()

def main():
    cnx = CloudSQLConnection()
    cursor = cnx.cursor()

    query = (f"SELECT MovieId FROM MOVIES;")
    cursor.execute(query)
    MovieIdLst = [id[0] for id in cursor.fetchall()]
    
    for MovieId in MovieIdLst:
        query = (f"SELECT TWEETID, CONTENT FROM TWEETS WHERE MOVIEID = '{MovieId}' AND Sentiment is NULL;")
        cursor.execute(query)
        Tweets = cursor.fetchall()

        if (not len(Tweets)):
            continue

        POS = []
        NEG = []
        NEU = []
        for TweetId, Content in Tweets:
            sentences = []
            sentences.extend(tokenize_tweets(Content))
            score = sentiment_analysis_vader(sentences)
            if (score > 0):
                POS.append(TweetId)
            elif (score < 0):
                NEG.append(TweetId)
            else:
                NEU.append(TweetId)
                
        # POS
        try:
            query = (f"UPDATE TWEETS SET Sentiment = 'POS' WHERE TWEETID IN {tuple(POS)};")
            cursor.execute(query)
            cnx.commit()
        except:
            cnx.rollback()
        # NEG
        try:
            query = (f"UPDATE TWEETS SET Sentiment = 'NEG' WHERE TWEETID IN {tuple(NEG)};")
            cursor.execute(query)
            cnx.commit()
        except:
            cnx.rollback()
        # NEU
        try:
            query = (f"UPDATE TWEETS SET Sentiment = 'NEU' WHERE TWEETID IN {tuple(NEU)};")
            cursor.execute(query)
            cnx.commit()
        except:
            cnx.rollback()
    cursor.close()
    OrdoRating()


  
if __name__=="__main__":
    main()
