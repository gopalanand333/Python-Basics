# using json data from web

import urllib.request
import json
def printResults(data):
    theJSON = json.loads(data)
    
    
def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    
    webUrl = urllib.request.urlopen(urlData);
    print(webUrl.getcode())
    if(webUrl.getCode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("error connecting")
    
if __name__ == "__main__":
    main()