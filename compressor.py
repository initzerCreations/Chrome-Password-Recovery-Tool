import zipfile
import os

def compress_all():
	jungle_zip = zipfile.ZipFile('all.zip', 'w')
	jungle_zip.write('stage1.txt', compress_type=zipfile.ZIP_DEFLATED)
	jungle_zip.write('stage2.txt', compress_type=zipfile.ZIP_DEFLATED)
	jungle_zip.write('stage3.txt', compress_type=zipfile.ZIP_DEFLATED)
	os.remove("stage1.txt")
	os.remove("stage2.txt")
	os.remove("stage3.txt")
	jungle_zip.close()