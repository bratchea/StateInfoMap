document.addEventListener("click", (e) => {
    if (e.target.tagName == "path") {
        let content = e.target.dataset.name;
        window.location = `http://state-info-proj.uk.r.appspot.com/state/${content}`;
    } else {
        console.log("Not Clickable");
    }
});
