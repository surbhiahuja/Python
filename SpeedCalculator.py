from time import *
import random as r

print(time())

def mistake(partest, user):

    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=user[i]:
                error +=1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e-time_s
    time_round = round(time_delay,2)
    speed = len(userinput)/time_round
    return round(speed)

test = ["A paragraph is a A paragraph is a A paragraph is a A paragraph is a"]
test1 = r.choice(test)
print("*****Typing Speed*******")
print(test1)
print("")
print("")
time_1 = time()
testinput = input("Enter : ")
time_2 = time()

print('Speed: ', speed_time(time_1, time_2, testinput))
print("Error ", mistake(test1, testinput))


