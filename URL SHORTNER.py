import pyshorteners

url = input("Enter the URL to shorten: ")

#TinyURL shortener service
short = pyshorteners.Shortener()
Short_URL = short.tinyurl.short(url)

print('\n'"The Shortened URL is: " + Short_URL)


