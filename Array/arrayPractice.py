from array import *


# 1. Create an array and tranverse
my_arr = array('i', [1,2,3,4,5])

for i in my_arr:
    print(i)

# 2. Access individual elements through indexes
print("Step 2")
print(my_arr[2])

# 3. Append any value to the array using append() method
print("Step 3")
my_arr.append(20)
print(my_arr)

# 4. Insert value in an array using insert() method
print("Step 4")
my_arr.insert(3, 7)
print(my_arr)

# 5. Extend python array using extend() method
print("Step 5")
my_arr1 = array('i', [3, 5, 8,])
my_arr.extend(my_arr1)
print(my_arr)

# 6. Add items from list into array using fromlist() method
print("Step 6")
tempList = [1, 9, 40]
my_arr.fromlist(tempList)
print(my_arr)

# 7. Remove any array element using remove() method
print("Step 7")
my_arr.remove(4)
print(my_arr)

# 8. Remove last array element using pop() method
print("Step 8")
my_arr.pop()
print(my_arr)

# 9. Fetch my element through its index using index() method
print("Step 9")
print(my_arr.index(8))

# 10. Reverse a python array using reverse() method

# 11. Get array buffer information through buffer_info() method
# 12. Check for number of occurances of an element using count() method
# 13. Convert array to string using tostring() method
# 14. Convert array to a python list with same elements using tolist() method
# 15. Append a string to char array using fromstring() method