from datetime import datetime
start_time = datetime.now()
#--------------------------
def Every_Digit_Number(n):
    digits_list = []
    while(n > 0):
        digits_list.append(n%10)
        n //= 10
    for digit in range(1, 10):
        if digit not in digits_list:
            return False
    return True
#---------------------------
largest_pandigital_number = -1
N = 100000 #1e5
for base in range(1, N):
    x = base
    mult = 2
    while(len(str(x))<9):
        x = int(str(x) + str(mult*base))
        mult+=1
    if(len(str(x))==9 and Every_Digit_Number(x)):
        print(x, end=", ")
        if x > largest_pandigital_number:
            largest_pandigital_number = x
print()
print(largest_pandigital_number)
#-------------------------------
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))