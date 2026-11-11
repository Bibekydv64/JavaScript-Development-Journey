let btn2 = document.querySelector('btn-child1')
let btn = document.querySelector('.btn-child');
let h4_text = document.querySelector('.h4');




btn.addEventListener('click', ()=>{
    if(h4_text.textContent.toLowerCase() == 'stranger'){
        h4_text.textContent = 'Friends'
        h4_text.style.color = 'black'
        btn.innerHTML = 'Remove'
    }
    else{
        h4_text.textContent = 'Stranger'
        h4_text.style.color = 'rebeccapurple'
        btn.innerHTML = 'Add Friend'
        
    }
    
})


