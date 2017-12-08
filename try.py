import collections
states = raw_input("Enter a sentance:")
x = states.split()

def unique(a):
	b=[]
	for word in a:
		if word not in b:
			b.append(word)
	return b

mylist = x
mylist = unique(mylist)
print mylist
str=''.join(mylist)
print str
cont = {i:str.count(i)for i in str}
print cont



#count_words={i:mylist.count(i) for i in mylist}
#Duplicate_number={i:x.count(i) for i in x}
#print Duplicate_number
#print count_words

 