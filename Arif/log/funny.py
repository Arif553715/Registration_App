
default = 1
first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

third_number = int(input("Third Number: "))
fourth_number = int(input("Fourth Number: "))
result1 = first_number + second_number
result2 = second_number / 2
result3 = third_number / 2
main_result = default + result1 + result2 + result3
print(main_result)
if main_result != 100:
    print("It is not 100. Try again please")
else:
    print("Successful Result", main_result)