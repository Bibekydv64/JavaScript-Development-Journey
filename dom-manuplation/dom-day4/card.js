// let html = document.querySelector('html')
let body = document.querySelector('body')
body.style.backgroundColor = 'black'
body.style.height = '100vh'
body.style.width = '100%'





let parent_div = document.createElement('div')
parent_div.classList.add('container')


body.append(parent_div)
let parent_div_class = document.querySelector('.container')
parent_div_class.style.height = '60vh'
parent_div_class.style.maxWidth = '600px'
parent_div_class.style.backgroundColor = 'white'
parent_div_class.style.borderRadius = '13px'




let para = document.createElement('p')
para.classList.add('para-text')
parent_div_class.append(para)
let para_class = document.querySelector('.para-text')
para_class.style.color = 'black'
para_class.style.paddingTop = '60px'
para_class.style.paddingLeft = '10px'
para_class.style.fontSize = '2rem'

para_class.innerHTML = 'premium'





let para1 = document.createElement('strike')
para1.classList.add('para-text1')
parent_div_class.append(para1)
let para_class1 = document.querySelector('.para-text1')
para_class1.style.color = 'black'
para_class1.style.fontSize = '1.2rem'
para_class1.style.paddingLeft = '10px'
para_class1.style.marginTop = '-20px'
para_class1.style.display = 'block'
para_class1.innerHTML = '$349.99'

let para2 = document.createElement('span')
para2.classList.add('para-text2')
parent_div_class.append(para2)
let para_class2 = document.querySelector('.para-text2')
para_class2.style.color = 'black'
para_class2.style.fontSize = '1.2rem'
para_class2.style.paddingLeft = '10px'
// para_class2.style.marginTop = '-5px'
para_class2.innerHTML = '$249.99'



let img = document.createElement('img')
img.classList.add('imgs')
img.src = 'headphone.png'
img.style.width = '100px'
img.style.paddingLeft = '200px'
img.style.display = 'block'
para_class1.style.marginTop = '-20px'
parent_div_class.append(img)




let para3 = document.createElement('p')
para3.classList.add('para-text3')
parent_div_class.append(para3)
let para_class3 = document.querySelector('.para-text3')
para_class3.style.color = 'black'
para_class3.style.fontSize = '1.2rem'
para_class3.style.paddingLeft = '190px'
para_class3.innerHTML = 'Free Shipping'













































