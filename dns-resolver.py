import dns.resolver
import os
import whois

'''
TODO
'''

print('Enter domain: ')
url = input().replace('https', '').replace('http', '').replace('/', '').replace(':', '').replace('www.', '').strip()
myResolver = dns.resolver.Resolver()
user = os.environ['USERPROFILE']

a = myResolver.query(url, 'A')
ns = myResolver.query(url, 'NS')
mx = myResolver.query(url, 'MX')
txt = myResolver.query(url, 'TXT')
cname = myResolver.query('www.' + url, 'CNAME')
whois = whois.whois(url).text
arr = a, cname, ns, mx, txt

try:
    save_path = user + '/Desktop/' + url
    os.makedirs(save_path)

except FileExistsError:
    save_path = user + '/Desktop/' + url + str(random.randint(1,101))
    os.makedirs(save_path)
readme = open(save_path + '/' + 'README.txt', 'a')

for rdata in arr:
    for i in rdata:
        readme.write(str(i) + '\n\n')
readme.write(whois)

print('README saved to ' + save_path)