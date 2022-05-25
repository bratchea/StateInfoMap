const allParagraphs = document.getElementsByTagName("p");

for (let i = 0; i < allParagraphs.length; i++) {
    allParagraphs[i].addEventListener("click", (e) => {
        let content = e.target.innerText;
        window.location = `http://state-info-proj.uk.r.appspot.com/state/${content}`;
    });

    allParagraphs[i].addEventListener("mouseover", (e) => {
        e.target.style = "cursor: pointer;"
    });
}
