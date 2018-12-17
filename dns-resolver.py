import dns.resolver
import os

url = 'vadefensecounsel.com'
myResolver = dns.resolver.Resolver()

a = myResolver.query(url, 'A')
ns = myResolver.query(url, 'NS')
mx = myResolver.query(url, 'MX')
txt = myResolver.query(url, 'TXT')
cname = myResolver.query('www.' + url, 'CNAME')
arr = a, cname, ns, mx, txt

save_path = 'C:/users/marcus.legault/scripts/DNS-backups/' + url
os.makedirs(save_path)
readme = open(save_path + '/' + 'README.txt', 'a')

for rdata in arr:
    for i in rdata:
        readme.write(str(i) + '\n\n')

print('README saved to ' + save_path)