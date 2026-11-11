let btn1 = document.querySelector('.btn-child1')
let btn = document.querySelector('.btn-child');
let h4_text = document.querySelector('.h4');




btn.addEventListener('click', ()=>{
        h4_text.textContent = 'Friends'
        h4_text.style.color = 'black'
})


btn1.addEventListener('click', ()=>{        
        h4_text.textContent = 'Stranger'
        h4_text.style.color = 'rebeccapurple'  
})

