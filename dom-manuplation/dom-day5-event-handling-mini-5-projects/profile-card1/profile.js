let btn = document.querySelector('.btn')
btn.addEventListener('click', ()=>{
    if(btn.textContent.trim() == '+Add Friend'){
        btn.textContent = 'Remove Friend'
        btn.style.boxShadow = '0px 10px 10px #354de8'
    }
    else{
        btn.textContent = '+Add Friend'
        btn.style.boxShadow = '10px 0px 10px #354de8'
    }
})




