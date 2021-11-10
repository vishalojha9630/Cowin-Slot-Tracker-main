import requests
import time
from os import system
from playsound import playsound
pin = 123456         # Enter Pin Code of your City eg.- 473765
date ="dd-mm-yyyy"   # Enter Date Here eg.- "31-05-2021"
URL = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={date}"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
def check():
    count = 0
    result = requests.get(URL,headers=header)
    rj = result.json()
    data = rj["sessions"]
    for center in data:
        if center["available_capacity"]>0 and center["min_age_limit"] == 18:
            count+=1
            print(center["name"])
            print(center["address"])
            print(center["available_capacity"])
            print(center["vaccine"]+"\n")
    if count != 0:
        playsound('song.mp3')
        return True
    if count == 0:
        print("No Center Available")
        return False
    return True
while (check() != True):
    time.sleep(5)
    system('cls')