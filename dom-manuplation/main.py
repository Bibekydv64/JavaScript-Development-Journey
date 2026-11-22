# # 14-DAY JAVASCRIPT LOGIC & CONFIDENCE WORKBOOK

# **Mission:** Become an independent JavaScript developer who can look at any UI and understand the logic behind it.

# **Duration:** 14 Days  
# **Daily practice:** 60–90 minutes  
# **Technology:** HTML + CSS + Vanilla JavaScript  
# **Focus:** DOM, Events, Conditions, Arrays, Objects, State, Functions and UI Logic.

# ==================================================
# MY DAILY DEVELOPMENT RULES
# ==================================================

# 1. No copying code from YouTube or tutorials.
# 2. Understand the UI before writing code.
# 3. Write the logic in plain English first.
# 4. Build the HTML structure.
# 5. Write JavaScript independently.
# 6. Test normal and unusual user actions.
# 7. Ask for hints when stuck, not the full solution.
# 8. Do not move to the next day until I understand the current concepts.

# ==================================================
# PHASE 01 — BASIC LOGIC DEVELOPMENT
# DAYS 01–04
# ==================================================

# DAY 01 — COUNTER & BUTTON LOGIC

# Main concepts:
# - Variables
# - DOM selection
# - Click events
# - Conditions
# - DOM updates

# Exercises:

