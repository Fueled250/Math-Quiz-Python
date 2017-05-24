#S.McDonald 11/1/2016
#math_quiz
#This program will generate two random numbers, adds them, and compares the result
#with a user's input


import random #to be used for generating random numbers

#input
#function to generate random number
def gen_random_num():
    num = random.randint(0, 10) #return a randomly generated num between 0-1000
    return num

#calculate sum
def calculate_sum(num_1st, num_2nd):
    return num_1st + num_2nd

#display prompt, ask for result
def display_prompt(num1, num2):
    print("Please add the two numbers: ", num1, " and ", num2)
    user_res = int(input(">>"))
    return user_res

#compare the total with user's result
def compare_results(total, user_res):
    if user_res == total:
        print("Congrats! You can add!!")
    else:
        print("Failure! You cannot add! Since you cannot add, the answer is: ", total)



#processing
def main():
    #call random num 1 generator
    num1 = gen_random_num()
    #call random num 2 generator
    num2 = gen_random_num()
    #add the two numbers
    total = calculate_sum(num1, num2)
    #provide user with two numbers to add: display the prompt
    user_res = display_prompt(num1, num2)
    #compare the result
    compare_results(total, user_res)


#call the main()
main()
    
