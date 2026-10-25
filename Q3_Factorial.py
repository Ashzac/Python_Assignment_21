fact = 1
user_num = int(input("enter a user number:- "))
temp_num  = user_num
while temp_num>0:
    fact*=temp_num
    temp_num = temp_num-1
print(f"the factorial of the number {user_num} is {fact}")