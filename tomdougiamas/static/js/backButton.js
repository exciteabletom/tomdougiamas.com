"use strict";

document.getElementById("back-button").addEventListener("click", () => {
		// Create a back button that never takes the user away from our site.
		let curPath = window.location.pathname;

		let pathArr = curPath.split("/");
		pathArr = pathArr.slice(0, -2) // remove last two elements from array

		let newLoc = pathArr.join("/");

		if (newLoc === "") {
			newLoc = "/#nav";
		}

		window.location = newLoc;
	}
)