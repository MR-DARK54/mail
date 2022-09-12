import random,string,os,sys,time

os.system('clear')
print ('\033[1;34mplease wait............')
time.sleep(2)
g = '''
\033[1;35m
 #by : M R - D A R K 

 #tm : t.me/name_dark

 #fr : egypt /2022

'''
print (g)

time.sleep(5)

print ('\033[1;36m')

f = open('list.txt' , 'r' ) .readlines()

dark = 0
while (dark < len (f)) :
    for i in f :
          print (i.strip() +str(random.randint(1000,99999)) + '@gmail.com' ) 
          print (i.strip() +str(random.randint(1000,99999)) + '@yahoo.com' )
          print (i.strip() +str(random.randint(1000,99999)) + '@hotmail' )
