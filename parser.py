from bs4 import BeautifulSoup
import urllib2
from unidecode import unidecode
site= 'http://seekingalpha.com/article/4051237-r1-rcms-achi-ceo-joe-flanagan-q4-2016-results-earnings-call-transcript?part=single'
hdr={'User-Agent':'Mozilla/5.0'}
req=urllib2.Request(site, headers=hdr)
page=urllib2.urlopen(req)
soup = BeautifulSoup(page)

#print soup.prettify()


#----------Function to find the indices of each person's in the array
def find(lst, a):
    return [i for i, x in enumerate(lst) if x==a]


answer=soup.find_all(class_="answer")
count=0
answer_author=[]
answers_source=[]
answers_content=[]

for eachobject in answer:
	answer_author.append(eachobject.get_text())
	answers_source.append(eachobject.parent.parent)

for eachobject in answers_source:
	answers_content.append(eachobject.find_next_sibling().get_text())

answers_content_decoded=[]
z=0
for eachobject in answers_content:
	answers_content_decoded.append(unidecode(answers_content[z]))
	z+=1
#print len(answers_content_decoded)
#print answers_content_decoded
x=int(raw_input("Enter the no of unique people:"))
unique_names=[]
for i in range(0,x):
	unique_names.append(str(raw_input("Enter the names now: ")))

print unique_names

for each_name in unique_names:
	file=open(each_name+".txt","w")
	indices=find(answer_author,each_name)
	file.write(answer_author)
	file.write("\n")
	for each_i in indices:
		file.write(answers_content_decoded[each_i])
		file.write("\n")
		file.write("\n")
	file.close()