# 1. Basic Counter — Increase the number by clicking a button.
------------------------------------------------------Question1-----------------------------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercises</title>
    <link rel="stylesheet" href="index.css">
    <style>
    body{
    background-color: black;
}
.container{
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.display{
    font-size: 2.2rem;
    font-weight: bolder;
    text-align: center;
    margin: 20px 0px;
    color: whitesmoke;
}
.display1{
    color: whitesmoke;
    text-align: center;
    font-size: 1.2rem;
    font-weight: bolder;
}


.btn{
    width: 120px;
    height: 40px;
    font-weight: bolder;
    font-size: 1rem;
    margin: 15px;
    cursor: pointer;
}

    </style>
    </style>
</head>
<body>
    
    <div class="container">
        <div class="another-container">
           <h1 style="color: whitesmoke;">WELCOME TO THIS EXERCISES</h1>
           <p class="display">1</p>
           
           <div class="btn-container">
            <button class="btn btn1" type="button">Increment</button>
            <button class="btn btn2" type="button">Reset</button>
            <button class="btn btn3" type="button">Decrement</button>
           </div>

        </div>
    </div>

    <script >let btn1 = document.querySelector('.btn1')
let btn2 = document.querySelector('.btn2')
let btn3 = document.querySelector('.btn3')
let display = document.querySelector('.display')



btn1.addEventListener('click',function(){
    increment = Number(display.textContent)
    display.textContent = increment +1
})



btn2.addEventListener('click',function(){
    display.textContent = '0'
})




btn3.addEventListener('click',function(){
    increment = Number(display.textContent)
    display.textContent = increment -1
})
</script>
</body>
</html>
----------------------------------------------------------------------------Question2--------------------------------------------------------------------------------------------------
# 4. Negative Number Prevention — Do not allow the counter below zero.
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercises</title>
    <link rel="stylesheet" href="index.css">
    <style>
        *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    background-color: black;
}
.container{
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.display{
    font-size: 2.2rem;
    font-weight: bolder;
    text-align: center;
    margin: 20px 0px;
    color: whitesmoke;
}
.display1{
    color: whitesmoke;
    text-align: center;
    font-size: 1.2rem;
    font-weight: bolder;
}


.btn{
    width: 120px;
    height: 40px;
    font-weight: bolder;
    font-size: 1rem;
    margin: 15px;
    cursor: pointer;
}

    </style>
</head>
<body>
    
    <div class="container">
        <div class="another-container">
           <h1 style="color: whitesmoke;">WELCOME TO THIS EXERCISES</h1>
           <p class="display">1</p>
           <p class="display1"></p>
           
           <div class="btn-container">
            <button class="btn btn1" type="button">Increment</button>
            <button class="btn btn2" type="button">Reset</button>
            <button class="btn btn3" type="button">Decrement</button>
           </div>

        </div>
    </div>

    <script src="index.js">
        let display = document.querySelector('.display')
let display1 = document.querySelector('.display1')
let btn1 = document.querySelector('.btn1')
let btn2 = document.querySelector('.btn2')
let btn3 = document.querySelector('.btn3')
// --------------------btn1---------------------------------------
let btn1_event = function(){
    let number = Number(display.textContent)

        display.textContent = number +1

}
btn1.addEventListener('click',btn1_event)

//-----------------btn2---------------------------------------------
        let btn2_event = function(){
            display.textContent = '0'
        
        }
        btn2.addEventListener('click', btn2_event)

        let btn3_event = function(){
            let number = Number(display.textContent)
                if(number < 0){
                    display1.textContent = 'beta 0 se niche nahi jayega'
                    display.textContent = '0'
                
            }
            else{
                display.textContent = number - 1
            }
        
        }

        btn3.addEventListener('click',btn3_event)


    </script>
</body>
</html>
# 5. Step Counter — Increase or decrease by 5 instead of 1.
# 6. Maximum Limit — Stop increasing after reaching 100.

# DAY 02 — PASSWORD & VISIBILITY LOGIC

# Main concepts:
# - Boolean
# - Conditional statements
# - Toggle logic
# - Input properties

# Exercises:

# 1. Password Visibility — Show and hide a password.
# 2. Confirm Password — Check whether two passwords match.
# 3. Password Length — Require at least 8 characters.
# 4. Password Strength — Display weak, medium or strong.
# 5. Clear Input — Clear the password field with a button.
# 6. Show/Hide Multiple Fields — Control two password fields independently.

# DAY 03 — LIVE TEXT CONTROLLER

# Main concepts:
# - Input events
# - String methods
# - String length
# - Dynamic DOM updates

# Exercises:

# 1. Live Character Counter — Display the number of typed characters.
# 2. Maximum Character Limit — Stop accepting input after 100 characters.
# 3. Remaining Characters — Show how many characters remain.
# 4. Live Text Preview — Display typed text in another element.
# 5. Uppercase Converter — Convert text to uppercase.
# 6. Word Counter — Count words in a text area.

# DAY 04 — LIKE & FOLLOW SYSTEM

# Main concepts:
# - Boolean state
# - Toggle
# - Conditional rendering
# - Dynamic text

# Exercises:

# 1. Like Button — Like and unlike a post.
# 2. Like Counter — Increase and decrease likes.
# 3. Follow Button — Toggle Follow and Following.
# 4. Bookmark Button — Save or remove a bookmark.
# 5. Notification Toggle — Turn notifications on or off.
# 6. Theme Switcher — Toggle light and dark mode.

# ==================================================
# PHASE 02 — INTERACTIVE UI LOGIC
# DAYS 05–08
# ==================================================

# DAY 05 — ACCORDION COMPONENT

# Main concepts:
# - Events
# - Conditional visibility
# - classList
# - State

# Exercises:

# 1. Single Accordion — Open and close one section.
# 2. Multiple Accordion — Control multiple sections.
# 3. Exclusive Accordion — Only one section can remain open.
# 4. Expand All — Open all sections.
# 5. Collapse All — Close all sections.
# 6. Dynamic Arrow — Change the arrow when a section opens.

# DAY 06 — TAB SWITCHER

# Main concepts:
# - Arrays
# - Active state
# - DOM manipulation
# - Class management

# Exercises:

# 1. Basic Tabs — Switch between three content sections.
# 2. Active Tab — Highlight the selected tab.
# 3. Four-Tab Dashboard — Display different content.
# 4. Profile Tabs — Switch between Posts, About and Photos.
# 5. Tab Counter — Display the number of times a tab is selected.
# 6. Reset Tabs — Return to the first tab.

# DAY 07 — LIVE SEARCH FILTER

# Main concepts:
# - Arrays
# - filter()
# - includes()
# - toLowerCase()
# - Dynamic rendering

# Exercises:

# 1. Name Search — Search names from an array.
# 2. Case-Insensitive Search — Search without worrying about uppercase.
# 3. Empty Search — Display all items when the input is empty.
# 4. No Results — Display a message when nothing matches.
# 5. Product Search — Filter products by name.
# 6. Category Filter — Filter products by selected category.

# DAY 08 — FORM VALIDATION

# Main concepts:
# - Input values
# - Conditions
# - Functions
# - Form events
# - Error messages

# Exercises:

# 1. Empty Field Validation — Reject empty input.
# 2. Email Validation — Check basic email format.
# 3. Password Validation — Check minimum password length.
# 4. Confirm Password — Check whether passwords match.
# 5. Error Messages — Display errors under individual inputs.
# 6. Success Message — Display a success message when all fields are valid.

# ==================================================
# PHASE 03 — DATA & APPLICATION LOGIC
# DAYS 09–11
# ==================================================

# DAY 09 — SHOPPING QUANTITY CONTROLLER

# Main concepts:
# - Variables
# - Conditions
# - Calculations
# - Functions

# Exercises:

# 1. Quantity Increase — Increase product quantity.
# 2. Quantity Decrease — Decrease product quantity.
# 3. Minimum Quantity — Prevent quantity below one.
# 4. Maximum Quantity — Limit quantity to ten.
# 5. Price Calculator — Calculate quantity × price.
# 6. Dynamic Total — Update total price whenever quantity changes.

# DAY 10 — MINI EXPENSE TRACKER

# Main concepts:
# - Arrays
# - Objects
# - push()
# - reduce()
# - DOM rendering

# Exercises:

# 1. Add Expense — Add an expense to an array.
# 2. Display Expenses — Render expenses in a list.
# 3. Total Expense — Calculate the total.
# 4. Delete Expense — Remove an expense.
# 5. Category Expense — Categorize expenses.
# 6. Highest Expense — Find the most expensive transaction.
# 7. Empty State — Show a message when there are no expenses.

# DAY 11 — QUIZ APPLICATION

# Main concepts:
# - Arrays of objects
# - Index management
# - Conditions
# - Score calculation
# - Application state

# Exercises:

# 1. Display Question — Show one question at a time.
# 2. Select Answer — Allow users to select an option.
# 3. Check Answer — Determine whether the answer is correct.
# 4. Score Counter — Increase score for correct answers.
# 5. Next Question — Move to the next question.
# 6. Final Result — Display the final score.
# 7. Restart Quiz — Reset the quiz to its initial state.

# ==================================================
# PHASE 04 — INDEPENDENT DEVELOPER THINKING
# DAYS 12–14
# ==================================================

# DAY 12 — DYNAMIC SEARCH SUGGESTIONS

# Main concepts:
# - Arrays
# - filter()
# - Input events
# - Dynamic rendering
# - Conditional UI

# Exercises:

# 1. Search Suggestions — Display matching names while typing.
# 2. No Suggestions — Display an appropriate empty message.
# 3. Click Suggestion — Put the selected result inside the input.
# 4. Clear Search — Remove input and suggestions.
# 5. Search Highlight — Highlight matching text.
# 6. Maximum Suggestions — Display only five suggestions.

# DAY 13 — MINI SHOPPING CART

# Main concepts:
# - Arrays of objects
# - Object properties
# - find()
# - filter()
# - reduce()
# - State management

# Exercises:

# 1. Product List — Display products from an array.
# 2. Add to Cart — Add a selected product.
# 3. Duplicate Product — Increase quantity instead of adding duplicates.
# 4. Remove Product — Delete an item from the cart.
# 5. Cart Quantity — Display total item quantity.
# 6. Cart Total — Calculate the total price.
# 7. Empty Cart — Display a message when the cart is empty.

# DAY 14 — MINI TASK MANAGEMENT DASHBOARD

# Main concepts:
# - CRUD operations
# - Arrays and objects
# - State management
# - Functions
# - DOM rendering
# - Conditional logic

# Exercises:

# 1. Add Task — Create a new task.
# 2. Display Tasks — Render all tasks.
# 3. Complete Task — Mark a task as completed.
# 4. Edit Task — Update an existing task.
# 5. Delete Task — Remove a task.
# 6. Filter Tasks — Show All, Pending and Completed.
# 7. Task Statistics — Display total, completed and pending tasks.

# ==================================================
# THE MOST IMPORTANT SKILL: UI TO LOGIC
# ==================================================

# Whenever I see a UI, I must answer these questions BEFORE coding:

# 1. COMPONENTS
#    What elements are present in this interface?

# 2. USER ACTIONS
#    What can the user click, type, select or submit?

# 3. EVENTS
#    Which event should handle each action?

# 4. STATE
#    What information must JavaScript remember?

# 5. CONDITIONS
#    What rules determine the application's behaviour?

# 6. DATA
#    Do I need variables, arrays or objects?

# 7. OUTPUT
#    Which elements must change on the screen?

# 8. FUNCTIONS
#    Can I separate the logic into reusable functions?

# 9. TESTING
#    What happens with empty input, repeated clicks or invalid data?

# ==================================================
# MY DAILY COMPLETION CHECKLIST
# ==================================================

# [ ] I understood the UI.
# [ ] I identified all components.
# [ ] I identified user actions.
# [ ] I wrote the logic in plain English.
# [ ] I identified the required variables and data.
# [ ] I implemented the JavaScript independently.
# [ ] I tested all exercises.
# [ ] I can explain WHY my code works.
# [ ] I can rebuild the component without looking at my previous code.

# ==================================================
# FINAL MISSION
# ==================================================

# After 14 days, I should be able to:

# - Look at a UI and identify its components.
# - Understand the sequence of user interactions.
# - Convert user actions into JavaScript events.
# - Identify the required state and data structures.
# - Write conditions without randomly guessing.
# - Break complex behaviour into smaller functions.
# - Build small real-world components independently.
# - Debug my own JavaScript logic.

# **MY PRINCIPLE:**

# I am not learning JavaScript to memorize syntax.

# I am learning JavaScript to develop the ability to THINK, DESIGN and IMPLEMENT LOGIC independently.

# ONE DAY AT A TIME. ONE CONCEPT AT A TIME. NO SHORTCUTS.

# — 14-Day JavaScript Confidence Challenge














