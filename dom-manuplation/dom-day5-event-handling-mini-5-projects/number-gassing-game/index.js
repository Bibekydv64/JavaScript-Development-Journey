let input = document.querySelector('.input')
let display = document.querySelector('.display')
let display1 = document.querySelector('.display1')
let form = document.querySelector('form')



form.addEventListener('click',(e)=>{
    let random_number = Math.floor(Math.random() * 40) + 1
    let array = []

    e.preventDefault()
    
    if(random_number > parseInt(input.value )){
        display.textContent = 'To high'
        display.style.color = 'white'
    }
    else if(random_number < parseInt(input.value)){
        display.textContent = 'To low'
        display.style.color = 'white'
    }
    else{
        display.textContent = 'Congracts'
        display.style.color = 'white'
    }

    array.push(input.value)
    display1.style.color = 'white'
    console.log(array)
    
    form.reset()
})


















