text = document.getElementById("name")



setInterval(function(){
   fetch("http://127.0.0.1:8000/api_test/")
    .then((data) => data.json())
    .then((t) => text.innerText = t["name"]) 
}, 100)