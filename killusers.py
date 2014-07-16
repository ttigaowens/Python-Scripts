import os

##This is a dumb script to delete user profiles from a Citrix server

exempt = ["Public", "Default", ".NET", "All"]

for d in os.listdir('c:\\users\\'):
        newpath = str("C:\\users\\" + d)
        try:
                pos = d.index(" ")
        except:
                pos = len(d)
        if  d[0:pos] not in exempt:
                #os.system("mkdir " + newpath)
                os.system("rd " + newpath + " /s /q")
                print d + " - DELETED"
                        
        else:
                print d
