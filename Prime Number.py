value = input()
value = int(value)
is_prime = True

if value == 1:
    is_prime = False

for i in range(2, value):
    if value % i == 0:
        is_prime = False
        break

if is_prime == True:
    print("소수가 맞음")
else:
    print("소수가 아님")


