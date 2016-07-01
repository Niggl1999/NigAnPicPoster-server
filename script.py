#!/usr/bin/env python

import sys,os
from twython import Twython
import datetime
from pushbullet import Pushbullet

pb = Pushbullet("xxxxxxxxxxxxxxxxxx") #Insert your pushbullet api-key here
i = datetime.datetime.now()
now = datetime.datetime.now()
my_channel = pb.channels[1] #Insert the number of the pushbullet-channel you want the bot to report to

#Get current day of the week
def datetoday(day, month, year):
    d = day
    m = month
    y = year
    if m < 3:
        z = y-1
    else:
        z = y
    dayofweek = ( 23*m//9 + d + 4 + y + z//4 - z//100 + z//400 )
    if m >= 3:
        dayofweek -= 2
    dayofweek = dayofweek%7
    return dayofweek

months = [ 'january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december' ]

days =[ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
       'Sunday' ]


d = now.day
m = now.month
y = now.year


dayofweek = days[datetoday(d, m, y)-1]
#Get text for Tweet
tweetStr = "This is a random bullsh*t tweet. because I am testing out a twitter bot!"
file="/xx/xxx/xx" +now.strftime("%d.%m.%Y") +".txt" #Insert folder, where the files are
f=open(file,'rU').readlines()
print type(f)
buffer=''
if f:
    for line in f:
       buffer += line
tweet_text = dayofweek + ": " + buffer

#initialise twitter api
    # your twitter consumer and access information goes here
apiKey = 'xxxxxxxxxxxx'
accessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
accessTokenSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
apiSecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
#Get picture
photo_name = now.strftime("%d.%m.%Y") +".jpg"
photo_path = '/xx/xxx/xx' + photo_name #Insert folder, where the files are
photo = open(photo_path, 'rb')
#check if day IS NOT Sunday and if the tweet is max 140 chars long
if (dayofweek != "Sunday") and len(tweet_text) <= 140:
 print "Day: " +dayofweek   #Report to Terminal: Day
 print "Date " +now.strftime("%d.%m.%Y")    #Report to Terminal: Date
 print "Text: " +tweet_text     #Report to Terminal: Tweet-Text
 print "Photo name: " +photo_name       #Report to Terminal: Picture-Name
 print "Text file location: " +files    #Report to Terminal: Textfile-Name
 api.update_status_with_media(status=tweet_text, media=photo)       #Finally post the tweet
 my_channel.push_note("Twitter_Bot","Sucsessfully posted: %s" %tweet_text)      #Report to pushbullet
else:
 #ERROR Report to Terminal
 print "tweet not sent. Too long. 140 chars Max."   
 print "It is Sunday"
 print "Date: " +now.strftime("%d.%m.%Y")
 print "Text: " +tweet_text
 print "Photo name: " +photo_name
 print "Text file location: " +file
 #ERROR Report to pushbullet
 my_channel.push_note("Twitter_Bot - Huston we have a problem","Not sucsessfully posted: %s " %tweet_text)

