class Node:
    def __init__(self,v):
        self.val=v
        self.next=None


class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_tail(self,val):
        NewNode =Node(val)
        if self.head==None:
           self.head=NewNode
        else:
            tmp=self.head
            while tmp.next != None:
                tmp=tmp.next

            tmp.next=NewNode


    def print_list(self):
         tmp=self.head
         while tmp!= None:
          print(tmp.val)
          tmp=tmp.next



def main():
    list=Linkedlist()
    list.insert_at_tail(10)
    list.insert_at_tail(20)
    list.insert_at_tail(30)
    list.insert_at_tail(40)
    list.print_list()
                


main()