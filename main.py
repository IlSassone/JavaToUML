from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys


fnt = ImageFont.truetype("./fonts/SFPro.ttf", 18)
title = ImageFont.truetype("./fonts/Heavy.ttf", 20)
qrcode = Image.open("./github.png", "r")



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
        while not temp[cont]== "{" and not temp[cont]== "throws": 
            #cont > tipo dato
            #cont+1 > nome attributo
            print(temp[cont])
            
            temp[cont+1]=temp[cont+1].replace(",","")
            nStr+=temp[cont+1]+": "
            nStr+=temp[cont]+", "
            cont+=2     
            
            
        nStr+=") "
        pass
    if mode == "methodName":
        temp = str.replace("(", " ")
        temp = temp.replace(")", " ")
        temp = temp.split()
        
        if temp[0]=="private":
            nStr+="- "
        elif temp[0]=="public":
            nStr+="+ "
        elif temp[0]=="protected":
            nStr+="# "

        nStr+=temp[2]+"( "
        cont = 3
        while not temp[cont] == "{":
            temp[cont+1]=temp[cont+1].replace(",","")
            nStr+=temp[cont+1]+": "
            nStr+=temp[cont]+", "
            cont+=2
        nStr+="): "+temp[1]

    """if len(nStr) >= 50:
        nStr = nStr[:50] +"\n"+nStr[50:]
        """
    my_wrap = textwrap.TextWrapper(width = 60)
    wrap_list = my_wrap.wrap(text=nStr)
    nStr = "\n".join(wrap_list)
    return nStr


mode = None
className = None
classAttributes = []
classConstructors = []
classMethods = []
f = open(sys.argv[1], "r")
f1 = f.readlines()
f.close()
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


im = Image.new("RGB", (500, 750), color="white")

d = ImageDraw.Draw(im)

#writes title
d.text((20, 15), className, font=title, fill="black")
d.line((0,50, 500, 50), fill="grey")
#writes attributes
offset = 60
for item in classAttributes:
    d.text((20, offset), item, font=fnt, fill="black")
    offset+=20
offset+=10
d.line((0,offset, 500, offset), fill="grey")
offset+=10

for item in classConstructors:
    d.text((20, offset), item, font=fnt, fill="black")
    if "\n" in item:
        offset+=40
    else: offset+=20

for item in classMethods:

    d.text((20, offset), item, font=fnt, fill="black")
    if "\n" in item:
        offset+=40
    else: offset+=20



#writes the repo's qrcode
im.paste(qrcode.resize((75,75)), (420, 670))

im.save("output.png")
im.show()
