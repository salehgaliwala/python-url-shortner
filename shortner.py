import pyshorteners

s = pyshorteners.Shortener(api_key="YOUR_KEY")

long_url = input("Enter the URL to shorten: ")

short_url = s.bitly.short(long_url)

print("The shortened URL is: " + short_url)
