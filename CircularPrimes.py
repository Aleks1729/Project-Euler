import math
from datetime import datetime
start_time = datetime.now()
#-------------------------------------
N = 1000000 #10^6
isPrime = [True for _ in range(N)]
Primes = []
#--------------------------------------
def Eratosthenes_Sieve():
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, N):
        if(isPrime[i]):
            Primes.append(i)
            for j in range(i**2, N, i):
                isPrime[j] = False

def Is_Circular(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if(int(Get_Permutation(str_n, i)) not in Primes):
            return False
    return True

def Get_Permutation(string, index):
    return string[index:] + string[:index]
#-------------------------------------------
Eratosthenes_Sieve()
cnt = 0
for prime in Primes:
    if(Is_Circular(prime)):
        print(prime, end=", ")
        cnt+=1
print()
print(cnt)
#------------------------------------------------
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))