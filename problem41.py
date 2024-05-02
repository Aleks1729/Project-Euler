from datetime import datetime
start_time = datetime.now()
import itertools
#--------------------------
largest_pandigital_prime = -1
digits = [i for i in range(1, 8)]
perms = list(itertools.permutations(digits))
#----------------------------------------
def Is_Prime(n):
    d = 2
    while(d*d <= n):
        if(n % d == 0):
            return False
        d+=1
    return True
#--------------------------------
for perm in perms:
    prime_candidate = ""
    for digit in perm:
        prime_candidate += str(digit)
    if Is_Prime(int(prime_candidate)):
        if(int(prime_candidate) > largest_pandigital_prime):
            largest_pandigital_prime = int(prime_candidate)
print(largest_pandigital_prime)
#-------------------------------
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))