import sys
sys.path.append('/home/kamateck/Desktop/scan_project/PYnfc/')
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

pn532 = Pn532_i2c()
pn532.SAMconfigure()

def scanNfc() : 
    card_data = pn532.read_mifare().get_data()
    card_data = card_data.hex()
    return (card_data)
