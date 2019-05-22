#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
from vncdotool import api
import sys
import time
import linecache

def sam(a,b):
    return(a+b)
def qwerty(c,d):
    if c<=d:
        return("go")
    return
def runTest():
    line = linecache.getline("/dip/test1/test_sl.cfg", 1)
   # print(line)
    #nmax = 15
    #print(nmax)
    i=1
    while i <= int(5):
        line = linecache.getline("/dip/test1/test_sl.cfg", i)
        cr_vm= line.split(' ')
        #print(s)
        if cr_vm[0] == "NameVM:":
            name_vm = cr_vm[1]
	    name_vm=name_vm[0:-1]
            print(name_vm)
        elif cr_vm[0] == "PortVM:":
            port_vm = cr_vm[1]
	    port_vm=port_vm[0:-1]
            print(port_vm)
        elif cr_vm[0] == "HostVM:":
            host_vm = cr_vm[1]
	    host_vm=host_vm[0:-1]
            print(host_vm)
	elif cr_vm[0] == "WayVM:":
            way_vm = cr_vm[1]
	    way_vm=way_vm[0:-1]
            print(way_vm)

        i+=1
    
    fname_cr_vm="./create_vm.sh"
    
    create_vm = ' '.join((fname_cr_vm, name_vm, way_vm, port_vm))

    print(create_vm) 
    if name_vm != '' and port_vm != '' and way_vm != '':
            #start script
	
	subprocess.call("%s" % create_vm, shell=True,stdout=subprocess.PIPE)
	#subprocess.call(["%s" % create_vm])
	#ubprocess.Popen([
	
        print("Ok!")
    else:
        print("Error! NameVM: and(or) PortVM: NOT DEFINED! If you want exit: Q. If you want continue: S.")
        err=iinput()
        if err == "Q":
        	sys.exit()
    
    if host_vm != '' and port_vm != '':
             #start script
 	add_client='::'.join((host_vm, port_vm))
	print(add_client)
	client=api.connect(add_client, password=None)
        
	print("Ok!")
    else:
        print("Error! NameVM: and(or) PortVM: NOT DEFINED! If you want exit: Q. If you want continue: S.")
        err=input()
        if err == "Q":
        	sys.exit()
      
        
    i=1
    n=1
    while i <= int(108):
        line = linecache.getline("/dip/test1/test_sl.cfg", i)
        drive_in = line.split(' ')
        #print(p)
        
        if drive_in[0] == "MouseMove:":
	  	x=drive_in[1]
		#x=x[0:-1]
		y=drive_in[2]
		y=y[0:-1]
		print(x)
		print(y)
		client.mouseMove(int(x),int(y))
        elif drive_in[0] == "MousePress:":
            	mp=drive_in[1]
		mp=mp[0:-1]
		print(mp)
		client.mousePress(int(mp))
        elif drive_in[0] == "KeyPress:":
            	key_pr=drive_in[1]
		key_pr=key_pr[0:-1]
            	print(key_pr)
		client.keyPress(str(key_pr))
        elif drive_in[0] == "Pause:":
            	sec=drive_in[1]
		sec=sec[0:-1]
           	print(sec)
		time.sleep(int(sec))
	elif drive_in[0]== "ScreenSrc:":
                src_way=drive_in[1]
                src_way=src_way[0:-1]
                print(src_way)
		n += 1
        elif drive_in[2]== "ScreenResult:":
                  result_way=drive_in[3]
                  result_way_way=result_way[0:-1]
                  print(result_way)
                  client.captureScreen(result_way)
     	rms=int(diffImg(result_way, src_way))
	
	if rms != 0:
		print("Step №%d! ERROR! " % n)
		sys.exit()  
	else:
		print("Step №%d! OK! " % n)
        
 		
	#if drive_in[2]== "ScreenSrc:": 
	#	src_way=drive_in[3]
	#	src_way=src[0:-1]
	#	print(src_way)
	#	client.captureScreen(src_way)
			
	#elif drive_in[3]== "ScreenSrc:":
	#	src_way=drive_in[4]     
        #       src_way=src[0:-1]
        #        print(src_way)
        #        client.captureScreen(src_way)			
 			
        i+=1
def diffImg(file1,file2):
    image1 = Image.open(file1)
   # print image1
    image2 = Image.open(file2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    #h = ImageChops.difference(image1, image2).histogram()
    return math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
runTest()

#def driveTest()
    
    #return 
#def imgDif(img1, img2):
    #return
#def 
