import random

def digit_generator(hmd_fd, hmd_sd): # hmd_fd = how many digits for first digit, hmd_sd = how many digits for second digit
    fd = int("".join([str(random.randint(0,9)) for j in range(hmd_fd)]))
    sd = int("".join([str(random.randint(0,9)) for j in range(hmd_sd)]))
    
    if fd == "":
        fd = 0
    if sd == "":
        sd = 0
        
    return [fd, sd]

def number_of_problems(quantity, hmd_fd, hmd_sd):
    return [digit_generator(hmd_fd, hmd_sd) for j in range(quantity)]
        
def answerkey(problem_set, operation):
    if operation == 1:
        return [j[0] + j[1] for j in problem_set]
    elif operation == 2:
        return [j[0] - j[1] for j in problem_set]
    elif operation == 3:
        return [j[0] * j[1] for j in problem_set]
        
def printing_out(problem, operation):
    if operation == 1:
        return str(max(problem)) + ' + ' + str(min(problem)) + " = "
    elif operation == 2:
        return str(max(problem)) + ' - ' + str(min(problem)) + " = "
    elif operation == 3:
        return str(max(problem)) + ' * ' + str(min(problem)) + " = "

        
if __name__ == "__main__":
    q = int(input("how many problems?: "))
    fd = int(input("how many digits for first digit?\n>>> "))
    sd = int(input("how many digits for second digit?\n>>> "))
    oper = int(input("what operation?\n1.addition\n2.subtraction\n3.multiplication\n>>> "))
    
    problem_set = number_of_problems(q, fd, sd)
    answer_key = answerkey(problem_set, oper)
    
    counter = 0
    lst_marker = 0
    for l in problem_set:
        print(f"{str(lst_marker + 1)}. {printing_out(l, oper)}")
        answer = int(input("type answer: "))
        if answer == answer_key[lst_marker]:
            counter += 1
        lst_marker += 1
        
    print(f"final score: {counter / q * 100} % ({counter} / {q})")
    
    # ideas:
    #     -timer and average time per problem
    #     -stats sheet
    #     -random operation per problem?