btn1 = document.getElementById("s1")
title = document.getElementById("title")
disc = document.getElementById("disc")

btn1.getEventListener("click", function(){
    fetch("http://127.0.0.1:8000/wiki/api")
        .then((data) => data.json())
        .then((t) => title.innerText = t["title"])
        .then((t) => disc.innerText = t["disc"])
})