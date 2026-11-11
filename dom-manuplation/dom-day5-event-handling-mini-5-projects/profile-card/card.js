
let btn = document.querySelector('.btn-child');
let h4_text = document.querySelector('.h4');




btn.addEventListener('click', ()=>{
    if(h4_text.textContent.toLowerCase() == 'stranger'){
        h4_text.textContent = 'Python Developer'
    }
    else{
        h4_text.textContent = 'Stranger'
    }
    
})