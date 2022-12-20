"use strict";

document.getElementById("down-arrow").addEventListener("click", () => {
    document.querySelector("main").scrollIntoView({
        behavior: "smooth"
    })
})
