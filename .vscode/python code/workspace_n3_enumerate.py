from tkinter import E

print()
print("#enumerate 사용하기")

l = ["A", "B", "C"]
print(list(enumerate(l)))
print()

for i, value in enumerate(l):

    print("{}번째 요소는 {}입니다".format(i, value))

print()

dic = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"

}

print()
print("#items 사용하기")
print("items():", dic.items())
print()

for key, element  in dic.items():
    print("dict[{}] = {}".format(key, element))


array = [i * i for i in range(0, 20, 2)]

print(array)

print()
print("#join 사용하기")

number = int(input("정수 입력> "))

if number % 2 == 0:
    print("\n".join([
          "입력한 문자열은 {}입니다.",
          "{}는(은) 짝수입니다."
          ]).format(number, number))

else:
    print("\n".join([
          "입력한 문자열은 {}입니다.",
          "{}는(은) 홀수입니다."
          ]).format(number, number))

print()
print("#이진수로 변환하기")

output = [i for i in range(1, 101) if "{:b}".format(i).count('0') == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))

print("합계: ", sum(output))

