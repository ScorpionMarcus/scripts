import webbrowser

'''
TODO
'''
url = []
u = open('urls.txt', 'r').readlines()

def removeBreak(read, arr):
    for i in read:
        arr.append(i.rstrip('\n'))

removeBreak(u, url)

for i in url:
	try:
		print(i + " -- retaking screenshot")
		chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
		webbrowser.get(chrome_path).open_new_tab('https://sms.scorpiondesign.com/cms/screenshots/' + 'www.' + i + '.png?retake=true')
	except:
		print(i + " -- RETAKE ERROR")

print("Done!")