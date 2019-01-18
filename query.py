import dns.resolver
import os
import whois
import random
from pathlib import Path
import requests
import sys

'''
TODO
'''

url = sys.argv[1].replace('https', '').replace('http', '').replace('/', '').replace(':', '').replace('www.', '').strip()
myResolver = dns.resolver.Resolver()
user = str(Path.home())
arr = []

print('\nQuerying ' + url + '...')

def ping(record_type):
    try:
        if record_type == 'CNAME':
            record = myResolver.query('www.' + url, record_type)
        else:
            record = myResolver.query(url, record_type)
        arr.append(record)
    except:
        print('No ' + record_type + ' records found')

for i in ['A', 'CNAME', 'NS', 'MX', 'TXT']:
    ping(i)

try:
    save_path = user + '/Desktop/' + url
    os.makedirs(save_path)
except FileExistsError:
    save_path = user + '/Desktop/' + url + str(random.randint(1,101))
    os.makedirs(save_path)

readme = open(save_path + '/' + 'README.txt', 'a')

try:
    status = requests.get('http://www.' + url + '/_status')
    if status.status_code == 200:
        readme.write(status.text + '\n\n')
    else:
        pass
except:
    pass

for rdata in arr:
    for i in rdata:
        readme.write(str(i) + '\n\n')
        print(str(i))

try:
    info = whois.whois(url).text
    readme.write(info)
except:
    print('Unable to retrieve WHOIS')

print('README saved to ' + save_path)