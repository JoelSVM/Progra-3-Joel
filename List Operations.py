list=[1,2,3,4,5,2,2]
list.append(6)
print list
print"-------------------"
print list.count(2)
print"-------------------"
xList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
xList.extend(bList)
print "Extended List : ", xList
print"-------------------------------"
aList = [123, 'xyz', 'zara', 'abc'];
print "Index for xyz : ", aList.index( 'xyz' ) 
print "Index for zara : ", aList.index( 'zara' )
print "Index for abc : ", aList.index( 'abc' )
print"----------------------------------------------"
aList = [123, 'xyz', 'zara', 'abc'];
aList.insert( 3, 2009)
print "Final List : ", aList
print"-----------------------------------------"
aList = [123, 'xyz', 'zara', 'abc'];
print "A List : ", aList.pop()
print "B List : ", aList.pop()
print "C List : ", aList.pop()
print"-------------------------------------------"
aList = [123, 'xyz', 'zara', 'abc'];
aList.remove("abc")
print "list " ,aList
print"----------------------------------------------"
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.reverse();
print "List : ", aList
print"----------------------------------------------"
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
aList.sort();
print "List : ", aList


