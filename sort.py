import os
import sys
import shutil

def createdir(dirname):
    
    try:
        os.makedirs(dirname)
    except OSError:
        if os.path.exists(dirname):
            pass
        else:
            raise
def checkfile():
	lists=[]
	for files in os.listdir("."):
        	extension =os.path.splitext(files)[1][1:]
        	if extension:
        		lists=lists+[files+" "+extension]
	return lists
    	

i=raw_input("Path of folder to be sorted : ")

try:
	fp=open("list.lst","r")
except:
	print "Sorry! can't read file list.lst"
	sys.exit(2)
st=os.stat(fp.name)
try:
	os.chdir(i)
except:
	print "Sorry! can't find the specified directory"
	sys.exit(3)


files=checkfile()

while True:
	line=fp.readline()	
	if not line:
		break
	name=line.split("=")[0]	 #Entry name in the list file
	exts= line.split("=")[1] #Extensions provided in the list file
	
	for i in files:
		
		b=i.split(" ") #b[1]=extension of the file b[0]=Name of the file
		
		if b[1]==" ":
			continue
		for chext in exts.split(" "):
			if b[1] == chext:
				print "Creating directory",name
				createdir(name)
				print "moving",b[0],"to",name,"/",b[0]
				shutil.move(b[0],name+"/"+b[0])
				 
	
fp.close()
