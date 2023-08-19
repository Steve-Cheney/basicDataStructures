# Basic Data Structures (BDS)
# Last updated: 8/12/23
#
# This package contains basic generic data structures and relevant tools. 
#
# Classes included in this file:
#   - node
#   - linkedList
#
#
# https://www.stephendoescomp.bio
# Stephen Cheney © 2023

class node:
    next = None
    prev = None
    val = None

    
    def __init__(self, val):
        self.val = val

    
    # Format:
    #   Node
    #   Val: [val]
    #   Prev: [val] Next: [val]
    def __str__(self):
        currVal = str(self.getVal())
        prevVal = "None"
        nextVal = "None"
        if self.getPrev() is not None:
            prevVal = str(self.getPrev().getVal())
        if self.getNext() is not None:
            nextVal = str(self.getNext().getVal())
        return '***** Node *****\nVal: '+ currVal + '\nPrev: ' + prevVal + ' Next: ' + nextVal + '\n****************\n'

    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def getVal(self):
        return self.val
    
    def setNext(self, n):
        self.next = n
        if n is not None and self is not None:
            n.prev = self
    def setPrev(self, n):
        self.prev = n
        if n is not None and self is not None:
            n.next = self       
    
    # Returns three lists of the prev, curr, and next node values starting at given node
    def nodeList(self):
        curr = self
        @staticmethod
        def appendPrev(n):
            if n.getPrev() is None:
                return None
            else:
                return n.getPrev().getVal()
        
        @staticmethod
        def appendNext(n):
            if n.getNext() is None:
                return None
            else:
                return n.getNext().getVal()
        
        prevList = [appendPrev(curr)]
        nodeList = [curr.getVal()]
        nextList = [appendNext(curr)]
        
        while curr.getNext() is not None:
            curr = curr.getNext()
            prevList.append(appendPrev(curr))
            nodeList.append(curr.getVal())
            nextList.append(appendNext(curr))
        
        return prevList, nodeList, nextList
        
    def nodeListToString(self):
        nodeListOut = self.nodeList()
        return 'Prev:' + str(nodeListOut[0]) + '\nNode:' + str(nodeListOut[1]) + '\nNext:' + str(nodeListOut[2])


class linkedList:
    head = None
    last = None
    length = 0

    def __init__(self, n):
        self.head = n
        self.last = n
    
    def __len__(self):
        return self.length

    # Format
    #   [val][val][...][val]
    def __str__(self):
        out = ""
        if self.getHead() is None:
            return out    
        curr = self.getHead()
        while curr is not None:
            out += str(curr.getVal())
            curr = curr.getNext()
        return out

    def getHead(self):
        return self.head
    def getLast(self):
        return self.last
    def getLength(self):
        return self.length
    def addLen(self):
        self.length += 1
    def subLen(self):
        self.length -= 1

    def setHead(self, n):
        self.head = n
        return self.head
    def setLast(self, n):
        self.last = n
        return self.last

    # Append a node (n) to the linkedlist object
    def append(self, n):
        self.addLen()
        if self.getHead() is None:
            self.setHead(n)
            self.setLast(n)
            return self
        else:
            self.getLast().setNext(n)
            n.setPrev(self.getLast())
            self.setLast(n)
            n.setNext(None)
            return self
        
    # Prepend a node (n) of any value to the start of the linkedlist object
    def prepend(self, n):
        oldh = self.getHead()
        newh = self.setHead(n)
        oldh.setPrev(newh)
        newh.setNext(oldh)
        self.addLen()
        return self

    # Pad the start of the linkedlist object (padNum) times with a node of value (val)
    def padFront(self, padNum, val):
        assert type(padNum) is int and padNum > 0
        for i in range(padNum):
            self.prepend(node(val))
        return self

    # Pad the end of the linkedlist object (padNum) times with a node of value (val)    
    def padEnd(self, padNum, val):
        assert type(padNum) is int and padNum > 0
        for i in range(padNum):
            self.append(node(val))
        return self    
    
    # Remove and return the last node of the linkedlist object
    def pop(self):
        end = self.getLast()
        prev = end.getPrev()
        prev.setNext(None)
        self.setLast(prev)
        self.subLen()
        return end  
    
    # Remove and return the first node of the linkedlist object
    def delete(self):
        head = self.getHead()
        next = head.getNext()
        next.setPrev(None)
        self.setHead(next)
        self.subLen()
        return head
    
    # Return the node at the given index (i)
    # 0-indexed
    def nodeAt(self, index):
        # based on wanted index, determine if faster to forward or reverse traverse
        # i <= length/2 -> forward traversal (start at head)
        # i > length/2 -> reverse traversal (start at last)
        # i < 0 -> reverse traversal
        
        # edge cases:
        #   i oob -> return None
        #   i = head -> getHead()
        #   i = last -> getLast()

        linkedListLength = self.getLength()

        if index >= linkedListLength:
            return None
        if index == 0:
            return self.getHead()
        if index == linkedListLength - 1:
            return self.getLast()
        
        @staticmethod
        def forwardTraverse(fT):
            currNode = self.getHead()
            for j in range(fT):
                currNode = currNode.getNext()
            return currNode
        
        @staticmethod
        def reverseTraverse(rT):
            currNode = self.getLast()
            for j in range(rT - 1):
                currNode = currNode.getPrev()
            return currNode
        
        if index > 0:
            if index <= linkedListLength / 2:
                return forwardTraverse(index)
            else:
                return reverseTraverse(linkedListLength - index)
        
        if index < 0:
            index = abs(index)
            if index > linkedListLength: # if i would traverse more than one length of LL
                index = index % linkedListLength # mod to prevent uneccessary traversals
            return reverseTraverse(index)
    

    # Given a Linked List, split and return 2 Linked Lists at the given index
    def splitAt(self, index):
        linkedListLength = self.getLength()

        if index == 0:
            return self, None
        if index >= self.getLength():
            return None, None
        target1 = self.nodeAt(index - 1)
                
        target2 = self.nodeAt(index)
                
        target1.setNext(None)
        target2.setPrev(None)

        ll1 = linkedList(self.getHead())
        ll2 = linkedList(target2)
        
        ll1.setLast(target1)
        ll2.setLast(self.nodeAt(linkedListLength - 1))
        
        @staticmethod
        def setLength(ll, n):
            ll.length = n
        
        setLength(ll1, index)
        setLength(ll2, linkedListLength - index)

        return ll1, ll2
    
    # Given this Linked List and a second Linked List, pad with value (pad) to match lengths
    def padMatch(self, ll2, pad):
        selfLength = self.getLength()
        ll2Length = ll2.getLength()

        lenDiff = abs(selfLength - ll2Length)

        if selfLength > ll2Length:
            ll2.padFront(lenDiff, pad)
        else:
            self.padFront(lenDiff, pad)
        
        return self, ll2
    
    # Extend this Linked List with (ll2)
    def extend(self, ll2):
        currLast = self.getLast()
        currLast.setNext(ll2.getHead())
        ll2.getHead().setPrev(currLast)
        self.setLast(ll2.getLast())
        
        @staticmethod
        def setLength(ll2, n):
            ll2.length = n

        setLength(self, self.getLength() + ll2.getLength())
        return self

    
