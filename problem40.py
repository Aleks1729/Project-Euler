from datetime import datetime
start_time = datetime.now()
#--------------------------
N = 1000000 #1e6
c = 7
#--------------------------
champernowne_constant = ""
n = 1
while(len(champernowne_constant) < N):
    champernowne_constant += str(n)
    n+=1
ans = 1
for i in range(c):
    ans *= int(champernowne_constant[10**i-1])
print(ans)
#-------------------------------
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))