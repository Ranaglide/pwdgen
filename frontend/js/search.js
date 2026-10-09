const input = document.getElementById("search-input")
const find_btn = document.getElementById("find")


const search_by_query = (query) => {
    const params = new URLSearchParams();
    params.append('q', query);
    fetch(`${host}/get-songs?${params.toString()}`, {
        method: "GET", headers: {
            "content-type": "Application/json"
        }
    }).then(r => r.json()).then(r => {
        if (r.success) {
            const results = document.querySelector(".search__results")
            results.innerHTML = ``
            r.results.forEach(res => {
                result = document.createElement("div")
                result.classList.add("result")
                result.innerHTML = `<button class="result__button">Create password</button><iframe class="result" frameborder="0" allow="clipboard-write"style="width: 100%;height: 100%;border: none;"
                src="https://music.yandex.ru/iframe/album/${res.album_id}/track/${res.id}">Слушайте
                <a href="https://music.yandex.ru/album/${res.album_id}/track/${res.id}?utm_source=web&utm_medium=copy_link">
                ${res.title}</a> — <a href="https://music.yandex.ru/artist/${res.artist_id}">${res.artists}</a> на Яндекс Музыке</iframe>`

                result.querySelector(".result__button").onclick = () => {
                    alert(res.title)
                }
                results.appendChild(result)
            });
        } else {
            alert(r.message)
        }
    })
}


find_btn.addEventListener("click", (e) => {
    e.preventDefault()
    search_by_query(input.value)
    input.value = ""
})