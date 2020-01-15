# imports
from sentiment_analysis import compute_tweets

# asking for user input
tweets = input("Please enter the file name for the tweets: ")
keywords = input("Please enter the file name for the keywords: ")

# setting variable and using compute_tweets function
tupleList = compute_tweets(tweets, keywords)

# checks to see if the output was a [], if so that means the keywords file did not exist
if tupleList != []:
    # formatting output
    print("\nEASTERN:\nAverage happiness score:", tupleList[0][0], "\nTotal number of keyword tweets:",
          tupleList[0][1], "\nTotal number of tweets is:", tupleList[0][2])
    print("\nCENTRAL:\nAverage happiness score:", tupleList[1][0], "\nTotal number of keyword tweets:",
          tupleList[1][1], "\nTotal number of tweets is:", tupleList[1][2])
    print("\nMOUNTAIN:\nAverage happiness score:", tupleList[2][0], "\nTotal number of keyword tweets:",
          tupleList[2][1], "\nTotal number of tweets is:", tupleList[2][2])
    print("\nPACIFIC:\nAverage happiness score:", tupleList[3][0], "\nTotal number of keyword tweets:",
          tupleList[3][1], "\nTotal number of tweets is:", tupleList[3][2])
else:
    print(tupleList)
