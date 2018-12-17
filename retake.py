from selenium import webdriver

url = [
'adamstonelawfirm.com',
'johnsonkraeuter.com',
'natural-lookingresults.com',
'haroldcampbell.com',
'deloachelawoffice.com',
'zenlawfirm.com',
'mdaccidentlaw.com',
'1876law.com',
'hesslawoffice.com',
'hchlawyers.com',
'caseysimmonsandbryant.com',
'huttonlaw.com',
'orangecountylitigationfirm.com'
]

for i in url:
	try:
		print(i + " -- retaking screenshot")
		chromedriver = 'C:/Users/marcus.legault/scripts/chromedriver.exe'
		driver = webdriver.Chrome(chromedriver)
		driver.get('https://sms.scorpiondesign.com/cms/screenshots/' + 'www.' + i + '.png?retake=true')
		print(i + " -- screenshot retaken successfully\n")

	except:
		print(i + " -- RETAKE ERROR")

print("Done!")