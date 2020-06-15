className = None
classAttributes = []
classConstructors = []
classMethods = []
f = open("Impiegato.java", "r")
f1 = f.readlines()
f.close()


#the className must me in upper case in camelNotation, so the first word with capital is the className
def searchName(list):
    for items in list:
        if items[0].isupper():
            return items
    
    return None


def strClean(str, mode):
    nStr = ""
    #clean the className
    if mode == "className":
        if "abstract" in str:
            nStr += "abstract "
        elif "interface" in str:
            nStr += "interface "

        temp = str.split()
        nStr+=searchName(temp)
        pass
    
    if mode == "attributeName":
        temp = str.split()
        #writes visibility
        if temp[0]=="private":
            nStr+="- "
        elif temp[0]=="public":
            nStr+="+ "
        elif temp[0]=="protected":
            nStr+="# "
        #writes attribute name
        if temp[1] == "static" or temp[1] == "final":
            if temp[2] == "static" or temp[2] == "final":
                nStr+=temp[4]+": "
                
            else:
                nStr+=temp[3]+": "
        else:
            nStr+=temp[2]+": "
        
        nStr = nStr.replace(";", '')
        
        if temp[1] == "static" or temp[1] == "final":
            nStr+= temp[1]+" "
            if temp[2] == "static" or temp[2] == "final":
                nStr += temp[2]+" "
                nStr += temp[3]
            else:
                nStr += temp[2]
        else: 
            nStr += temp[1]
        
        pass

    if mode == "constructorName":
        temp = str.replace("(", " ")
        temp = temp.replace(")", " ")
        temp = temp.split()
        print(temp)
        if temp[0]=="private":
            nStr+="- "
        elif temp[0]=="public":
            nStr+="+ "
        elif temp[0]=="protected":
            nStr+="# "

        nStr+=temp[1]+"( "
        cont = 2
        while not "throws" in temp[cont]:
            #cont > tipo dato
            #cont+1 nome attributo
            nStr+=temp[cont+1]+": "
            nStr+=temp[cont]+", "
            cont+=2
        nStr+=") "
        pass
    if mode == "methodName":
        temp = str.replace("(", " ")
        temp = temp.replace(")", " ")
        temp = temp.split()
        print(temp)
        if temp[0]=="private":
            nStr+="- "
        elif temp[0]=="public":
            nStr+="+ "
        elif temp[0]=="protected":
            nStr+="# "

        nStr+=temp[2]+"( "
        cont = 3
        while not temp[cont] == "{":
            nStr+=temp[cont+1]+": "
            nStr+=temp[cont]+", "
            cont+=2
        nStr+="): "+temp[1]




    return nStr


mode = None

for l in f1:
    #finds the name of the class and saves it
    if "class" in l:
        className = strClean(l, "className")
        
    if mode == None:
        if "start_" in l: #is this the start of a mode?
            #which mode in particular?
            if "start_attributes" in l:
                print("mode changed to attributes")
                mode = "attributes"
            elif "start_constructors" in l:
                mode = "constructors"
                print("mode changed to constructors")
            elif "start_methods" in l:
                mode = "methods"
                print("mode changed to methods")
        
    
    #saves the attributes in UML notation
    if mode == "attributes":
        if "private" in l or "public" in l or "protected" in l:
            classAttributes.append(strClean(l, "attributeName"))
            
        if "end_attributes" in l:
            mode = None
            print("there are no more attributes to scan")

    #saves the constructors in UML notation
    elif mode == "constructors":
        if "private" in l or "public" in l or "protected" in l:
            classConstructors.append(strClean(l, "constructorName"))
        
        
        
        if "end_constructors" in l:
            mode = None
            print("there are no more constructors to scan")



    #saves methods in UML notation
    elif mode == "methods":
        if "private" in l or "public" in l or "protected" in l:
            classMethods.append(strClean(l, "methodName"))



        if "end_methods" in l:
            mode = None
            print("there are no more methods to scan")

print(className)
print(classAttributes)
print(classConstructors)
print(classMethods)