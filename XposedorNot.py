# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# import the library module
import hashlib
import urllib.request
import io
import json
import requests
#import sha3
from Crypto.Hash import keccak #pip install pycryptodom
   
def logo():
	logo = '''
 __   __                         _  ____       _   _       _   
 \ \ / /                        | |/ __ \     | \ | |     | |  
  \ V / _ __   ___  ___  ___  __| | |  | |_ __|  \| | ___ | |_ 
   > < | '_ \ / _ \/ __|/ _ \/ _` | |  | | '__| . ` |/ _ \| __|
  / . \| |_) | (_) \__ \  __/ (_| | |__| | |  | |\  | (_) | |_ 
 /_/ \_\ .__/ \___/|___/\___|\__,_|\____/|_|  |_| \_|\___/ \__|
       | |                                                     
       |_|    Twitter: @ManiarViral                                        
    	      Description: This tool is to search an aggregated repository of xposed passwords comprising of ~850 million real time passwords. Usage of such 		compromised passwords is detrimental to individual account security. 
								  
 '''
	return logo
	
def note():
	note = '''

The following explains a bit more about the response/output characteristics in simple terms :

Digits (D): Count of numbers
Alphabets (A): Count of alphabets
Special chars(S): Count of special chars
Length(L): Length of the password
Count: shows the number of times, this password was observed in the collected xposed data breaches
'''
	return note

def checkInternetConnection():
		try:
			urllib.request.urlopen('https://google.com/')
		except:
			print('[!] No internet connection...Please connect to the Internet')
		else:
			print('[+] Checking Internet connection...')
			
def cmd_passwordSearch():

	# initialize a string
	password = input("\n Enter your password:");

	# encode the string
	encoded_str = password.encode()
	
	# Generating Keccak hash
	keccak_hash = keccak.new(digest_bits=512)
	
	# create sha3 hash objects initialized with the encoded string
	obj_sha3_224 = hashlib.sha3_224(encoded_str)   # SHA3-224
	obj_sha3_256 = hashlib.sha3_256(encoded_str)   # SHA3-256
	obj_sha3_384 = hashlib.sha3_384(encoded_str)   # SHA3-384
	obj_sha3_512 = hashlib.sha3_512(encoded_str)   # SHA3-512
	obj_sha3_5121 = keccak_hash.update(encoded_str)# SHA3-Keccak-512
      
	# print in hexadecimal
	print("\nSHA3-224 Hash: ", obj_sha3_224.hexdigest())
	print("\nSHA3-256 Hash: ", obj_sha3_256.hexdigest())
	print("\nSHA3-384 Hash: ", obj_sha3_384.hexdigest())
	print("\nSHA3-512 Hash: ", obj_sha3_512.hexdigest())
	print ("\nSHA3-keccak-512 Hash: ", keccak_hash.hexdigest())
	sha3k512 = keccak_hash.hexdigest()

	sub_pass = sha3k512[0:10]

	#print("First 10 characters from the password:", sub_pass)
	
	response = requests.get("https://passwords.xposedornot.com/api/v1/pass/anon/"+sub_pass)
	json_data = json.loads(response.text)
	print("\nOutput:", json_data)
	
def main():

	print(logo())
	
	checkInternetConnection()
	
	cmd_passwordSearch()
	
	print(note())
	
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? (y/n) \n> ')).lower()
			if choice[0] == 'y':
				cmd_passwordSearch()
				continue
			if choice[0] == 'n':
				exit(0)
				break
		except ValueError:
			sys.exit(0)
	

if __name__ == "__main__":
	main()