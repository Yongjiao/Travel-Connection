from app import db,models

user=models.User.query.get(1)

messages = user.get_guser_messages().all()
print user.nickname
# templists for storing user 
lists = []
for message in messages:
    tempusers = message.get_guserconncector().all()
    for tempuser in tempusers:
        lists.append(tempuser.nickname)
print lists
n = len(lists) - 1
print n
m = len(lists) - 2
m1 = m
print m
while n>=0:
	print lists
	print 'n=', n
	if lists[n] == user.nickname:
		print 'here!'
		lists.pop(n)
	n = n - 1
print lists
lists = list(set(lists))
print lists, 'firstone',lists[0]
# n = len(lists) - 1
# m = len(lists) - 2
# i = 1
# while n>=0:
# 	if lists[n] != 0:    
# 	    while m >= 0:
# 	        if lists[n]==lists[m]:
# 	                lists[m] = 0
# 	        m = m - 1
# 	        print 'm=',m
# 	        i = i + 1
# 	m = len(lists) - 2 - i 
# 	n = n - 1
# 	print 'n=',n 
# print lists