class main:
    def main():
    
        '''################################
              __node__ class examples
        ################################'''
        print()
        print('\n__node__ class examples')
        # Creating three nodes with values: [1, 2, 3]
        nodeEx1 = node(1)
        nodeEx2 = node(2)
        nodeEx3 = node(3)
        print('\nnode.__str__ of nodeEx1:\n')
        print(nodeEx1)

        # Setting previous and next nodes of one node
        nodeEx2.setPrev(nodeEx1)
        nodeEx2.setNext(nodeEx3)

        print('Concatanated nodes:')
        print(nodeEx1)
        print(nodeEx2)
        print(nodeEx3)

        # Return three lists of the prev, curr, and next node values starting at given node
        # String form of nodeList()
        print('Nodes in list form')
        print(nodeEx1.nodeListToString())

        '''################################
           __linkedList__ class examples
        ################################'''
        print()
        print('\n__linkedList__ class examples')
        # Creating an empty Linked List
        linkedListEx = linkedList(None)
        # Filling a Linked List by appending nodes
        string = "0123456789"
        for chr in string: 
            linkedListEx.append(node(int(chr)))
        
        print('\nlinkedList.__str__ of linkedListEx:')
        print(linkedListEx)
        print('\nHead Node:\n', linkedListEx.getHead())
        print('Last Node:\n', linkedListEx.getLast())
        print('Length: ', linkedListEx.getLength())
        print('Prepending node(\'A\')')
        linkedListEx.prepend(node('A'))
        print('\nlinkedListEx:')
        print(linkedListEx)
        print('\nPadding end with 3 Bs')
        linkedListEx.padEnd(3,'B')
        print(linkedListEx)
        print('\nPadding front with 4 0s')
        linkedListEx.padFront(4, 0)
        print(linkedListEx)
        print('\nPopping removes and returns the last node:')
        print(linkedListEx.pop())
        linkedListEx.pop()
        linkedListEx.pop()
        print('\nDeleting removes and returns the first node:')
        print(linkedListEx.delete())
        linkedListEx.delete()
        linkedListEx.delete()
        linkedListEx.delete()
        linkedListEx.delete()
        print(linkedListEx)
        print('\nnodeAt(i) returns the node at index i:')
        print(linkedListEx.nodeAt(6))
        print('\nsplitAt(i) returns a modified original linked list and a new linked list split at index i:')
        splitLL = linkedListEx.splitAt(4)
        print('index = 4')
        print(splitLL[0])
        print(splitLL[1])
        print('\npadMatch matches input linked lists with given pad value:')
        paddedLL = splitLL[0].padMatch(splitLL[1],'Z')
        print('pad = \'Z\'')
        print(paddedLL[0])
        print(paddedLL[1])
        print('\nextend() extends the target linked list with given linked list:')
        extendedLL = paddedLL[1].extend(paddedLL[0])
        print('Extending paddedLL[0] with paddedLL[1]')
        print(extendedLL)

    main()