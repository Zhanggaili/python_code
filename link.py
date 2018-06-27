class Node( object ):
    
    def __init__ (self ,elem):
        self.elem = elem
        self.next = None
    
class Singlelinklist( object ):
    
    def __init__(self ,node = None):
        self._head = node
        
    def is_empty(self):
        return self._head == None
    
    def length(self):
        cur = self._head
        count = 0
        if(cur != None):
            count+=1
            cur=cur.next
        return count
    
    def travel(self):
        cur = self._head
        while(cur != None):
            print cur.elem ,
            cur=cur.next
        print('')

    
    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            node.next = cur
            self._head = node
    
    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def insert(self,pos,item):
        node=Node(item)
        n = self.length()
        if pos == 0:
            self.add(item)
        elif pos == n-1:
            self.append(item)
        else:
            count = 0
            cur = self._head
            pre = None
            while pos > count:
                count += 1
                pre = cur
                cur = cur.next
            node.next = cur
            pre.next = node
            
    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
        
    
    def remove(self,item):
        cur = self._head
        pre = None
        if cur.elem == item:
            self._head = cur.next
            return
        while cur.elem != item :
            pre = cur
            cur =cur.next       
            if cur == None :
                return
        pre.next = cur.next
    
if __name__ =='__main__':
    al=Singlelinklist()
    print(al.is_empty())
    print(al.length())
    al.append(1)
    print(al.is_empty())
    al.append(2)
    al.append(3)
    al.append(4)
    al.append(5)
    al.append(6)
    al.append(7)
    al.append(8)
    al.insert(3,100)
    al.travel()
    al.remove(8)
    al.travel()
    print(al.length())
    print(al.search(100))