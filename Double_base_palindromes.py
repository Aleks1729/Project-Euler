from datetime import datetime
start_time = datetime.now()
#----------------------------
N = 1000000 #1e6
#-------------------------
def If_Palindrome(string):
    d = len(string)
    for i in range(d//2):
        if(string[i] != string[d-i-1]):
            return False
    return True
#----------------------------
cnt = 0
sum = 0
for n in range(N):
    if(If_Palindrome(str(n)) and If_Palindrome(bin(n)[2:])):
        print(n, end=", ")
        sum+=n
        cnt+=1
print()
print(cnt)
print(sum)
#-----------------------------
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))