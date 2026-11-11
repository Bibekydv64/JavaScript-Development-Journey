# 🔥 LEVEL 2 — Trend Logic
# Q11
# Print:
# UP
# DOWN
# SAME
# for every comparison.

# current_number = 0
# previous_number = 0
# num_of_obj = []

# for num in range(10):
#     user_input = int(input('Enter a Number:'))
#     num_of_obj.append(user_input)

#     current_number = user_input
#     previous_number = user_input

#     if previous_number >= current_number:
#         print(f'Up trend')
#         print(f'up trend Number:{user_input}')
#         print(f'previous Number:{previous_number}')

#     else:
#         print(f'down trend')
#         print(f'down trend Number:{user_input}')
#         print(f'previous Number:{previous_number}')
        

                              

# Q12
# Count total UP trends.
# Example:
# 2 → 5

# print('When you enter 200 then Program Exit automatically!')

# previous_holder_number = 0

# while True:
#     user_input = int(input('Enter a Number:'))

#     if user_input == 200:
#         print(f'program Exit you entered:{user_input}')
#         break

#     elif previous_holder_number > user_input:
#         print(f'Up trend, previous Number{previous_holder_number} and curent Number{user_input}')

#     else:
#         print(f'Down trend, previous Number:{previous_holder_number} and curent Number:{user_input}')
        
# previous_holder_number = user_input



# print('Enter 200 to exit')

# previous_holder_number = None
# total_up_trends = 0

# while True:
#     user_input = int(input('Enter a Number: '))

#     if user_input == 200:
#         print('Program Exit')
#         break

#     if previous_holder_number is None:
#         previous_holder_number = user_input
#         continue

#     if user_input > previous_holder_number:
#         print(f'UP Trend: {previous_holder_number} → {user_input}')
#         total_up_trends += 1

#     elif user_input < previous_holder_number:
#         print(f'DOWN Trend: {previous_holder_number} → {user_input}')

#     else:
#         print('Sideways: No change')

#     previous_holder_number = user_input

# print(f'Total UP trends: {total_up_trends}')





        


# Q15
# Find longest UP streak.
# Example:
# 1 2 3 4 1
# Longest UP streak:
# 3











# Q16
# Find longest DOWN streak.


# Q17
# Count how many times trend changes.
# Example:
# UP → DOWN
# DOWN → UP




# Q18
# Detect if sequence is fully increasing.


# Q19
# Detect if sequence is fully decreasing.

# Q20
# Detect zig-zag pattern.
# Example:
# 1 5 2 6 3 7


# 🔥 LEVEL 3 — Positive + Trend Mix


# Q21
# Count:
# positive UP trends
# negative DOWN trends




# Q22
# Count:
# negative → positive
# transitions.



# Q23
# Count:
# positive → negative
# transitions.



# Q24
# Find biggest positive number.


# Q25
# Find smallest negative number.




# Q26
# Print first negative number only.






# Q27
# Print second positive number only.






# Q28
# Break loop after:
# 3 positives
# 2 negatives




# Q29
# Take input until positive sum becomes greater than 100.




# Q30
# Take input until negative count becomes 5.















