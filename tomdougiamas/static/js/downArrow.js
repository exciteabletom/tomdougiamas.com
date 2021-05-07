"use strict";

document.getElementById("down-arrow").addEventListener("click", () => {
    document.querySelector("#nav").scrollIntoView({
        behavior: "smooth"
    })
})
