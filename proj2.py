#proj2.py
from bs4 import BeautifulSoup
import requests


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

cntr=0
for story_heading in soup.find_all(class_="story-heading"): 
	if(cntr<10):
	    if story_heading.a: 
	        print(story_heading.a.text.replace("\n", " ").strip())
	    else: 
	        print(story_heading.contents[0].strip())
	    cntr+=1



#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here

base_url = 'http://www.michigandaily.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for mostread in soup.find_all(class_="panel-pane pane-mostread"): 
	#print(mostread)
	for lists in mostread.ol.contents:
		if (lists.string.strip()!=""):
			print(lists.string.strip())



#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

imgs =soup.find_all('img') 
for item in imgs:
	if (item.get('alt')):
		print (item.get('alt'))
	else:
		print('No alternative text provided!')



#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here


base_url = 'https://www.si.umich.edu'
base_page='/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
r = requests.get(base_url+base_page)
soup = BeautifulSoup(r.text, "html.parser")

redirect=""

links=[]
while(1):
	try:
		if(redirect==""):
			req = requests.get(base_url+base_page)
			links.append(base_page)
			soups = BeautifulSoup(req.text, "html.parser")
			value=soups.find_all("a", { "title" : "Go to next page" })
			redirect=value[0].get('href')
			links.append(redirect)


		else:
			new_base=redirect
			nreq = requests.get(base_url+new_base)
			soups = BeautifulSoup(nreq.text, "html.parser")
			value=soups.find_all("a", { "title" : "Go to next page" })
			redirect=value[0].get('href')
			links.append(redirect)
	except:
		break
#print(redirect)
#print(links)
#now u got a list of links that leads to the next page
email_links=[]
for pages in links:
	page_base = pages
	newreq = requests.get(base_url+page_base)
	soupiee = BeautifulSoup(newreq.text, "html.parser")
	email_context=soupiee.find_all("div", { "class" : "field-name-contact-details" })
	for context in email_context:
		email_links.append(context.find_all('a')[0].get('href'))

for email_item in email_links:
	email_base=email_item
	finalreq=requests.get(base_url+email_base)
	soupss = BeautifulSoup(finalreq.text, "html.parser")
	email=soupss.find_all("div", {"class" : "field-name-field-person-email"})
	for em in email:
		print(em.find_all('a')[0].text)


