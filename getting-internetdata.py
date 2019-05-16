# lets import data from internet

import urllib.request # have classes to handle urls and http calls

def main():
    webUrl = urllib.request.urlopen("http://www.googe.com")
    print(str(webUrl.read()))  #reads all content from web

if __name__ == '__main__':
    main()
    