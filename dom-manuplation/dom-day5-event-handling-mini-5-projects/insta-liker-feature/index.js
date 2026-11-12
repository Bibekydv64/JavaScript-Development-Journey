let img = document.querySelector('.img')
let lovelogo = document.querySelector('.lovelogo')



img.addEventListener('dblclick', ()=>{
    lovelogo.style.transform = 'translate(60%, -400%) scale(1.3)';
    lovelogo.style.opacity = '1'




    setTimeout(() => {
        lovelogo.style.opacity = '0';
    }, 700);

  setTimeout(() => {
        lovelogo.style.transform = 'translate(90%, -400%) scale(0)';
    }, 1000);
            
})







