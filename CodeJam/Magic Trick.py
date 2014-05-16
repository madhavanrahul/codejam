f= open('D:\CodeJam\MagicTrick.IN','rU')


testcases = int(f.readline()); 
#print testcases
#for line in f:
#    print line



for case in range(testcases):
 output = []
 firstArrang = [] 
 secondArrang = []
 temp = ""
 firstguess = int(f.readline());
 #print firstguess
 for i in range(4):
     temp =  f.readline()
     firstArrang.append(temp.split())   
 
 secondguess = int(f.readline());
 #print secondguess
 for i in range(4):
     temp =  f.readline()
     secondArrang.append(temp.split())              
  
 for var in firstArrang[firstguess-1]:
    if var in secondArrang[secondguess-1]:
#        print case," : ",firstArrang[firstguess-1],"and",secondArrang[secondguess-1]
        output += var
 
 if len(output)>1:
     print "Bad Magician"
 elif len(output)<1:
     print "playercheated"
 else:   
     print output[0]
              
  
f.close()
