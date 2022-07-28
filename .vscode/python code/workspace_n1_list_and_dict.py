from tkinter import E
from unicodedata import name


print("______숫자정리_____")
print()

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,1,3,5,4,8,9,7,2,3]
counter ={}

for number in numbers:
    counter[number] = numbers.count(number)

print(counter)
print()
print("  list, dict, str   섞인 자료 분배하기")
print()

character = {
    "name" : '기사',
    'level' : "12",
    'items' : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
        },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
    }

for key in character:

    if type(character[key]) is str:
        print(key, ":", character[key])
    
    # if type(character[key]) is int:
    #     print(key, ":", character[key]) 만약 character 에서 12 를 str 이 아닌 int 형태로 만든다면 이 코드를 실행해야함
    
    if type(character[key]) is list:

        for x in character[key]:
            print(key, ":", x)
    
    if type(character[key]) is dict:

        for x in character[key]:
            print(x, ":", character[key][x])



#예제

print()
print()


En_dict = {"expose" : "노출하다", "throughout" : ["~동안 죽", "~에 걸처"],
           "rather" : "다소",  "exposure" : "노출", "artifical" : "인공의", 
           "director" : {"Me" : "LWC", "My_Brain" : "lol"},
           "books" : {"셰익스피어" : "hamlet", "reading book" : "three days" },
      
      
          }



while True == True:

    name_key = input()
    
    if name_key not in En_dict:

        print("아직 학습되지 않은 정보입니다")

    else:

        if type(En_dict[name_key]) is str:

            print(name_key, ":", En_dict[name_key])

        elif type(En_dict[name_key]) is list:

            for e in En_dict[name_key]:

                print(name_key, ":", e)

        elif type(En_dict[name_key]) is dict:

            for x in En_dict[name_key]:

                print(x, ":", En_dict[name_key][x])


    