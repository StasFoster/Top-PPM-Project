btn1 = document.getElementById("s1");
title = document.getElementById("title");
disc = document.getElementById("disc");
console.log("_____2_____");
btn1.addEventListener("click", function(){
    fetch("http://127.0.0.1:8000/wiki/api")
        .then((response) => response.json())
        .then((data) => {
            title.innerText = data["title"];
            disc.innerText = data["disc"];
        })
        .catch((error) => console.error('Ошибка:', error));
})