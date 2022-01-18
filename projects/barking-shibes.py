# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

# how to call api?
#dogged quote and image needed
#write html string to a html file to look into browser

#pip install requests

import requests
import os
# from requests.sessions import _Data

quote_url = "http://quotes.stormconsultancy.co.uk/random.json"

request = requests.get(quote_url)
#deserialize_request=json.loads(request)
quote_data=request.json()
quote= quote_data['quote']
print(quote)


pic_url="http://shibe.online/api/shibes"
request_pic=requests.get(pic_url)
pic_data=request_pic.json()

pic=pic_data[0]

cwd=os.getcwd()
# path="Documents\codingnomads\python-201-main_jsiu\python-201-main\projects"
print(cwd)

f = open(os.path.join(cwd,'barking.html'),'w', encoding="utf-8")

message = f"""<html>
<head></head>
<body><p>
{quote}
<img src="{pic}">
</p></body>
</html>"""

f.write(message)
f.close()


#the first word is much, many, so , such, very
#much many for quantity
#so, very, such before adjective
# select a word?
#take out articles
# take out anything except for nouns and adjectives
# there are uncountable nouns

#create HTML structure
#write to the file

#print(request.status_code) # should be seeing 200 or something is wrong

