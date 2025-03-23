# creating an empty list
height_lst = []
weight_lst= []
name_lst =["Steve", "Tony", "Natasha","Bruce","Peter","Bucky"]
lst_bmi =[]
Underweight = []
Normal_Weight = []
Overweight = []


 

# for loop that uses the names list to ask the user to input the height and weight of the person. After that it will use that information and it will be appended to the hieght and weight list.
#Then next it will input those into the BMI equation and later and the BMI to lst_bmi. The loop will run until the final person information as been inputed. 
for i in range(len(name_lst)):
    height = int(input("Enter in " +name_lst[i]+ "'s height (in inches): " ))
    weight = int(input("Enter the " +name_lst[i]+ "'s weight (in pounds): " ))
    # adding the element
    height_lst.append(height)
    weight_lst.append(weight) 
    
    bmi = weight_lst[i]*703/height_lst[i]**2
    lst_bmi.append(bmi)
   
#This for loop will run into it gets to the end of the names array. Inbeded in the for loop is an if loop that is seeing what that BMI would be classified in Underweight, Normal weight and Overweight.
#When it figures out what if statment is true it will enter that BMI number into the list that the if statment is found true for. 
for i in range(len(name_lst)):
    if lst_bmi[i] > 24.90:
        Overweight.append(i)
    elif lst_bmi[i] > 18.5:
         Normal_Weight.append(i)
    else:
        Underweight.append(i)
    
    
 # This is will print the length of the array for Underweight, Normal weight, and Overweight and showing the user how many people are in those catergories but doesn't show the people's BMI.    
print("Amount of people that are Underweight: ", len(Underweight))
print("Amount of people that are normal wieght: ", len(Normal_Weight))
print("Amount of people that are overweight :",len(Overweight))

    
   
