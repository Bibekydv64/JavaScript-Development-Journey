// Q1 — Smart Number Analyzer
// Take 10 numbers and:
// Count positive numbers
// Count negative numbers
// Count even numbers
// Find largest number
// Find smallest number
// Example Output
// Positive Numbers = 4Negative Numbers = 3Even Numbers = 5Largest Number = 90Smallest Number = -12

-----------------------------------Using-js--------------------------------------------------------------------------

let obj = []
let positive_counter = 0
let positive_sum = 0

let negative_counter = 0
let negative_sum = 0

let user_range = Number(prompt('Enter a size of list:'))

for(let num=1; num <= user_range; num++){
  let user_number = Number(prompt('Enter Number'))
  obj.push(user_number)
  if(obj > 0{
    positive_counter = positive_counter+1
    positive_sum = positive_sum+obj
  }
  else{
    negative_counter = negative_counter+1
    negative_sum = negative_sum+ obj
  }
  }

console.log(`Total +V counter:${positive_counter}`)
console.log(`Total Positive Sum:${positive_sum}`)

console.log(`Total -V counter:${negative_counter}`)
console.log(`Total Positive Sum:${negative_sum}`)


--------------------------------------------------Using-python--------------------------------------------------------------------------

list = []
positive_counter = 0
positive_sum = 0

negative_counter = 0
negative_sum =0

user_input = int(input('Enter list size:'))

for num in range(user_input):
    user_numbers_input = int(input('Enter a number:'))
    list.append(user_numbers_input)

    if num % 2 == 0:
        positive_counter += 1
        positive_sum  += num

    else:
        negative_counter += 1
        negative_sum  += num
  
print(f'total postive Counter:{positive_counter}')
print(f'Total Postive Sum:{positive_sum}')

print(f'Negative Counter:{negative_counter}')
print(f'Total Negative sum:{negative_sum}')
        
---------------------------------------------------------------------using js-------------------------------------------------------------------------------------

// # Q5 — Advanced Positive Number Logic 🔥
// # Take numbers continuously from user.
// # Stop only when user enters 0.
// # Then:
// # Count positive numbers
// # Count negative numbers
// # Find largest positive number
// # Find smallest negative number
// # Print sum of all positive numbers
// # Example
// # Input:510-270
// # Output:
// # Positive Count = 3Negative Count = 1Largest Positive = 10Smallest Negative = -2Sum Positive = 22

// let array =[]
// let positive_counter = 0
// let positive_sum = 0
// let negative_counter =0
// let negative_sum = 0


// while(true){
//   let user_input = Number(prompt('Enter a values:'))
//   if(user_input != 0){
//     array.push(user_input)
//     if(user_input > 0){
//       positive_counter = positive_counter+1
//       positive_sum += user_input
      
//     }
//     else{
//       negative_counter = negative_counter+1
//       negative_sum += user_input
//     }
//   }
//   else{
//     console.log('Program Breaked You enter:0')
//     break
//   }
// }
// console.log(`Your Enter Values${array}`)
// console.log(`positive Count:${positive_counter}`)
// console.log(`positive Sum:${positive_sum}`)
// console.log(`negative Count:${negative_counter}`)
// console.log(`positive Sum:${negative_sum}`)

// console.log('Min Number:',Math.min.apply(null,array))


---------------------------------------------------------------------using js-------------------------------------------------------------------------------------

// # Q1 — Positive Filter System
// # Take 10 numbers:
// # Count positive numbers
// # Sum only positive numbers
// # Ignore negatives
// let array_obj= []
// let postive_count = 0
// let postive_sum = 0

// console.log('When you Enter 0 program Exit Automatically!')
// while(true){
//   user_input = Number(prompt('Enter a values:'))
//   if(user_input ==0){
//     console.log('program Exited You enter: 0')
//     break
//   }
//   if(user_input > 0){
//     array_obj.push(user_input)
//     postive_sum += user_input
//     postive_count +=1
//   }
//   else{
//     continue
//   }
// }

---------------------------------------------------------------------using js-------------------------------------------------------------------------------------
// # Q3 — Threshold Analyzer
// # Take 10 numbers:
// # Count numbers > 30
// # Sum numbers > 30
// # Find largest number > 30
// let positive_sum = 0
// let postive_count = 0
// let array_obj = []
// for(let num =1; num <=10; num++){
//   user_input = Number(prompt('Enter a values:'))
//   if(user_input >= 30){
//     array_obj.push(user_input)
//     postive_sum += user_input
//     postive_count +=1
//   }
//   else{
//     continue
//   }
// }



// # Q4 — Negative Data Cleaner
// # Take 10 numbers:
// # Count negative numbers
// # Sum negative numbers
// # Ignore positives completely


// let negative_sum = 0
// let negative_count = 0
// let array_obj = []
// for(let num =1; num <=10; num++){
//   user_input = Number(prompt('Enter a values:'))
//   if(user_input < 0){
//     array_obj.push(user_input)
//     negative_sum += user_input
//     negative_count +=1
//   }
//   else{
//     continue
//   }
// }




# Q5 — Zero Detector System
# Take 10 numbers:
# Count zeros
# Count non-zero numbers
# Sum only non-zero numbers




# Q6 — Dual Condition Filter
# Take 10 numbers:
# Count numbers > 50 AND even
# Count numbers > 50 AND odd
# Sum only numbers > 50




# Q7 — Range Analyzer
# Take 10 numbers:
# Count numbers between 10 and 100
# Sum numbers in this range
# Find smallest number in range



# Q8 — Extremes Tracker
# Take 10 numbers:
# Find largest number
# Find smallest number
# Count how many numbers are above average (basic logic: assume average = 50)



# Q9 — Running Sum Break System
# Take numbers continuously:
# Stop when sum exceeds 200
# Count how many numbers entered
# Print final sum


# Q10 — Full Classification System (Hardest)
# Take 10 numbers:
# Count positive even
# Count positive odd
# Count negative even
# Count negative odd
# Count zeros
# Sum only positive numbers




# 🔥 LEVEL 2 — Trend Logic

# Q11
# Print:
# UP
# DOWN
# SAME
# for every comparison.



# Q12
# Count total UP trends.
# Example:
# 2 → 5


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




# 🔥 LEVEL 4 — Thinking Upgrade




# Q31
# Find average of positive numbers only.




# Q32
# Find average of negative numbers only.






# Q33
# Count how many numbers are closer to zero.
# Condition:
# -5 closer than 20






# Q34
# Detect mountain pattern.
# Example:
# 1 2 3 2 1






# Q35
# Detect valley pattern.
# Example:
# 5 3 1 3 5




# Q36
# Count direction reversals.




# Q37
# Find largest UP jump.
# Example:
# 2 → 20
# Jump:
# 18



# Q38
# Find largest DOWN jump.


# Q39
# Print all local peaks.
# Example:
# 1 5 2
# Peak:
# 5




# Q40
# Print all local valleys.



# 🔥 LEVEL 5 — Real Thinking



# Q41
# Mini stock analyzer:
# Print:
# BUY signal if 3 UP trends
# SELL signal if 3 DOWN trends




# Q42
# Count market reversals.





# Q43
# Detect fake breakout.
# Example:
# UP → immediately DOWN





# Q44
# Detect strong bullish sequence.
# Condition:
# 5 consecutive UP




# Q45
# Detect strong bearish sequence.




# Q46
# Print trend percentage:
# UP %
# DOWN %




# Q47
# Find volatility.
# (big movement count)




# Q48
# Find most repeated trend.





# Q49
# Detect consolidation.
# Condition:
# numbers moving in small range.






# Q50
# Create mini trend dashboard:
# UP count
# DOWN count
# Positive count
# Negative count
# Highest
# Lowest
# Average



# Q3 — Password Strength Checker
# Check:
# uppercase
# lowercase
# numbers
# symbols
# minimum length
# Return:
# weak
# medium
# strong












# Q4 — Smart Calculator
# Menu-based:
# add
# subtract
# history
# clear history
# Store calculation history in list.















# Q5 — Number Pattern Analyzer
# Input list:
# [1,2,2,3,4,4,4,5]
# Find:
# duplicates
# unique numbers
# highest repeated number








# 🧠 LEVEL 2 — Real Thinking Starts
# Q6 — Library Management Mini System
# Features:
# add book
# remove book
# search book
# issue book
# return book
# Think about:
# availability tracking
# duplicate books








# Q9 — Quiz Game Engine
# Features:
# multiple questions
# score system
# correct/wrong tracking
# timer idea (optional)






# Q10 — Bank Interest Simulator
# Input:
# amount
# years
# interest rate
# Show yearly growth table.





# 🧠 LEVEL 3 — Builder Mindset
# Q11 — Chat System Simulation
# Two users can:
# send messages
# view chats
# delete chats
# Store chat history.






# Q14 — Hospital Queue System
# Patients:
# emergency priority
# token generation
# doctor assignment




# Q15 — Employee Salary System
# Calculate:
# bonus
# overtime
# tax deduction
# Generate salary slip.




# 🧠 LEVEL 4 — Quant/Trading Brain Start



# Q16 — Candle Analyzer
# Input candles:
# open high low close
# Detect:
# bullish
# bearish
# doji







# Q17 — Moving Average System
# Store prices and calculate:
# SMA
# EMA idea
# crossover detection





# Q18 — Trade Journal
# Store:
# entry
# exit
# profit/loss
# win rate





# Q19 — Risk Management Calculator
# Input:
# capital
# risk %
# stop loss
# Calculate:
# lot size
# max loss






# Q20 — Strategy Backtest Logic
# Simulate:
# buy signal
# sell signal
# total trades
# win ratio





# 🧠 LEVEL 5 — Architect Thinking
# Q21 — Mini Operating System Simulation
# Menu:
# file creation
# delete file
# rename file
# Simulate memory storage.






# Q22 — AI Chatbot Logic
# Keyword-based chatbot:
# greetings
# trading questions
# Python questions



# Q23 — E-commerce Cart System
# Features:
# add to cart
# remove item
# total price
# discount coupon








# Q24 — Social Media Feed Logic
# Users can:
# post
# like
# comment
# Store relationships.


# Q25 — Multiplayer Game Scoreboard
# Track:
# players
# kills
# deaths
# ranking



# 🧠 LEVEL 6 — HARD DESIGN THINKING
# Q26 — Traffic Signal Simulator

# Dynamic timing based on:

# vehicle count
# emergency vehicles




# Q27 — Smart File Organizer

# Separate files by:

# extension
# size
# date



# Q28 — Fake Stock Exchange

# Users:

# buy shares
# sell shares
# track portfolio




# Q29 — Crypto Wallet Simulation

# Features:

# send money
# receive money
# transaction history




# Q30 — Real-Time Notification System

# Simulate:

# unread messages
# notification queue
# priority notifications














# Q34 — Fraud Detection Logic

# Detect suspicious transactions:

# high amount
# repeated transfers
# unusual behavior








# Q35 — Autonomous Task Scheduler

# Tasks:

# priority
# deadlines
# execution queue

# Simulate CPU scheduler thinking.










# 🔹 LEVEL 1 — Control Flow (20 Qn)

# Focus:

# if-else
# loops
# nested conditions

# Example (no answer):

# 👉 Take numbers until -1
# 👉 Print only numbers divisible by 3 AND 5
# 👉 Stop if sum exceeds 200




# 🔹 LEVEL 2 — State Management (20 Qn)

# Focus:

# memory of previous values
# counters
# sequences

# Example:

# 👉 Take numbers
# 👉 Track:

# last number
# current trend (up/down)

# 👉 Print when trend changes





# 🔹 LEVEL 3 — Pattern Recognition (20 Qn)

# Focus:

# consecutive patterns
# sequence detection

# Example:

# 👉 Stop when pattern appears:

# even → odd → even → odd
# 🔹 LEVEL 4 — Event-Driven Logic (20 Qn)

# Focus:

# trigger-based actions

# Example:

# 👉 Take numbers continuously

# Rules:

# if 3 increases → print "BUY"
# if sudden drop > 20 → print "ALERT"
# 🔹 LEVEL 5 — Decision Systems (20 Qn)

# Focus:

# combining multiple conditions

# Example:

# 👉 Input: price, volume

# Rules:

# price ↑ AND volume ↑ → BUY
# price ↑ BUT volume ↓ → FAKE
# price ↓ → SELL
# 🧠 Hindi clarity







# 🧠 Start NOW (Level 2 — State Management)
# Q1
# 👉 Take numbers continuously
# Track:
# previous number
# 👉 Print:
# "UP" if current > previous
# "DOWN" if current < previous

# Stop when user enters -1









# Q2
# 👉 Take numbers
# 👉 Count how many times:
# number increased from previous




# Q3
# 👉 Take numbers
# 👉 Detect:
# 2 consecutive increases
# → print "TREND UP"




# Q4

# 👉 Take numbers

# 👉 Reset counter if:
# value drops



# ══════════════════════════════════════════════════════════════════════
# 🧠 P1 — Online Shopping Coupon System
# Difficulty: ⭐⭐☆☆☆

# Concepts:
# ✔ Dictionary Lookup
# ✔ Validation
# ✔ Percentage Calculation
# ✔ Conditional Logic

# ──────────────────────────────────────────────────────────────────────

# Dictionary:

# coupon = {
#     "SAVE10": 10,
#     "SAVE20": 20,
#     "VIP50": 50
# }

# Task:

# A customer is shopping online.

# 1. Ask the user to enter the total bill amount.
# 2. Ask the user to enter a coupon code.

# Rules:

# • If the coupon exists:
#     → Apply the discount.
#     → Print:
#         Original Bill
#         Discount %
#         Discount Amount
#         Final Bill

# • If the coupon does not exist:
#     → Print "Invalid Coupon"

# Bonus Challenge:
# • Prevent negative bill amounts.
# • Accept coupon codes in uppercase/lowercase.




# ══════════════════════════════════════════════════════════════════════
# 🧠 P7 — Login + OTP Verification
# Difficulty: ⭐⭐⭐⭐☆

# Concepts:
# ✔ Dictionary Lookup
# ✔ Random Number
# ✔ Multi-Step Validation

# ──────────────────────────────────────────────────────────────────────

# Dictionary

# users = {
#     "Bibek":"pass123"
# }

# Task

# Username

# ↓

# Password

# ↓

# Generate OTP

# ↓

# Ask OTP

# ↓

# Verify

# Rules

# Correct Username
# +
# Correct Password
# +
# Correct OTP

# ↓

# Login Successful

# Else

# ↓

# Login Failed

# Thinking Question:
# ❓Why should OTP be checked only AFTER password verification?
# ══════════════════════════════════════════════════════════════════════




# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📚 MODULE 1 — Anonymous Functions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Learn
# ✔ Lambda Function
# ✔ One-line Functions
# ✔ Sorting using lambda
# ✔ Lambda with map()
# ✔ Lambda with filter()

# Practice Questions

# Qn) Square every number using lambda



# Qn) Cube every number


# Qn) Sort tuple list using lambda
# tuples = (7,1,6,3,5,2,9,10,12,8)

# sorted_values = lambda x: sorted(x)
# print(sorted_values(tuples))




# ☐ Find longest word pass bhai

# ☐ Find shortest word pass bhai

# ☐ Multiply two numbers using lambda



# ☐ Even/Odd checker using lambda



# ☐ Maximum using lambda




# Mini Project
# 🟢 Student Ranking System



#     Student Ranking System

#   +-----------------------+
#   |   Student Database    | 
#   +-----------------------+
#               |
#               |
#   Read Student Information
#               |
#               ▼
#     +-------------------+
#     | Process Data      |
#     +-------------------+
#     | Total             |
#     | Percentage        |
#     | Grade             |
#     | Pass/Fail         |
#     +-------------------+
#               |
#               ▼
#    +----------------------+
#    | Ranking Algorithm    |
#    +----------------------+
#    | Sort Students        |
#    | Highest Marks        |
#    | Lowest Marks         |
#    +----------------------+
#               |
#               ▼
#     +--------------------+
#     | Display Report     |
#     +--------------------+
#     |
