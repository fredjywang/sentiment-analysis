# imports
import string


# function to turn tweet into a list
def tweet_list(line):
    # turns the tweet into a list, removes punctuation, and converts it into lowercase
    tweetsList = line.split()
    for i in range(2, len(tweetsList)):
        tweetsList[i] = tweetsList[i].strip(string.punctuation).lower()

    return tweetsList


# function to turn keywords file into a dictionary
def keywords_dict(keywordsFile):
    keyDict = {}

    # creates a dictionary with keywords.txt as key and the sentiment value as value
    try:
        keywords_infile = open(keywordsFile, "r", encoding="utf-8")
        for line in keywords_infile:
            list = line.split(',')
            keyword = list[0]
            value = list[1].strip('\n')
            keyDict[keyword] = value

        return keyDict

    except IOError:
        return []


# function to determine the timezone of a tweet
def determine_timezone(tweetsList):
    # determine latitude and longitude of the tweet
    latitude = tweetsList[0].strip('[]')
    latitude = float(latitude.strip(','))
    longitude = float(tweetsList[1].strip('[]'))

    # determine location of the tweet based on latitude and longitude
    if 49.189787 > latitude > 24.660845:
        if -125.242264 < longitude < -115.236428:
            return 'pacific'
        if -115.236428 < longitude < -101.998892:
            return 'mountain'
        if -101.998892 < longitude < -87.518395:
            return 'central'
        if -87.518395 < longitude < -67.444574:
            return 'eastern'

    # returns false on tweets.txt outside of these four regions
    else:
        return False


# function to compute tweets using previous functions
def compute_tweets(tweetFile, keywordsFile):
    keyDict = keywords_dict(keywordsFile)

    # lists by region
    pList = []
    mList = []
    cList = []
    eList = []

    # checks to see if the keywords function worked or not
    if keyDict != []:
        # categorize each tweet's value by region
        try:
            tweets_infile = open(tweetFile, "r", encoding="utf-8")
            for line in tweets_infile:
                tweetList = tweet_list(line)

                timezone = determine_timezone(tweetList)

                # checks if tweet is in the four regions
                if timezone:
                    keywordCount = 0
                    sentiTotal = 0

                    # iterate through the tweet list and dictionary to check for keywords.txt
                    for i in tweetList:
                        for j in keyDict:
                            if i == j:
                                keywordCount += 1
                                sentiTotal += float(keyDict[j])
                    try:
                        tweetValue = sentiTotal / keywordCount
                    except ZeroDivisionError:
                        tweetValue = 0

                    if timezone == 'pacific':
                        pList.append(tweetValue)
                    elif timezone == 'mountain':
                        mList.append(tweetValue)
                    elif timezone == 'central':
                        cList.append(tweetValue)
                    elif timezone == 'eastern':
                        eList.append(tweetValue)

                else:
                    pass

        # if file doesn't exist
        except IOError:
            return []

        # counting number of keyword tweets in each region
        pKeyTweet = 0
        for i in pList:
            if i > 0:
                pKeyTweet += 1

        mKeyTweet = 0
        for i in mList:
            if i > 0:
                mKeyTweet += 1

        cKeyTweet = 0
        for i in cList:
            if i > 0:
                cKeyTweet += 1

        eKeyTweet = 0
        for i in eList:
            if i > 0:
                eKeyTweet += 1

        # sentiment value of each region and rounded
        try:
            pAverage = sum(pList) / pKeyTweet
            pAverage = float('%.2f' % pAverage)
        except ZeroDivisionError:
            pAverage = 0
        try:
            mAverage = sum(mList) / mKeyTweet
            mAverage = float('%.3f' % mAverage)
        except ZeroDivisionError:
            mAverage = 0
        try:
            cAverage = sum(cList) / cKeyTweet
            cAverage = float('%.3f' % cAverage)
        except ZeroDivisionError:
            cAverage = 0
        try:
            eAverage = sum(eList) / eKeyTweet
            eAverage = float('%.3f' % eAverage)
        except ZeroDivisionError:
            eAverage = 0

        # tuples by region
        pTuple = (pAverage, pKeyTweet, len(pList))
        mTuple = (mAverage, mKeyTweet, len(mList))
        cTuple = (cAverage, cKeyTweet, len(cList))
        eTuple = (eAverage, eKeyTweet, len(eList))

        # list of tuples
        tupleList = [eTuple, cTuple, mTuple, pTuple]

        return tupleList
    # else statement occurs when the keywords function returns [], so compute_tweets returns [] since file did not exist
    else:
        return []