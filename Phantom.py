import sys
import os.path
import requests
import json


class main:
    def scrap(url):
        r = requests.get(url)
        results = r.json()
        output = json.dumps(results, indent=2, sort_keys=True)
        return output

    def save(ip, out):
        dir = 'Outputs/' + ip + ".json"
        f = open(dir, "w+")
        with open(dir, 'w') as f:
            f.write(out + "\n")


x = len(sys.argv)
if x == 2:
    ip = sys.argv[1]
    url = "http://ip-api.com/json/" + ip + "?fields=status,message,country,region,regionName,city,zip,isp,org,as,proxy,query"

    out = main.scrap(url)
    print(out)

if x == 1:
    print("Press Ctrl+C to stop this file")
    while True:
        ip = input('\nIp: ')
        url = "http://ip-api.com/json/" + ip + "?fields=status,message,country,region,regionName,city,zip,isp,org,as,proxy,query"

        out = main.scrap(url)
        print(out + "\n")

        saveFile = input("Would you like to save this file? ('y' or 'n'): ")

        if saveFile == 'y':

            dir = 'Outputs/' + ip + ".json"
            file_exists = os.path.exists(dir)
            if file_exists == True:
                print("This files already exists!")

            if file_exists == False:
                main.save(ip, out)
                print("This file has been saved")

        if saveFile == 'n':
            pass