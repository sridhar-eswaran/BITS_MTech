# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:14:31 2021

@author: SESWARAN
"""

class node:
    def __init__(self,book_id=None,avail_count=None):
        self.book_id=book_id
        self.avail_count = avail_count
        self.inventory_count = avail_count
        self.checkOut_count = 0
        self.left_child=None
        self.right_child=None
        #self.parent=None # pointer to parent node in tree

class binary_search_tree:
    def __init__(self):
        self.root=None

#%% Q1 :: Read Books List

    def readBookList(self,book_id,avail_count):
        if self.root==None:
            self.root=node(book_id,avail_count)
        else:
            self._readBookList(book_id,avail_count,self.root)

    def _readBookList(self,book_id,avail_count,cur_node):
        global file
        if book_id<cur_node.book_id:
            if cur_node.left_child==None:
                cur_node.left_child=node(book_id,avail_count)
                #cur_node.left_child.parent=cur_node # set parent
            else:
                self._readBookList(book_id,avail_count,cur_node.left_child)
        elif book_id>cur_node.book_id:
            if cur_node.right_child==None:
                cur_node.right_child=node(book_id,avail_count)
                #cur_node.right_child.parent=cur_node # set parent
            else:
                self._readBookList(book_id,avail_count,cur_node.right_child)
        else:
            print("book_id already in database!")
            file.write('\n book_id already in database!')


#%% Q2 :: Check in / Check Out
#check in
    def checkOut(self,book_id):
        global file
        print('\n ***CHECK OUT BOOKS***')
        file.write('\n ***CHECK OUT BOOKS***')
        if self.root!=None:
            return self._checkOut(book_id,self.root)
        else:
            return None

    def _checkOut(self,book_id,cur_node):
        global file
        if book_id==cur_node.book_id:
            if cur_node.avail_count>=1:
                cur_node.avail_count -= 1
                cur_node.checkOut_count +=1
                file.write('\n'+repr(book_id) + ' has been successfully checked out; # of books available:' + repr(cur_node.avail_count))
                return print(f'{book_id} has been successfully checked out; # of books available:{cur_node.avail_count} ')
            if cur_node.avail_count==0:
                file.write('\n' + repr(book_id) + ' not available for check out')
                return print(f'Book {book_id} not available for check out')
        elif book_id<cur_node.book_id and cur_node.left_child!=None:
            return self._checkOut(book_id,cur_node.left_child)
        elif book_id>cur_node.book_id and cur_node.right_child!=None:
            return self._checkOut(book_id,cur_node.right_child)

#checkin
    def checkIn(self,book_id):
        print('\n ~~~CHECK IN BOOKS~~~')
        file.write('\n ~~~CHECK IN BOOKS~~~')
        if self.root!=None:
            return self._checkIn(book_id,self.root)
        else:
            return None

    def _checkIn(self,book_id,cur_node):
        if book_id==cur_node.book_id:
            if cur_node.avail_count<cur_node.inventory_count:
                cur_node.avail_count += 1
                file.write('\n'+repr(book_id) + ' has been successfully checked in; # of books available:' + repr(cur_node.avail_count))
                return print(f'{book_id} has been successfully checked in; # of books available:{cur_node.avail_count} ')
            if cur_node.avail_count>=cur_node.inventory_count:
                file.write('\n Additional Book' + repr(book_id) + ' Please add it to ledger before transacting')
                return print(f'Additional Book {book_id} received. Please add it to ledger before transacting ')
        elif book_id<cur_node.book_id and cur_node.left_child!=None:
            return self._checkIn(book_id,cur_node.left_child)
        elif book_id>cur_node.book_id and cur_node.right_child!=None:
            return self._checkIn(book_id,cur_node.right_child)


    
#%% Q3 :: Get Top 3 Books

    def topChkOut(self):
        print('\n ***TOP3 BOOKS LIST***')
        file.write('\n\n ***TOP3 BOOKS LIST***')
        if self.root!=None:
            self._topChkOut(self.root)
            file.write('\n Top Book 1:: ID:'+repr(t1.book_id)+'; Checkout Count: '+repr(t1.checkOut_count))
            print('Top Book 1:: ID:'+str(t1.book_id)+'; Checkout Count: '+str(t1.checkOut_count)) ######
            file.write('\n Top Book 2:: ID:' + repr(t2.book_id) + '; Checkout Count: ' + repr(t2.checkOut_count))
            print('Top Book 2:: ID:'+str(t2.book_id)+'; Checkout Count: '+str(t2.checkOut_count)) ######
            file.write('\n Top Book 3:: ID:' + repr(t3.book_id) + '; Checkout Count: ' + repr(t3.checkOut_count))
            print('Top Book 3:: ID:'+str(t3.book_id)+'; Checkout Count: '+str(t3.checkOut_count)) ######

            
    def _topChkOut(self,cur_node):
        global t1,t2,t3
        if cur_node!=None:
            self._topChkOut(cur_node.left_child)

            if t1 == None:
                t1 = cur_node

            elif t1 != None and t2 == None:
                if t1.checkOut_count > cur_node.checkOut_count:
                    t2 = cur_node
                elif t1.checkOut_count <= cur_node.checkOut_count:
                    t2 = t1
                    t1 = cur_node

            elif t1 != None and t2 != None and t3 == None:
                if t1.checkOut_count <= cur_node.checkOut_count and t2.checkOut_count > cur_node.checkOut_count:
                    t3 = t2
                    t2 = t1
                    t1 = cur_node
                elif t2.checkOut_count <= cur_node.checkOut_count:
                    t3 = t2
                    t2 = cur_node
                else:
                    t3 = cur_node

            
            elif t1 != None and t2 != None and t3 != None:
                if t1.checkOut_count <= cur_node.checkOut_count:
                    t3 = t2
                    t2 = t1
                    t1 = cur_node

                elif t1.checkOut_count > cur_node.checkOut_count and t2.checkOut_count <= cur_node.checkOut_count:
                    t3 = t2
                    t2 = cur_node

                
                elif t2.checkOut_count > cur_node.checkOut_count and t3.checkOut_count <= cur_node.checkOut_count:
                    t3 = cur_node
                        
                    
              
            self._topChkOut(cur_node.right_child)

#%% Q4 :: Get Not issued books

    def notChecked(self):
        print('\n ***NOT ISSUED BOOKS LIST***')
        file.write('\n\n ***NOT ISSUED BOOKS LIST***')
        if self.root!=None:
            self._notChecked(self.root)
            
    def _notChecked(self,cur_node):
        if cur_node!=None:
            self._notChecked(cur_node.left_child)

            if cur_node.checkOut_count == 0:
                file.write('\n Book ID: '+repr(cur_node.book_id)+' is not issued and the available copies are: '+repr(cur_node.avail_count))
                print('Book ID: '+str(cur_node.book_id)+' is not issued and the available copies are: '+str(cur_node.avail_count))
                    
              
            self._notChecked(cur_node.right_child)       

#%% Q5 :: Find Books
## Search book list
    def search(self,book_id):
        print('\n ***BOOK SEARCH RESULT***')
        file.write('\n\n ***BOOK SEARCH RESULT***')
        if self.root!=None:
            return self._search(book_id,self.root)
        else:
            return 

    def _search(self,book_id,cur_node):
        if book_id==cur_node.book_id:
            if cur_node.avail_count>=1:
                file.write('\n Book '+repr(book_id)+' available for check out; # of books available:'+repr(cur_node.avail_count))
                return print(f'Book {book_id} available for check out; # of books available:{cur_node.avail_count} ')
            if cur_node.avail_count==0:
                file.write('\n Book ' + repr(book_id) + ' not available for check out')
                return print(f'Book {book_id} not available for check out')
        elif book_id<cur_node.book_id and cur_node.left_child!=None:
            return self._search(book_id,cur_node.left_child)
        elif book_id>cur_node.book_id and cur_node.right_child!=None:
            return self._search(book_id,cur_node.right_child)
        file.write('\n Book ' + repr(book_id) + ' does not exist')
        return print(f'Book {book_id} does not exist') 
    
    
#%% Q6 :: Print Books List
    def print_tree(self):
        global totalBooks
        print('\n ***BOOK INVENTORY***')
        file.write('\n\n ***BOOK INVENTORY***')
        print(f'\n ***Total Number of Books available: {totalBooks}***')
        file.write('\n***Total Number of Books available:'+repr(totalBooks)+'***')
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            file.write('\nBook ID:'+repr(cur_node.book_id)+' \t Available:'+repr(cur_node.avail_count)+' \t No. Check outs = '+repr(cur_node.checkOut_count))
            print (f'Book ID:{cur_node.book_id} \t Available: {cur_node.avail_count} \t No. Check outs = {cur_node.checkOut_count}')
            self._print_tree(cur_node.right_child)


#%% Main Function
def readBooksList(binaryTree,filepath):
    with open(filepath) as file:
        lines = file.readlines()
    lines = [line.replace('\n','').split(',') for line in lines]
    [binaryTree.readBookList(int(book[0]),int(book[1])) for book in lines]
    return lines

#create outputFile txt



def readPrompts(binaryTree,filepath):
    with open(filepath) as file:
        lines = file.readlines()
    lines = [line.replace('\n','').split(':') for line in lines]
    for line in range(len(lines)):
        if lines[line][0] == 'checkOut':
            binaryTree.checkOut(int(lines[line][1]))
        if lines[line][0] == 'checkIn':
            binaryTree.checkIn(int(lines[line][1]))
        if lines[line][0] == 'ListTopBooks':
            binaryTree.topChkOut()
        if lines[line][0] == 'BooksNotIssued':
            binaryTree.notChecked()
        if lines[line][0] == 'findBook':
            binaryTree.search(int(lines[line][1]))
        if lines[line][0] == 'printInventory':
            binaryTree.print_tree()
    return lines
            
txtfileLocation = 'C:/Users/seswaran/OneDrive/OneDrive - JAGUAR LAND ROVER/M.Tech_Materials/05_Assignments/DSAD/fileList.txt'
promptfileLocation = 'C:/Users/seswaran/OneDrive/OneDrive - JAGUAR LAND ROVER/M.Tech_Materials/05_Assignments/DSAD/prompts.txt' 
bookLedger = binary_search_tree()  
lines = readBooksList(bookLedger,txtfileLocation)
file = open('C:/Users/seswaran/OneDrive/OneDrive - JAGUAR LAND ROVER/M.Tech_Materials/05_Assignments/DSAD/outputFile.txt','w')
#bookIdList = [int(line[0]) for line in lines]   
totalBooks  = len(lines)
t1=None
t2=None
t3=None
prompts = readPrompts(bookLedger,promptfileLocation)
file.close()


