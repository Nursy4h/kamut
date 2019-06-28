import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.1)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
mengetik('Cintamu bagaikan TeamViewer yang selalu mengendalikan hatiku')
mengetik('berharap setelah aku berhasil login di hati kamu ga akan ada tombol logout, dan sessionku ga bakal pernah expired')
