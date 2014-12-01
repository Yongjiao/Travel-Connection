COMPSCI316
==========

Note from Vivian on version 1.0 on 26th.        
I changed the name of the entire project from microblog to final project

and now flask/bin/python doesn't work

i think the virtualenv might have died or been routed incorrectly because my computer still looks in microblog instead of what i've renamed the project to. you guys will probably have to trouble shoot or create an entirely new project u_u

i will be fixing this problem myself tomorrow. and i'll update

Xiaodan version is 'microblog'
Now it can user OpenID to login. After login it can show and edit the profile of users.
If you want to use this version, please delete the app.db and db_repository part and create your own database to test.

Now we have the following tables: User, AreaOfInteresting, Ratings, Messages. The table named post is only for test. I will delete it at proper time.

Yan has done lots of work of front-end, but I still need time to connect front-end and back-end. If someone who is familiar with HTML, CSS, and Javascript, please do that.

Yan's work is in Travel/doc, the names of pages start with "Travel". 

--2014/12/01--Xiaodan--
How to run the app:
1. using your own flask folder.
2. using db_create.py, db_migrate.py, db_upgrade.py makes your own database.
3. using run.py runs the app.

What app can do now:
1.login with OpenID
2.Rating others without any limitation. (You need type the URL to visit other's profile pages, because we do not have a list of search result to show relative users. You can't rate yourself.)
3.Edit your profile.(When you visit other's profile, the edit link will go away.)
4.Send message to someone from his or her profile pages, and browse the history of messages between you and him or her. Messages are shown in order of time.

What we should do:
1.search part!
2.connect back-end to front-end
3.make limitations for different evironment as many as possible.

What we can't do:
1.concurrency problems...

--Xiaodan-- 
