let input = document.querySelector('#input')
let display = document.querySelector('.p')

input.addEventListener('input',(event)=>{
    let num = event.target.value

    if(num.length == 4 ){
        display.textContent = `+977-${num}`
    }
})

