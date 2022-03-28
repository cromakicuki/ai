from datetime import datetime
from turtle import right

# odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
# for i in range(5):
#     right_this_minute = datetime.today().minute

#     if right_this_minute in odds:
#         print('This minute seems a little odd.')
#     else:
#         print('Not an odd minute.')

# print('Hello num!')

# 21+21

# ultimate_answer = 21+ 21
# print(ultimate_answer)

# for i in [1,2,3]:
#     print(i)

# for ch in 'Hi!':
#     print(ch)

# for num in range(5):
#     print('Head First Rocks!')

import random
import time
print(help(random.randint))

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute.')
    wait_time = random.randint(1,5)
    time.sleep(wait_time)
