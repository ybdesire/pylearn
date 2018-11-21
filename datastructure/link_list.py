class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
        
        
def main():
    # init link list
    n4 = Node(4,None)
    n3 = Node(3,n4)
    n2 = Node(2,n3)
    n1 = Node(1,n2)
    n0 = Node(0,n1)
    # go through link list
    n = n0
    while(n!=None):
        print(n.data)
        n = n.next_node
    
    
if __name__ == '__main__':
    main()