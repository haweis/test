#coding:utf-8 
  
try: 
    import xml.etree.cElementTree as ET 
except ImportError: 
    import xml.etree.ElementTree as ET 
import sys 
  
try: 
    tree = ET.parse("obj.xml")     #打开xml文档 
    #root = ET.fromstring(country_string) #从字符串传递xml 
    root = tree.getroot()         #获得root节点  
except Exception, e: 
    print "Error:cannot parse file:obj.xml."
    sys.exit(1) 
print root.tag, "---", root.attrib  

print '*'*20, "一. loop root", "*"*20
for child in root: 
    print child.tag, "---", child.attrib["name"], "(%d)" % (int(child.attrib["attr_cnt"]))
    for loop in range(int(child.attrib["attr_cnt"])):
        print "|--->", child[loop].attrib["id"], ":", child[loop].attrib["index"]
print 




print '*'*20, "二. interater", "*"*20
for obj in root.iter('obj'):
    print obj.attrib["name"], "(%d)"% int(obj.attrib["attr_cnt"])
    for index in range(int(obj.attrib["attr_cnt"])):
        print "|--->", child[index].attrib["id"], ":", child[index].attrib["index"]
print

print '*'*20, "三. class", "*"*20
class AttrClass(object):
    def __init__(self, attr):
        mydict = attr.attrib
        self.id=mydict["id"]
        self.key=mydict["index"]
    def showattr(self):
         print "|--->", self.id, ":", self.key



class ObjClass(object):
    def __init__(self, obj):
        mydict=obj.attrib
        self.name=mydict["name"]
        self.attr_cnt=mydict["attr_cnt"]
    def showObj(self):
         print self.name, "(%d)" % (int(self.attr_cnt))
    def showAllAttr(self,obj):
         for index in range(int(self.attr_cnt)):
             myattr=AttrClass(obj[index])
             myattr.showattr()


for obj in root:
    myobj=ObjClass(obj)
    myobj.showObj()
    myobj.showAllAttr(obj)
