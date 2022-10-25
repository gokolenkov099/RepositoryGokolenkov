def openFile():
    f1 = open('data.txt','r')
    while True:
        data = f1.readline().split("-")
        print(data)
        if data[0] == '':
            break
        return data
        f1.close()
    except IOError:
        print(IOError.with_traceback())

 def dataMonth()
        data2= openFile()
        print(data2)
        data1 =['01','09','1999']
        if int(data2[0])< int(data1[0]):
            data1[0]=data2[0]
        if int(data2[1])<int(data1[1]):
            data2[1]=data1[1]
    print(data1[0], "-", data1[1])
