from os.path import exists


#reading from file
def file_read(filename):
    try:
        f = open(filename, 'r')
        text = f.read().split("\n")
        if text[-1]=="":
            del text[-1]
        f.close()
        return text
    except:
        print("error in reading file")


#writing in file
def file_write(filename,text):
    try:
        f = open(filename, 'w')
        for x in range(len(text)):
            f.write(text[x]+"\n")
        f.close()
    except:
        print("error in writing file")

#checking file for existing
def file_check(filename):
    return exists(filename)

#creating file
def file_create(filename):
    try:
        f = open(filename, 'w')
        f.close()
    except:
        print("error in creating file")    