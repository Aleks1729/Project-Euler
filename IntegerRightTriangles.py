from datetime import datetime
start_time = datetime.now()
#--------------------------
MAX_PERIMETER = 1000 + 7
number_of_solutions = [0 for _ in range(MAX_PERIMETER)]
max_number_of_solutions = -1
perimeter_with_max_number_of_solutions = -1
#-----------------------
for perimeter in range(1, MAX_PERIMETER):
    for a in range(1, perimeter):
        for b in range(a, perimeter-a):
            c = perimeter-a-b
            if(a**2 + b**2 == c**2):
                number_of_solutions[perimeter] += 1
                if(number_of_solutions[perimeter] > max_number_of_solutions):
                    max_number_of_solutions = number_of_solutions[perimeter]
                    perimeter_with_max_number_of_solutions = perimeter
                #print('(', a, ", ", b, ", ", c, ')', sep="")
print(perimeter_with_max_number_of_solutions)
print(max_number_of_solutions)
#-------------------------------
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))