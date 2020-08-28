from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys


fnt = ImageFont.truetype("./fonts/SFPro.ttf", 18)
title = ImageFont.truetype("./fonts/Heavy.ttf", 20)


class ImageCreator:
    def __init__(self, fileName):
        self.file = fileName
        self.mode = None
        self.className = None
        self.classAttributes = []
        self.classConstructors = []
        self.classMethods = []
        self.im = Image.new("RGB", (500, 750), color="white")
        self.d = ImageDraw.Draw(self.im)

        self.readData()
        self.writeImage()

        

        
    

    def searchName(self, list):
        for items in list:
            if items[0].isupper():
                return items
        
        return None

    def strClean(self, str, modes):

        temp = None
        nStr = ""
        #clean the className
        if modes == "className":
            if "abstract" in str:
                nStr += "abstract "
            elif "interface" in str:
                nStr += "interface "

            temp = str.split()
            nStr+=self.searchName(temp)
            pass
        
        if modes == "attributeName":
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

        if modes == "constructorName":
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
        if modes == "methodName":
            flaggella = False
            abstract = False
            temp = str.replace("(", " ")
            temp = temp.replace(")", " ")
            temp = temp.split()
            if temp[1] == "abstract":
                temp.remove("abstract")
                abstract = True
            if temp[1] == "static": 
                temp.remove("static")
                flaggella = True
            if temp[0]=="private":
                nStr+="- "
            elif temp[0]=="public":
                nStr+="+ "
            elif temp[0]=="protected":
                nStr+="# "

            nStr+=temp[2]+"( "
            cont = 3
            while not temp[cont] == "{" and not temp[cont]== "throws" and not temp[cont]==";":
                temp[cont+1]=temp[cont+1].replace(",","")
                nStr+=temp[cont+1]+": "
                nStr+=temp[cont]+", "
                cont+=2
            nStr+="): "+temp[1]
            if flaggella == True: nStr+=" static"
            if abstract == True: nStr+=" abstract"
        """if len(nStr) >= 50:
            nStr = nStr[:50] +"\n"+nStr[50:]
            """
        my_wrap = textwrap.TextWrapper(width = 60)
        wrap_list = my_wrap.wrap(text=nStr)
        nStr = "\n".join(wrap_list)
        return nStr


    def readData(self):
        with open(self.file, "r") as f:
            for l in f:
                if "class" in l:
                    self.className = self.strClean(l, "className")

                if self.mode == None:
                    if "start_" in l: #is this the start of a mode?
                        #which mode in particular?
                        if "start_attributes" in l:
                            print("mode changed to attributes")
                            self.mode = "attributes"
                        elif "start_constructors" in l:
                            self.mode = "constructors"
                            print("mode changed to constructors")
                        elif "start_methods" in l:
                            self.mode = "methods"
                            print("mode changed to methods")
                    
                
                #saves the attributes in UML notation
                if self.mode == "attributes":
                    if "private" in l or "public" in l or "protected" in l:
                        self.classAttributes.append(self.strClean(l, "attributeName"))
                        
                    if "end_attributes" in l:
                        self.mode = None
                        print("there are no more attributes to scan")

                #saves the constructors in UML notation
                elif self.mode == "constructors":
                    if "private" in l or "public" in l or "protected" in l:
                        self.classConstructors.append(self.strClean(l, "constructorName"))
                    
                    
                    
                    if "end_constructors" in l:
                        self.mode = None
                        print("there are no more constructors to scan")



                #saves methods in UML notation
                elif self.mode == "methods":
                    if "private" in l or "public" in l or "protected" in l:
                        self.classMethods.append(self.strClean(l, "methodName"))



                    if "end_methods" in l:
                        self.mode = None
                        print("there are no more methods to scan")

            print(self.className)
            print(self.classAttributes)
            print(self.classConstructors)
            print(self.classMethods)

    def writeImage(self):
        #writes title
        self.d.text((20, 15), self.className, font=title, fill="black")
        self.d.line((0,50, 500, 50), fill="grey")
        #writes attributes
        offset = 60
        for item in self.classAttributes:
            self.d.text((20, offset), item, font=fnt, fill="black")
            offset+=20
        offset+=10
        self.d.line((0,offset, 500, offset), fill="grey")
        offset+=10

        for item in self.classConstructors:
            self.d.text((20, offset), item, font=fnt, fill="black")
            if "\n" in item:
                offset+=60
            else: offset+=20

        for item in self.classMethods:

            self.d.text((20, offset), item, font=fnt, fill="black")
            if "\n" in item:
                offset+=60
            else: offset+=20


