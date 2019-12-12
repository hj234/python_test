from numpy import *
group = [1,2,3,4]
group2 = [3,4,5,6]
result = zeros(4)
i=0
for number in group:
    for number2 in group2:
        result[i] += number * number2
    i = i+1
print(result)