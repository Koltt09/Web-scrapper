import requests
import time
from bs4 import BeautifulSoup

def Get_headers(url):
    try:
        #Make a GET request to the webpage
        Response = requests.get(url)
        Response.raise_for_status()  #Give an exception if there is HTTP errors

        #Parse the HTML of the webpage
        Soup = BeautifulSoup(Response.text, 'html.parser')

        #Find the elements that contain the headers
        Headers = Soup.find_all('h2')  #example 'h2' for the headers

        #Print the found headers
        if Headers:
            print(f"\nHEADERS OF: {url}\n")
            for i, Header in enumerate(Headers, start=1):
                print(f"{i}. {Header.get_text(strip=True)}")
            print("")
        else:
            print("\nHeaders not found on the webpage. Check the HTML structure\n")
    except requests.exceptions.MissingSchema:
        print("\nPlease, input a valid URL (Example: https://en.wikipedia.org/wiki/Nissan_GT-R)\n")
    except requests.exceptions.RequestException as e:
        print(f"\nError at obtaining webpage data: {e}\n")

#User Input
while True:
    print("Input the URL of the webpage you want to scrap (Including HTTP/HTTPS)")
    User_URL = input("Type 'Exit' to leave the program: ")

    if User_URL.lower() == "exit":
        break
    
    Get_headers(User_URL)
    print("Refreshing...")
    time.sleep(2)
