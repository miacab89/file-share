import xml.etree.ElementTree as ET
import json
from pkgutil import get_data
import requests
import json
import xmltodict
import utils

# Sample URL to fetch the html page
url = "https://fileshar.es/Ax58Dsm"
  
# Get the page through get() method
html_response = requests.get(url, 
    headers= {'headers': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
  
# Save the page content as sample.html
with open("share.html", "w") as html_file:
    html_file.write(html_response.text)

# Save data as xml file
with open("share.html", "r") as html_file:
    html_xml = ET.parse(html_file, filename="share.html")
    html_string = ET.tostring(html_xml)
    json_dict = dict(xmltodict.parse(html_string))
        
with open("data.json", "w") as file:
   json_data = json.dumps(json_dict)

with open("data.json", "w") as json_file:
    json_file.write(json_data)

print(json_data)

# def json_fetch():
#     res = requests.get('https://fileshar.es/Ax58Dsm')
    

#     with open(file = res) as j:
#         contents = json.dumps(j)

#     if res.status_code != 204:
#         return contents
#     else:
#         return error;

# json_fetch()

