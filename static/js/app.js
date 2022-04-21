document.addEventListener("click", (e) => {
    if (e.target.tagName == "path") {
        let content = e.target.dataset.name;
        console.log(content);
    } else {
        console.log("blah");
    }
});
