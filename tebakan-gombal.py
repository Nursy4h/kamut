GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan


import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik(BB+'                   #tebakan-gombalan-pedas ')
mengetik(GL+'   Malam paling indah ~ ')
mengetik(GG+'    MALAM APA YANG PALING INDAH???? ')
        time.sleep(random.random() * 0.5)
mengetik(RR+' 1')
mengetik(RR+' 2')
mengetik(RR+' 3')
mengetik(GG+'MELAMAR KAMU')
