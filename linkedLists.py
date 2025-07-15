class Node:
    def __init__(self,dataval= None):
        self.dataval=dataval
        self.nextval= None

class LinkedList:
    def __init__(self):
        self.headval = None

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode= Node(newdata)
        NewNode.nextval= middle_node.nextval
        middle_node.nextval= NewNode

    def listprint(self):
        printval= self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list1= LinkedList()
list1.headval = Node("Mon")
e2= Node("Tue")
e3 = Node("Thurs")
e4 = Node("Fri")

list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4

list1.Inbetween(list1.headval.nextval,"Wed")
list1.listprint()