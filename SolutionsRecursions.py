# #Task1: 
# n = int(input())

# def rec(n):
#     if n==1:
#         print(n)
#     else:
#         rec(n-1)
#         print(n, sep = '\f')
#         print()
# rec(n)


#Task2:
# n = int(input())
# def sum(n):
#     if n<=1:
#         return n
#         print(n)
#     else:
#         return(n+sum(n-1))
# print(sum(n))
# sum(n)

#Task3: 
def recursion(num): 
    if num < 10: 
        return num
    else: 
        return int(str(num%10)+str(recursion(num//10))

print(int(recursion(34256))

# number = int(input("Enter the number: "))  
# revr_num = 0    
# def recur_reverse(number):  
#     global revr_num  
#     if (num > 0):  
#         Reminder = number % 10  
#         revr_num = (revr_num * 10) + Reminder  
#         recur_reverse(number // 10)  
#     return revr_num  
      
# revr_num = recur_reverse(number)  
# print("n Reverse of entered number is = %d" % revr_num) 


# def step(n): 
#     if n ==1: 
#         return 1
#     elif n == 2: 
#         return 2
#     elif n == 3: 
#         return 4
#     else: 
#         return step(n-1) + step(n-2) + step(n-3)
    
#     print(step(7))



