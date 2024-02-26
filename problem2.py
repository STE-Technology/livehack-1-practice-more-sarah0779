"""This program prints the age of the oldest child
from the ages from the middle and youngest child 
assumming the age differences are the same """

#obtain the ages of youngest and middle child from user
youngest_child=int(input("Enter age of youngest child: "))
middle_child=int(input("Enter age of middle child: "))

#calculate the age difference
age_difference= middle_child - youngest_child

#calculate the age of oldest child
oldest_child=middle_child + age_difference

#print the age of the oldest child
print(oldest_child)