


// let new_elements = document.createElement('div.div')
// // new_elements.innerHTML = 'hey bibek beta'
// // Node.append(new_elements)
// let selector = document.querySelector('.div')
// selector.innerHTML = 'ME box 4'
// console.log(new_elements)



let parent = document.querySelector('.container')
let child = document.querySelectorAll('.p')

console.log(child)

let insert_new_elements = document.createElement('p')
insert_new_elements.innerHTML = 'Me box 4'
insert_new_elements.classList.add('p')

parent.append(insert_new_elements)


insert_new_elements.addEventListener('click', foreach(()=>{
    console.log('welcome to new elements')
    child.style.backgroundColor = 'green'
    
}))

 






parent.style.height = '400px'

// console.log(parent)


