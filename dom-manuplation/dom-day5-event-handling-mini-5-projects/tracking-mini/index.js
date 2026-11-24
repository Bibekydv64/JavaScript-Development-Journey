let input = document.querySelector('.input1');
let display = document.querySelector('.container1 span');
let display1 = document.querySelector('.container2 span');
let display2 = document.querySelector('.container3 span');
let display3 = document.querySelector('.container4 span');
let display4 = document.querySelector('.container5 span');


input.addEventListener('input',()=>{
    display.textContent = input.value.toUpperCase();
    display1.textContent = input.value.toLowerCase()
    display2.textContent = input.value.toLowerCase().split(" ").map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(" ");

})






