import requests
import json
import pymysql
import time


def get_movie_ids():
    #get the list of movie ids from the api 
    url = "https://online-movie-database.p.rapidapi.com/title/get-most-popular-movies"

    querystring = {"currentCountry":"US","purchaseCountry":"US","homeCountry":"US"}

    headers = {
        # "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com", #isku8282@colorado.edu
        # "X-RapidAPI-Key": "7e761221ebmshe0bb7c0a26b6ecap1eca95jsn8a992bbbf8a7"

        # "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com", #ishan.kumar@gmail.com
	    # "X-RapidAPI-Key": "36064eeaf9msh649fe238723d56cp16ccb1jsn1a73289dafad"

        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com",  #ishan.kumar@yahoo.com
	    "X-RapidAPI-Key": "ecff70f201msh6844cee40978cd8p156cc4jsndbf1e28ea030"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    newResponse = response.text
    # print(newResponse)

    # test = ["/title/tt11138512/","/title/tt4123432/","/title/tt6710474/","/title/tt7657566/","/title/tt13560574/","/title/tt1877830/","/title/tt12412888/","/title/tt12141112/","/title/tt3706352/","/title/tt5108870/","/title/tt9419884/","/title/tt10872600/","/title/tt11291274/","/title/tt13610562/","/title/tt10698680/","/title/tt10366460/","/title/tt13320622/","/title/tt8178634/","/title/tt14114802/","/title/tt4998632/","/title/tt1160419/","/title/tt14439896/","/title/tt4123430/","/title/tt2463208/","/title/tt8097030/","/title/tt3183660/","/title/tt0049833/","/title/tt5834426/","/title/tt2180339/","/title/tt10886166/","/title/tt7740496/","/title/tt8851148/","/title/tt6467266/","/title/tt6856242/","/title/tt2953050/","/title/tt10515864/","/title/tt11514780/","/title/tt14107554/","/title/tt10293406/","/title/tt0335345/","/title/tt10323676/","/title/tt1745960/","/title/tt3794354/","/title/tt8115900/","/title/tt13403046/","/title/tt11245972/","/title/tt3581652/","/title/tt11271038/","/title/tt1464335/","/title/tt9731534/","/title/tt9032400/","/title/tt10648342/","/title/tt2382320/","/title/tt5315212/","/title/tt11301946/","/title/tt4513678/","/title/tt9620288/","/title/tt3402236/","/title/tt11286314/","/title/tt13235822/","/title/tt6264654/","/title/tt0241527/","/title/tt10370710/","/title/tt0468569/","/title/tt14168394/","/title/tt7131622/","/title/tt12996154/","/title/tt11214590/","/title/tt0111161/","/title/tt14549466/","/title/tt12789558/","/title/tt0068646/","/title/tt0120338/","/title/tt8041270/","/title/tt0092099/","/title/tt12663250/","/title/tt0395495/","/title/tt4154796/","/title/tt11003218/","/title/tt7286456/","/title/tt15033192/","/title/tt10838180/","/title/tt8847712/","/title/tt18689424/","/title/tt0896798/","/title/tt13872248/","/title/tt14060232/","/title/tt1911644/","/title/tt6334354/","/title/tt4263482/","/title/tt1856101/","/title/tt1879016/","/title/tt15398776/","/title/tt11252248/","/title/tt14039582/","/title/tt9376612/","/title/tt0816692/","/title/tt9115530/","/title/tt4244994/","/title/tt9243804/"]

    splitValues = newResponse.split(",")
    print(splitValues)

    # print("############################################")

    movieIDsArray = []
    for movieValue in splitValues:
        # print("This is the movieValue: ", movieValue)
        secondSplitValues = movieValue.split("/")
        # print("These are the second split values, ", secondSplitValues)
        movieIDsArray.append(secondSplitValues[2])
    print("These are the updated movie ids: ", movieIDsArray)
    return movieIDsArray

def get_movie_info(movieIdValue, cursor, connection):
    url = "https://online-movie-database.p.rapidapi.com/title/get-overview-details"
    # testMovieID = 'tt1745960' #(movie that isn't released yet)
    # testMovieID = 'tt10293406'
    querystring = {"tconst":movieIdValue,"currentCountry":"US"}

    headers = {
        # "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com", #isku8282@colorado.edu
        # "X-RapidAPI-Key": "7e761221ebmshe0bb7c0a26b6ecap1eca95jsn8a992bbbf8a7"

        # "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com", #ishan.kumar@gmail.com
	    # "X-RapidAPI-Key": "36064eeaf9msh649fe238723d56cp16ccb1jsn1a73289dafad"

        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com", #ishan.kumar@yahoo.com
	    "X-RapidAPI-Key": "ecff70f201msh6844cee40978cd8p156cc4jsndbf1e28ea030"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    test = json.loads(response.text)
    movieTitle = None
    if "title" in test['title']:
        movieTitle = test['title']['title']
    
    year = None
    if "year" in test['title']:
        year = int(test['title']['year'])

    imgURL = None
    if "url" in test['title']['image']:
        imgURL = test['title']['image']['url']

    releaseDate = None
    if "releaseDate" in test:
        releaseDate = test['releaseDate']

    runningTime = None
    if "runningTimeInMinutes" in test['title']:
        runningTime = int(test['title']['runningTimeInMinutes'])
    
    rating = None
    ratingReason = None
    if "certificates" in test:
        if "certificate" in test['certificates']['US'][0]:
            rating = test['certificates']['US'][0]['certificate']
        if "ratingReason" in test['certificates']['US'][0]:
            ratingReason = test['certificates']['US'][0]['ratingReason']

    genres = None
    if "genres" in test:    
        genres = test['genres']
    
    plotOutline = None
    if "text" in test['plotOutline']:
        plotOutline = test['plotOutline']['text']

    plotSummary = None
    if "plotSummary" in test:
        if "text" in test['plotSummary']:
            plotSummary = test['plotSummary']['text']


    # print("Certificate values", certificateValues)
    print("This is the movieId: ", movieIdValue)
    print("This is the movieTitle: ", movieTitle)
    print("This is the year: ", year)
    print("This is the imgURL: ", imgURL)
    print("This is the releaseDate: ", releaseDate)
    print("This is the runningTime: ", runningTime)
    print("This is the rating: ", rating)
    print("This is the ratingReason: ", ratingReason)
    print("These are the genres: ", genres)
    print("This is the plotOutline: ", plotOutline)
    print("This is the plotSummary: ", plotSummary)

#     #     # Trusted Connection to Named Instance
    # connection = pymysql.connect(host='34.133.98.237',user='root', password='OrdoAtls4214!',database='ORDO', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
 
    # cursor = connection.cursor()
 
    strArray = str(genres)
    strArray = strArray.replace("[","").replace("]","")

    print(strArray)

    try:
        cursor.execute("INSERT INTO `MOVIES` (`MOVIEID`, `TITLE`, `YEAR`, `IMGURL`, `RELEASEDATE`, `RUNNINGTIME`, `RATING`, `RATINGREASON`, `GENRES`, `PLOT`, `PLOTOUTLINE`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(movieIdValue, movieTitle, year, imgURL, releaseDate, runningTime, rating, ratingReason, strArray, plotSummary, plotOutline))
    except:   
        print(" duplicte key")
    connection.commit()

    # print([movieIdValue, movieTitle])
    # return [movieIdValue, movieTitle]
    return movieTitle

    # cursor.close()
    # connection.close()
    
def get_movie_tweets(movieId, movieTitle, cursor, connection):
    headers = {
        "Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAACH1agEAAAAAJcKTWcIMf2oMEcSdd1%2FhXfReNGk%3DztstIYk4UowOUsimXOce2WcQdHwTWzkhgqdjkwSnNy0zooyuFO"
    }
    # movieTitle = "the suicide squad"
    # param1 = (movieTitle + " movie lang:en")

    # print(movieTitleIDArray[1])
    # param1 = (movieTitleIDArray[1] + " movie lang:en")

    param1 = (movieTitle + " movie lang:en")
    print(param1.encode())
    querystring = {"query":param1.encode(),"max_results":50}
    url = "https://api.twitter.com/2/tweets/search/recent"

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    allTweets = json.loads(response.text)
    # print(allTweets['data'][0]['text'])

    # connection = pymysql.connect(host='34.133.98.237',user='root', password='OrdoAtls4214!',database='ORDO', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    # cursor = connection.cursor()

    if 'data' in allTweets:
        allTweetsData = allTweets['data']
        for index in range(len(allTweetsData)):
            tweetId = allTweetsData[index]['id']
            tweetText = allTweetsData[index]['text']
            print("---------")
            print(tweetText)
            try:
                cursor.execute("INSERT INTO `TWEETS` (`MOVIEID`, `TWEETID`, `CONTENT`) VALUES(%s, %s, %s)",(movieId, tweetId, str(tweetText)))
            except:
                continue
    else:
        allTweetsData = None

    # testMovieID = 'tt2883738'
    # for index in range(len(allTweetsData)):
    #     tweetId = allTweetsData[index]['id']
    #     tweetText = allTweetsData[index]['text']
    #     print("---------")
    #     print(tweetText)
    #     cursor.execute("INSERT INTO `TWEETS` (`MOVIEID`, `TWEETID`, `CONTENT`) VALUES(%s, %s, %s)",(movieId, tweetId, str(tweetText)))
        # print("THIS IS THE TWEET ID", tweetId, "THIS IS THE TEXT", tweetText)
    # cursor.execute("INSERT INTO `TWEETS` (`MOVIEID`, `TWEETID`, `CONTENT`) VALUES(%s, %s, %s)",(testMovieID, movieTitle, int(year), imgURL, releaseDate, int(runningTime), rating, ratingReason, str(genre), plot))

    connection.commit()

    # cursor.close()
    # connection.close()


################## FUNCTION CALLS ##################

count = 0
allMovieIdsArr = get_movie_ids()
connection = pymysql.connect(host='34.133.98.237',user='root', password='OrdoAtls4214!',database='ORDO', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

for movieId in allMovieIdsArr:
    testMovieTitle = get_movie_info(movieId, cursor, connection)
    count +=1
    if count % 5 == 0:
        time.sleep(5)
    get_movie_tweets(movieId, testMovieTitle, cursor, connection)

# testMoviesArray = ['tt54321', 'everything everywhere all at once']
# get_movie_tweets(testMoviesArray, cursor, connection)

cursor.close()
connection.close()

