"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const downArrow = document.getElementById("down-arrow");

    downArrow.addEventListener("click", () => {
        document.querySelector("#nav").scrollIntoView({
            behavior: "smooth"
        })
    })
})
