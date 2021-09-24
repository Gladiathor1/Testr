import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse
from itertools import groupby
import numpy as np

tree = ET.parse('output1.xml')
root = tree.getroot()



temp = []


for page in root:
    for textbox in page:
        for textline in textbox:
            for text in textline:
                if(text.tag=="text"):
                    if("font" in text.attrib):
                        if text.attrib['font'] == "UNOPWS+Helvetica-Bold" and text.text.isdigit():
                            text.tag="Question"
                            temp.append(text)



#tree._setroot(root)
tree.write("output12.xml")


for val in temp:
    print(list(temp))


values = set(map(lambda x:x.attrib['bbox'].split(',')[0], temp))
#print(values.text)


newlist = [[y for y in temp if y.attrib['bbox'].split(',')[0]==x] for x in values]

#for group in newlist:
 #   print(group)
temp1=[]
check=False
for group in newlist:
    print('[', end='')
    #if(str(group)==sorted(str(group))):
    index=0
    myelm=0
    for elm in group:
        check=False
        print(elm.text)
        if index==0:
            myelm=int(elm.text)
        if(index>0):
            print(newval.text)
            if myelm==1:
                if(int(elm.text)>int(newval.text)):
                    if(int(elm.text)==(int(newval.text)+1)):
                        print("checking here")
                        print(elm.text," ",newval.text)
                        check=True
                    else:
                        check=False
                else:
                    check=False
        index += 1
        newval=elm
    if(check==True):
        temp1.append(group)
    print(']')
print("end")
mybbox=""
for val in temp1:
    print("break")
    for i in val:
        print(i.text)
        print(i.attrib['bbox'])
        mybbox=(i.attrib['bbox'].split(',')[0])
        print(mybbox)


tree = ET.parse('output1.xml')
root = tree.getroot()


for page in root:
    for textbox in page:
        for textline in textbox:
            for text in textline:
                if ("bbox" in text.attrib):
                    if (text.attrib['bbox'].split(',')[0] == mybbox):
                        if ("font" in text.attrib):
                            if text.attrib['font'] == "UNOPWS+Helvetica-Bold" and text.text.isdigit():
                                print('found')
                                text.tag = "MyQuestion"

tree.write("output123.xml")