from googleapiclient.discovery import build
import json
import pprint
import pdb
from lxml import html
#import requests



my_api_key = "AIzaSyCfXfB3DUeVWwFpFFqIcliJslJ-qfRJtF8"
my_cse_id = "012714669292352524483:jg2mcvgqwfy"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    #pdb.set_trace()
    return res['items']

#results = google_search(
    #'stackoverflow site:en.wikipedia.org'
#    'xanax cures anxiety', my_api_key, my_cse_id, num=2)
#sites=[]
#for i in range(1,len(results)):
#        sites.append(results[i]['formattedUrl'])
        #urls[i]['snippet']=results[i]['snippet']
        
'''all_text=[]
for i in range(1,len(results)/2):
#    pprint.pprint(results[i]['formattedUrl'])
#    pprint.pprint(results[i]['snippet'])

#    req = urllib.request.Request(url[i])
    r = requests.get(urls[i])
    plain_text=r.text
    soup=BeautifulSoup(plain_text)
    all_text.append(soup)
#    resp = urllib.request.urlopen(req)
#    respData = resp.read()
    paragraphs = re.findall(r'<p>(.*?)</p>',str(plain_text))
    for eachP in paragraphs:
        print(eachP)
'''
