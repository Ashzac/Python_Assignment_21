sum = 0
user_input = int(input("enter N of choice:- "))
for i in range(1,user_input+1):
    sum += i
print(f"the sum of the first {user_input} natural number is:- {sum}")