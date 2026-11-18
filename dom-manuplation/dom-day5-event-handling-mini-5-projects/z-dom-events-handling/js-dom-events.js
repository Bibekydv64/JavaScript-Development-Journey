let form = document.querySelector('form')
let btn = document.querySelector('.input')


form.addEventListener('submit',clickfxn)

function clickfxn(event){

    event.preventDefault()
    
    let div_container = document.createElement('div')
    div_container.classList.add('container')

    let img = document.createElement('img')
    img.classList.add('img')
    img.setAttribute('src', `${form[0].value}`)


    let h3 = document.createElement('h3')
    h3.classList.add('text-name')
    h3.textContent = `${form[1].value}`

    let p = document.createElement('p')
    p.classList.add('text-skill')


    let h2 = document.createElement('h2')
    h2.classList.add('text-age')
    h2.textContent = `${form[2].value} Years`

    let anotherP = document.createElement('p')
    anotherP.classList.add('para')
    p.textContent = `${form[3].value}`

    let para = document.createElement('p')
    para.classList.add('para')
    para.textContent = `${form[4].value}`

    let body = document.querySelector('body')
    body.append(div_container)


    div_container.append(img)

    div_container.append(h3)

    div_container.append(p)
    div_container.append(h2)
    div_container.append(anotherP)
    div_container.append(para)
form.reset()
}



