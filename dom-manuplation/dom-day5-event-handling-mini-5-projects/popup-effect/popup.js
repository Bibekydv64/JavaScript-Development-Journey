
let btn = document.querySelector('.button')
let mainContainer = document.querySelector('.container')
let icon = document.querySelector('.cross-icon')



function popup(){
    mainContainer.style.display = 'block'
}
btn.addEventListener('click', popup)






function closePopup(){
    mainContainer.style.display = 'none'
}

icon.addEventListener('click',closePopup)


