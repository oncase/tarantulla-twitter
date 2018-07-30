import json
import csv
import time
import os
import sys
from optparse import OptionParser
from twitterModule import twitter_integration as integration
import datetime



if __name__ =="__main__":
    
    baseDir = os.path.dirname(os.path.abspath(__file__)) + '/'

    '''Load API keys'''
    with open(baseDir + '../api-keys.json') as f:
        keys = json.load(f)

    '''Load config-timeline.json'''
    with open(baseDir + '../config-timeline.json') as fileName:
        confs = json.load(fileName)

    '''Set vars'''
    outputFolder = baseDir+confs['temp_output']
    publishers = confs['publishers']
    currDate = time.strftime("%d-%m-%Y")
    start = datetime.datetime.now()

    '''Send request for each publisher'''
    for publisher in publishers:
        
        pubStart = datetime.datetime.now()
        
        currPub = publisher['_twitter_screen']
        pubName = publisher['name']

        outputFile=outputFolder+currPub+currDate+'-tl.json'

        integration(outfile=outputFile, publisher=publisher["_twitter_screen"], keys=keys)
        
        pubEnd = datetime.datetime.now()

        print("Process Finished for "+ pubName + " in " +str(pubEnd-pubStart))
        print('\n')

    end = datetime.datetime.now()
    print("Total elapsed time: "+str(end-start))
