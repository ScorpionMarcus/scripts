import webbrowser

'''
TODO
url needs to reference something else
'''

url = [
'adelolalaw.com',
'penningplumbing.com',
'henrylawfirm.com',
'thomastears.com',
'henderson-law.com',
'mycleanteam.com',
'cflegal.net',
'stegplumbing.com',
'nevadalegalcounsel.com',
'divorcelawyersuffolkcounty.com',
'uselderlaw.com',
'sylvesterlawfirm.com',
'moralawonline.com'
]

for i in url:
	try:
		print(i + " -- retaking screenshot")
		chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
		webbrowser.get(chrome_path).open_new_tab('https://sms.scorpiondesign.com/cms/screenshots/' + 'www.' + i + '.png?retake=true')
	except:
		print(i + " -- RETAKE ERROR")

print("Done!")