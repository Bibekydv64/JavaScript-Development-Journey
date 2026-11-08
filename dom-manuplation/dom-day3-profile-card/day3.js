


let body = document.querySelector('body')
body.style.backgroundColor = 'black'
body.style.height = '100vh'
// body.style.display = 'flex'
// body.style.alignItems  = 'center'
// body.style.justifyContent = 'center'

let new_elements_insertion_div = document.createElement('div')

body.append(new_elements_insertion_div)


new_elements_insertion_div.style.height = '60vh'
new_elements_insertion_div.style.maxWidth = '400px'
new_elements_insertion_div.style.backgroundColor = 'white'
new_elements_insertion_div.style.borderRadius = '11px'



let heading_h1 = document.createElement('h1')
// console.log(heading_h1)
new_elements_insertion_div.append(heading_h1)
// console.log(new_elements_insertion_div)

heading_h1.innerHTML = 'Welcome'
heading_h1.style.padding = '20px'


let profile_img = document.createElement('img')
profile_img.src = 'bibek-profile.png'
profile_img.style.maxWidth = '40%'
profile_img.style.borderRadius = '50%'
profile_img.style.marginLeft = '100px'
new_elements_insertion_div.append(profile_img)



let heading_h2 = document.createElement('h2')

new_elements_insertion_div.append(heading_h2)

heading_h2.innerHTML = 'Bibek Kr.'

heading_h2.style.paddingLeft = '129px'
heading_h2.style.marginTop = '-1px'



let para = document.createElement('p')
para.innerHTML = 'Senior Developer'

new_elements_insertion_div.append(para)

para.style.paddingLeft = '129px'



// console.log(profile_img)
