import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')



import requests

bit = platform.architecture()[0]

if bit == "32bit":

        from Jahidul import R

        R()



elif bit == "32bit":

        print("   your device is 32 bit ")

        print("   32 bit will update soon")

        exit()
