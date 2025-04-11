import random


hmd_fd = int(input("input how many digits for the first digit: ")) # how many digits for first digit
hmd_sd = int(input("input how many digits for the second digit: ")) # how many digits for second digit

fd = [random.randint(0,9) for j in range(hmd_fd)].join()
sd = [random.randint(0,9) for j in range(hmd_sd)].join()

print(fd,sd)