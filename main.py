import random
import time

def digit_generator(hmd_fd, hmd_sd): # hmd_fd = how many digits for first digit, hmd_sd = how many digits for second digit
    fd = "".join([str(random.randint(0,9)) for j in range(hmd_fd)])
    sd = "".join([str(random.randint(0,9)) for j in range(hmd_sd)])
    
    if fd == "0":
        fd = int(fd)
    else:
        fd = int(fd.lstrip('0'))
        
    if sd == "0":
        sd = int(sd)
    else:
        sd = int(sd.lstrip('0'))
        
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
    
def get_ready():
    print("ready?")
    time.sleep(3)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print("go!\n")
    
def quizzing(problem_set, answer_key):
    correct = 0
    lst_marker = 0
    ttp = [] # time per problem
    
    for l in problem_set:
        ts_ep = time.time() # time start for each problem
        print(f"{str(lst_marker + 1)}. {printing_out(l, oper)}")
        answer = int(input("type answer: "))
        if answer == answer_key[lst_marker]:
            correct += 1
        lst_marker += 1
        te_ep = time.time() # time end for each problem
        ttp.append(int(te_ep - ts_ep))
    
    attp = round(sum(ttp) / len(ttp), 1)
        
    return correct, attp 
    
if __name__ == "__main__":
    q = int(input("how many problems?: "))
    fd = int(input("how many digits for first digit?\n>>> "))
    sd = int(input("how many digits for second digit?\n>>> "))
    oper = int(input("what operation?\n1.addition\n2.subtraction\n3.multiplication\n>>> "))
    
    problem_set = number_of_problems(q, fd, sd)
    answer_key = answerkey(problem_set, oper)
    
    get_ready()
    
    time_start = time.time()
    correct_answers, avg_time_per_problem = quizzing(problem_set, answer_key)
    time_finish = time.time()
    
    print(f"final score: {round(correct_answers / q * 100, 2)} % ({correct_answers}/{q})")
    print(f"elapsed time: {int(time_finish - time_start)}")
    print(f"average time per problem: {avg_time_per_problem}")
    
    # ideas:
    #     -stats sheet
    #     -random operation per problem?