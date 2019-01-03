from selenium import webdriver

'''
TODO
pull domains differently
very slow using chromedriver
'''

url = [
'cynthiamendoza.com',
'moorelaw.com',
'kylawpractice.com',
'hessolar.com',
'collinsdentalcare.com',
'dcrashlaw.com',
'coralspringsinjuryfirm.com',
'fortlauderdalepersonalinjuryfirm.com',
'mcguirelawplc.com',
'schwartzandperry.com',
'sachslawyers.com',
'o2law.com',
'brettpritchardlaw.com',
'rieserfamilydental.com',
'tevislawfirm.com',
'taubcriminaldefense.com',
'fischerlawlv.com'
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