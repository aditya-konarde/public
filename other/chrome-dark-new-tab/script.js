var color = document.documentElement.style.backgroundColor;
document.documentElement.style.backgroundColor = "black";
var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.target.nodeName == "BODY") {
            observer.disconnect();
            document.documentElement.style.backgroundColor = color || "";
        }
    });
});
observer.observe(document, { childList: true, subtree: true });
