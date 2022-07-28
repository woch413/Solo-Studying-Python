key_list = ["name", "hp", "mp", "leve"]
value_list = ["기사", 200, 30 , 5]
character = {}

for  x in range(len(key_list)):

    character[key_list[x]] = value_list[x]

print(character)    

print()
print()

limit = 30000
i = 1
sum_value = 0


while sum_value < limit:

    
    sum_value = sum_value + i

    i += 1

    
print("{}를 더할때 {}을 넘으며 그때의 값은 {}입니다".format(i-1, limit, sum_value))

print()
print()

max_value = 0
a = 0
b = 0

for i in range(1, 101):

    j = 100 - i

    if max_value <= i * j:
        
        a = i
        b = j

        max_value = a * b

        

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))