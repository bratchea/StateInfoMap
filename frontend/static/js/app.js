document.addEventListener("click", (e) => {
    if (e.target.tagName == "path") {
        let content = e.target.dataset.name;
        window.location = `http://state-info-proj.uk.r.appspot.com/state/${content}`;
    } else {
        console.log("Not Clickable");
    }
});

document.addEventListener("mouseover", (e) => {
    if (e.target.tagName == "path") {
        let box = document.getElementById("info-box");
        let x = e.clientX + "px";
        let y = e.clientY + "px";
        let content = e.target.dataset.id;

        box.style.display = "flex";
        box.style.top = y;
        box.style.left = x;
        box.innerText = content;
    } else {
        document.getElementById("info-box").style.display = "none";
    }
});
