'''
2, 3, 5, 7, 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397, 
748334
15
Duration: 0:01:13.745872
'''
from datetime import datetime
start_time = datetime.now()
#--------------------------
N = 1000000 #1e6
isPrime = [True for _ in range(N)]
Primes = []
#--------------------------------
def Eratosthenes_Sieve():
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, N):
        if(isPrime[i]):
            Primes.append(i)
            for j in range(i**2, N, i):
                isPrime[j] = False
def Truncatable_Prime_Right(n):
    n //= 10
    while(n>0):
        if n not in Primes:
            return False
        n //= 10
    return True
def Truncatable_Prime_Left(n):
    str_n = str(n)
    for _ in range(len(str_n)-1):
        str_n = str_n[1:]
        n = int(str_n)
        if n not in Primes:
            return False
    return True
#---------------------------------
Eratosthenes_Sieve()
sum = 0
cnt = 0
for prime in Primes:
    if(Truncatable_Prime_Right(prime) and Truncatable_Prime_Left(prime)):
        print(prime, end=", ")
        sum+=prime
        cnt+=1
print()
print(sum)
print(cnt)
#-------------------------------
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))