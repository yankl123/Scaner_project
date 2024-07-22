from py532lib.mifare import *
from py532lib.frame import *
from py532lib.constants import *

# Initialize the I2C connection
pn532 = Mifare()
pn532.SAMconfigure()

# Scan for a tag
uid = pn532.read_mifare().get_data()
if not uid:
    raise RuntimeError("No Mifare card currently activated.")
print("Card detected with UID:", uid.hex())


# Define the block number and the data to write
block_number = 4  # Block number to write to
data_to_write = bytearray(b'\x01\x02\x03\x04')  # 16 bytes of data

# Authenticate with the card
key_a = bytearray([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])  # Default key A

succses = False 
while not succses :
    try :
        succses = pn532.mifare_auth_a(block_number, MIFARE_FACTORY_KEY)
    except :
        break

# Write data to the block
if not pn532.mifare_write_ultralight(block_number, data_to_write):
    raise RuntimeError("Failed to write data to the block.")
print("Data written successfully to block", block_number)
