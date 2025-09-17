class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) - Linear time
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string  = f"[{last.val}"
            while last.next:
                last = last.next
                return_string += f", {last.val}"
            return_string += "]"
            return return_string

    
    # O(n) - Linear time
    def __contains__(self,value):
        last = self.head
        while last is not None:
            if last.val == value:
                return True
            last = last.next
        return False
 
    # O(n) - Linear time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # O(n) linear time
    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node

    # O(1) - constant time
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node

    # O(n) - Linear time 
    def insert(self,value,index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node

    # O(n) - linear time
    def delete(self,value):
        last = self.head
        if last is not None:
            if last.val == value:
                self.head = last.next 
            else:
                while last.next:
                    if last.next.val == value:
                        if last.next.next is None:
                            last.next.next.previous = last
                        last.next = last.next.next
                    last = last.next

    # O(n) - Linear time
    def pop(self,index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                if last.next.next is None:
                    last.next.next.previous = last
                last.next = last.next.next
                 
    # O(n) - Linear time
    def get(self,index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next 
            return last.val


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.append(4)
    ll.insert(5,0)
    ll.insert(15,1)
    ll.append(8)
    ll.append(9)
    ll.insert(17,2)
    ll.delete(15)
    ll.append(10)
    ll.pop(1)
    print(ll)
    print(ll.get(2))
