import requests
import re
import sys
import bs4

res = requests.get("https://www.facebook.com/pg/leahwiselawfirm/videos")
soup = bs4.BeautifulSoup(res.text, 'lxml')
for link in soup.find_all('a', href=True):
    print(link['href'])


'''
url = sys.argv[-1]
html = r.get(url)
video_url = re.search('hd_src:"(.+?)"', html.text).group(1)
print(video_url)
'''