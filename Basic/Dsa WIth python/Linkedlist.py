class Node:
    def __init__(self,v):
        self.val=v
        self.next=None


class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_positon(self,pos,val):
        newNode=Node(val)
        if pos==0:
            newNode.next=self.head
            self.head=newNode

        else:    
         temp=self.head
         for i in range(pos-1):
            temp=temp.next
            if temp==None:
                print("Out of bounds")
                return
         newNode.next=temp.next
         temp.next=newNode

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
    
    def delete_at_positon(self,pos):
        if pos==0:
          delnode=self.head
          self.head=self.head.next
          del delnode

        else:
            temp=self.head
            for i in range(pos-1):
                temp=temp.next
                if temp==None:
                    print("Out of bound")
                    return
            
            delnode=temp.next
            if temp.next==None:
                
                return
            temp.next=temp.next.next
            del delnode

    def reverse(self):
        # base case
        if self.head.next==None:
            return self.head
        #head in save first save will have 10 then 20 then 30 and so on
        save=self.head
        # head next value in head
        self.head=self.head.next
        # self.reverse() is like we do in reverse(head->next)
        newHead=self.reverse()
        # save->n->n means that saveing value of its own to next pointer
        #like 30 is save and 40 save.next.next so saving 30 in 40
        save.next.next=save
        save.next=None
        return newHead
   


def main():
    list=Linkedlist()
    list.insert_at_tail(10)
    list.insert_at_tail(20)
    list.insert_at_tail(30)
    list.insert_at_tail(40)
    # list.insert_at_positon(6,100)
    # list.delete_at_positon(3)
    list.reverse()
    list.print_list()


                


main()