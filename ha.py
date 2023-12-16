from datetime import datetime
def inputdate():
    a=input("enter date of PT [DD-MM-YY]:")
    j,k,l=a.split("-")
    dateIs = datetime(int(l),int(k),int(j))
    toOrdinal = dateIs.toordinal()
    return toOrdinal

from datetime import datetime  #exact same as the above function but used for date of commencement
def inputcomm():
    a=input("enter date of commencement [DD-MM-YY]:")
    j,k,l=a.split("-")
    dateIs = datetime(int(l),int(k),int(j))
    toOrdinal = dateIs.toordinal()
    return toOrdinal

ha = 1 #assuming HA=true at the start 
x= inputcomm() #the first date example: enlistment date (date is inputed at numner as of now)
y= inputdate()#first PT
ha1=x+14
while True:
    if y>ha1:
        print("ha lost(1)")
        break
    elif y<ha1 and ha==1:
        z=inputdate() #second PT
        d=z-y #duration
        if z>ha1:
            print("ha lost(2)")
            break
        elif d<=7 and z<ha1:
            print("ha true(1)")
            ha1=z+14
            y=z
            continue
        elif d>7:
            ha = 2 #means pending
            print("ha pending")
            continue
        print("ha lost(3)")
        break
    elif ha==2:
        a=inputdate() #third PT
        if (a-z)<=7 and a<=ha1 :
            ha = 1
            print("ha true(2)")
            y=a
            ha1=a+14
        else:
            print("ha lost(4)")
            break        

