#todo: tidy up this script


import tweepy
import wget
import pathlib
from make import makepic

#import api keys
import config

auth = tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
auth.set_access_token(config.access_token,config.access_secret)

api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

        status_list = status.text.split(' ')
        
        keyword = status_list[1]
        if len(status_list)>2 and len(status_list[2])==7 and status_list[2][0]=='#':
            colour = status_list[2]
        else:
            colour = '#0000ff'

        if len(keyword)>6:
            longword=True
        else:
            longword=False

        makepic(keyword,colour,longword)
        
        # Upload image
        media = api.media_upload("outfile_"+keyword+".png")
 
        # Post tweet with image
        tweet = "#"+keyword
        post_result = api.update_status(status=tweet, media_ids=[media.media_id], in_reply_to_status_id=status.id)



     

myStreamListener = MyStreamListener
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())

myStream.filter(track=['@ComicBoomBot'], async=True)
