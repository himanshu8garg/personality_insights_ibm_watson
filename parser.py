from bs4 import BeautifulSoup
import urllib2
from unidecode import unidecode
site= str(raw_input("Enter the website now: "))
hdr={'User-Agent':'Mozilla/5.0'}
req=urllib2.Request(site, headers=hdr)
page=urllib2.urlopen(req)
soup = BeautifulSoup(page)


#----------Function to find the indices of each person's in the array
def find(lst, a):
    return [i for i, x in enumerate(lst) if x==a]

def new_parser():
	answer=soup.find_all(class_="answer")
	count=0
	#print answer
	answer_author=[]
	answers_source=[]
	answers_content=[]

	for eachobject in answer:
		answer_author.append(eachobject.get_text())
		answers_source.append(eachobject.parent.parent)
		# print eachobject.get_text()
		# print "\n"
		# print "\n"
		# print eachobject.parent.parent
		# print "\n"
		# print "\n"
	print answers_source
	for eachobject in answers_source:
		#answers_content.append(eachobject.find_next_sibling().get_text())
	 	#print eachobject.find_next_sibling().find_next_sibling()
	 	answers_text=""
	 	y_object=eachobject.find_next_sibling()
	 	answers_text+=eachobject.find_next_sibling().get_text()
	 	while(y_object.find_next_sibling().find("strong")==None):
	 		answers_text+=y_object.find_next_sibling().get_text()
	 		y_object=y_object.find_next_sibling()
	 		
	 	answers_content.append(answers_text);
	 	# print "\n"
	 	# print "\n"

	answers_content_decoded=[]
	z=0
	for eachobject in answers_content:
		answers_content_decoded.append(unidecode(answers_content[z]))
		z+=1
	#print len(answers_content_decoded)
	# print answers_content_decoded
	print answer_author
	# print len(answers_content_decoded)
	# print len(answer_author)
	x=int(raw_input("Enter the no of unique people:"))
	y=int(raw_input("Enter the year:"))
	z=str(raw_input("Enter the ticker:"))
	unique_names=[]
	unique_position=[]
	for i in range(0,x):
		unique_names.append(str(raw_input("Enter the names now: ")))
		unique_position.append(str(raw_input("Enter the position of that person: ")))

	print unique_names
	p=0
	for each_name in unique_names:
		file=open(z+"_"+str(y)+"_"+unique_position[p]+"_"+each_name+".txt","w")
		p+=1
		indices=find(answer_author,each_name)
		print indices
		file.write("\n")
		for each_i in indices:
			file.write(answers_content_decoded[each_i])
			file.write("\n")
			file.write("\n")
		file.close()
		print "File Successfully Written :)"

def old_parser():
	answer=soup.find_all("strong")

	count=0
	print str(answer)


	answer_author=[]
	answers_source=[]
	

	for eachobject in answer:
		
		answer_author.append(eachobject.get_text())
		answers_source.append(eachobject.parent)

	# print "\n"
	# print answers_source
	# print answer_author
	# print len(answers_source)
	# print len(answer_author)


	#-----------------Garbage removal----------------------------------
	answers_content_garbage=[]
	for eachObject in answers_source:
		answers_content_garbage.append(unidecode(eachObject.get_text()))
	# print len(answers_content_garbage)
	# print answers_content_garbage
	indices_garbage=find(answers_content_garbage, "Question-and-Answer Session")
	# print indices_garbage
	del answers_source[0:indices_garbage[0]]
	del answer_author[0:indices_garbage[0]]
	#-----------------Garbage removal----------------------------------


	# print answers_source
	print answer_author
	# print len(answers_source)
	# print len(answer_author)

	x=int(raw_input("Enter the no of unique people:"))
	y=int(raw_input("Enter the year:"))
	z=str(raw_input("Enter the ticker:"))
	unique_names=[]
	unique_position=[]
	for i in range(0,x):
		unique_names.append(str(raw_input("Enter the names now: ")))
		unique_position.append(str(raw_input("Enter the position of that person: ")))

	print unique_names
	p=0
	for each_name in unique_names:
		answers_content=[]
		file=open(z+"_"+str(y)+"_"+unique_position[p]+"_"+each_name+".txt","w")
		p+=1
		indices=find(answer_author,each_name)
		print indices
		file.write("\n")
		answers_source_updated=[]
		for each_i in indices:
			answers_source_updated.append(answers_source[each_i])
		#print answers_source_updated
		for eachobject in answers_source_updated:
	 		answers_text=""
	 		y_object=eachobject.find_next_sibling()
	 		answers_text+=eachobject.find_next_sibling().get_text()
	 		# print answers_text
	 		while(y_object.find_next_sibling().find("strong")==None):
	 			answers_text+=y_object.find_next_sibling().get_text()
	 			y_object=y_object.find_next_sibling()
	  		answers_content.append(unidecode(answers_text));
	 	for eachobject in answers_content:
	 		file.write(eachobject)
	 		file.write("\n")
	 		file.write("\n")
	 	file.close()
	 	print "File Successfully Written :)"



if (soup.find_all(class_="answer")==[]):
	print "Using Old Parser"
	old_parser()
else:
	print "Using New Parser"
	new_parser()