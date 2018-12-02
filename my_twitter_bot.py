import tweepy
import time

print("this is my twitter bot", flush=True)

CONSUMER_KEY = 'SJhSxN1p82LtH2w3ThQlzSl4G'
CONSUMER_SECRET = '3knJH2kpJMf3k2ysLnrO9W4IiMuYCQTRoe2g9otbEunFujqTC8'
ACCESS_KEY = '1061864381011714048-t3sxP4myFPQUo4vj5BCDRtJPc1nrNB'
ACCESS_SECRET = 'OYGkuWM8zn3wOhNvqLBZmOgd7kKzBc78jbCfYUjSRSxz8'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
FILE_NAME = 'last_seen_id.txt'

#opens file for reading reading last_seen_id
def retrive_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

#opens file for writing last_seen_id
def store_last_seen_id(last_seen_id ,file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def reply_to_tweets():
	print('retriving and replying to tweets..', flush=True)
	#LASTSEEN ID FOR TESTING :1062674986568179713
	last_seen_id = retrive_last_seen_id(FILE_NAME)
	mentions = api.mentions_timeline(last_seen_id)

	for mention in reversed(mentions):
		print(str(mention.id) +'-'+ mention.text)
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		if '#helloworld' in mention.text.lower():
			print("found #helloworld!", flush=True)
			print('responding back..', flush=True)
			api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you! ', mention.id)



while True:
    reply_to_tweets()
    time.sleep(5)