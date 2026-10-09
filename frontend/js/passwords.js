const passwords__list = document.querySelector(".passwords__list")

document.onload = () => {

}

const get_passwords = () => {
    fetch(`${host}/get-passwords`, {
        method: "GET", headers: {
            "content-type": "Application/json"
        }
    }).then(r => r.json()).then(r => {
        if (r.success) {
            const list = document.querySelector(".passwords__list")
            list.innerHTML = ``
            r.results.forEach(res => {
                result = document.createElement("div")
                result.classList.add("password__item")
                result.innerHTML = ``

               
                list.appendChild(result)
            });
        } else {
            alert(r.message)
        }
    })
}