import subprocess
import re

def stage_2():
	output = subprocess.check_output("netsh wlan show profiles", shell=True).decode('utf-8')
	wifis = re.findall(': (.*)\r', output)
	filename = "stage2.txt"
	myfile = open(filename, 'w')

	for profile in wifis:
		output2 = subprocess.check_output("netsh wlan show profile name=\"" + profile + "\" key= clear", shell=True).decode('utf-8', 'ignore')
		clave_encontrada = re.search('Contenido de la clave  : (.*)\r',output2)
		if clave_encontrada is not None:
			myfile.write("{: <50}".format(profile))
			clave = clave_encontrada.group(1)
			myfile.write("{: <50}".format(clave)+"\n")
	myfile.close()
