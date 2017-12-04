states=raw_input("")
x=states.split()

def unique(a):
	b=[]
	for word in a:
		if word not in b:
			b.append(word)
	return b

mylist=x
mylist=unique(mylist)
print mylist

Duplicate_number={i:x.count(i) for i in x}
print Duplicate_number

 