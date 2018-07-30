import tweepy
import json
import csv
import time
import os

'''
    Twitter Modules

'''

def twitter_oauth (access_token, access_token_secret, consumer_key, consumer_secret):
    '''
        Twitter OAuthHandler function
        Function: Handle twitter authentication
    '''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    timeline_api = tweepy.API(auth)

    return timeline_api



def cleanFile(file, remove=False):
    '''
        Twitter Remove File
    '''
    
    if os.path.exists(file) and remove:
        os.remove(file)
        return 'File removed' + file
    else:
        return os.path.exists(file)



def output(data, file_name):
    '''
        Twitter Output Write Function
    '''
    with open (file_name, 'a', encoding='utf-8') as file:
        file.write(str(data))
        file.write("\n") 
   


def twitter_integration(outfile, publisher, keys):
    '''
        Twitter Integration Process - Publisher Full Load
    '''
    
    apiAuth = twitter_oauth(keys["ACSSTK"], keys["ACSSTKSCRT"], keys["CONSMKEY"], keys["CONSMKEYSCRT"])

    done = False
    while not done:        
        try:
            print("Tarantulla Twitter - Starting... - Publisher: " + publisher)
            print("Process Started at: "+ time.strftime("%d/%m/%Y %H:%M:%S"))
            
            page = 1
            total_tts=0
            ntweets=0
            for status in tweepy.Cursor(apiAuth.user_timeline, screen_name=publisher).pages():
                print("Collecting " + publisher + " : " + str(ntweets) + " tweets collected", end='\r')
                total_tts+=len(status)
                for i in range (0, len(status)):
                    output(status[i]._json,outfile)
                page+=1
                ntweets+=len(status)
            print("Process Finished at: "+ time.strftime("%d/%m/%Y %H:%M:%S") + " - Total of tweets collected = "+str(total_tts))
            done=True

        except tweepy.TweepError as e:
            print ("API Error - " + str(e))
            done = False
            i = 0
            while i <=5:
                time.sleep (60)
                i+=1
                print(str(i)+" minuto(s)")

            cleanFile(outfile, True)
            continue