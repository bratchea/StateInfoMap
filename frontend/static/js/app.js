document.addEventListener("click", (e) => {
    if (e.target.tagName == "path") {
        let content = e.target.dataset.name;
        window.location = `http://localhost:5000/us/state/${content}`;
    } else {
        console.log("blah");
    }
});
