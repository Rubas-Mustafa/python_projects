# import url lib
# use urllib.request to get the data from user
# write a function that takes an url
# returns a response

import urllib.request as urllib

def main(url):
    print("Checking Connectivity")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print(response.getcode())

input_url = input("Url of any website: ")
main(input_url)