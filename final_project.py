class Soultion1:
    # This Algorithm is taking in arrays that are already sorted, looking for the first occurrence of the target. Time Complextity 0(log(n))
    # This definition is making it so arr and target into instances so I can show multiple test cases.
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
#Start find_first_occurance by splitting it into right half and left half
    def find_first_occurance(self):
        left = 0 
        right = len(self.arr)-1
        answer = -1
#This is while loop that keeps running till left is bigger than the right side
        while left <= right:
            mid = (left + right) // 2
#If the target is found in the middle than the answer changes to the allocation of the middle
            if self.arr[mid] == self.target: 
                answer = mid
                right = mid - 1
#If the arr[mid] is smaller than the target the left side is mid +1             
            elif self.arr[mid] < self.target:
                left = mid + 1
#If the arr[mid] is bigger than the target the right changes to mid +1

            else: 
                right = mid - 1
        
        print(answer)
from math import ceil, floor
#This Algorithm is looking to rotate the array to left until zero is at the front of the array, Time Complexity is 0(n)
# This definition is making it so arr into instances so I can show multiple test cases.
class Soultion2:
    def __init__(self, arr):
        self.arr = arr
#I made a variable to find the index of 0 in the array. Then used that variable to make the new array with it rotating to the left

    def rotate_left_until_zero(self):
        zero_index = self.arr.index(0)
        print(self.arr[zero_index:] + self.arr[:zero_index])
#This Algorithm is used to take an array of characters such as “+,-,/,*” and do those operations on the last 2 numbers that are on the array. Time Complexity: O(n)
# This definition is making it so arr into instances so I can show multiple test cases.
class Soultion3:
    def __init__(self, arr):
        self.arr = arr
    def RPN(self):
#Looking for Char in the array so I used multiple if statements to see which character is being used then depending on the operation it would do that to the elements that were popped off the array.         
        stack = []
        for char in self.arr:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif char == '/':
                
                a = stack.pop()
                b = stack.pop()
#This if statement is used to show an error for the user if they tried to divide by a zero in the program.
                if  a != 0:
                    stack.append(int(b/a))
                else:
                    error = stack.append("Error")                  
                    print(error)
                    break

            elif char == '*':
                stack.append(stack.pop()* stack.pop())
            else: stack.append(int(char))

        print(stack)

class Node:
    # Data stored in the node Time Complexity is O(n1+n2)
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to merge two sorted linked lists
def sort_two_linked_lists(list1, list2):
    # Create a dummy node to serve
    # as the head of the merged list
    dummy_node = Node(0)
    temp = dummy_node

    # Traverse both lists simultaneously
    while list1 is not None and list2 is not None:
        # Compare elements of both lists and
        # link the smaller node to the merged list
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        # Move the temporary pointer
        # to the next node
        temp = temp.next

    # If any list still has remaining
    # elements, append them to the merged list
    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
    # Return the merged list starting
    # from the next of the dummy node
    return dummy_node.next

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()
#This is going first becuase it was the only way I could get Algorithm 4 to print 
if __name__ == "__main__":
    # Test Cases for the Algorithm 4
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(4)

    list2 = Node(1)
    list2.next = Node(3)
    list2.next.next = Node(4)

    list3 = Node(5)
    list3.next = Node(7)
    list3.next.next = Node(9)

    list4 = Node(2)
    list4.next = Node(6)
    list4.next.next = Node(8)

    list5 = Node(0)
    
    list6 = Node(2)
    list6.next = Node(6)
    list6.next.next = Node(8)

    merged_list = sort_two_linked_lists(list1, list2)
    merged_list2 = sort_two_linked_lists(list3,list4)
    merged_list3 = sort_two_linked_lists(list5,list6)
    print("Merged sorted linked list 1: ", end="")
    print_linked_list(merged_list)
    print("Merged sorted linked list 2: ", end="")
    print_linked_list(merged_list2)
    print("Merged sorted linked list 3: ", end="")
    print_linked_list(merged_list3)
     


s1 = Soultion1([1, 1, 2, 3, 3, 6, 10, 10, 10, 100], 3)
s2 = Soultion1([2, 3, 5, 7, 11, 13, 17, 19], 6)
s3 = Soultion1([], 1)
s4 = Soultion1([2],2)
s5 = Soultion1([74, 72, 76, 44, 100, 53, 100, 84, 41, 97], 97)
s6 = Soultion1([1, 1, 2, 3, 3, 6, 10, 10, 10, 100], 100)
print("The first occurance for Test Case 1:", end = "")
s1.find_first_occurance()
print("The first occurance for Test Case 2:", end = "")
s2.find_first_occurance()
print("The first occurance for Test Case 3:", end = "")
s3.find_first_occurance()
print("The first occurance for Test Case 4:", end = "")
s4.find_first_occurance()
print("The first occurance for Test Case 5:", end = "")
s5.find_first_occurance()
print("The first occurance for Test Case 6:", end = "")
s6.find_first_occurance()
soulution2_1 =Soultion2([3, 6, 9, 7, 0, 1, 2, 8])
soulution2_2 =Soultion2([6, 6, 10, 20, 3, 2, 7, 15, 16, 0])
soulution2_3 =Soultion2([0, 15, 20, 12, 14, 0, 17, 5, 13])
soulution2_4 =Soultion2([0])
print("Rotate Left till zero is in front of the Array, Test Case 1:", end = "")
soulution2_1.rotate_left_until_zero()
print("Rotate Left till zero is in front of the Array, Test Case 2:", end = "")
soulution2_2.rotate_left_until_zero()
print("Rotate Left till zero is in front of the Array, Test Case 3:", end = "")
soulution2_3.rotate_left_until_zero()
print("Rotate Left till zero is in front of the Array, Test Case 4:", end = "")
soulution2_4.rotate_left_until_zero()
soultion3_1 = Soultion3([ '2', '1', '+', '3', '*'])
soultion3_2 = Soultion3([ '4', '13', '5', '/', '+'])
soultion3_3 = Soultion3([ '4', '0', '5', '/', '+'])
soultion3_4 = Soultion3([ "100", "6", "9", "3", "+", "-11", "*", "/", "*", "170", "+", "5", "+"])
soultion3_5 = Soultion3([ '4', '0', '/', '2', '-3','-','-'])
print("Reverse Polish Notation, Test Case 1:", end = "")
soultion3_1.RPN()
print("Reverse Polish Notation, Test Case 2:", end = "")
soultion3_2.RPN()
print("Reverse Polish Notation, Test Case 3:", end = "")
soultion3_3.RPN()
print("Reverse Polish Notation, Test Case 4:", end = "")
soultion3_4.RPN()
print("Reverse Polish Notation, Test Case 5:", end = "")
soultion3_5.RPN()












