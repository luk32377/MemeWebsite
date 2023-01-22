
daim = document.getElementById("imspot");

function fetchmeme() {
	const xhttp = new XMLHttpRequest();
	xhttp.open("GET", "http://localhost:5000/request", true);
	xhttp.onload = function() {
		daim.src = this.responseText;
	}
	xhttp.send();
}

fetchmeme();

document.onkeydown = function(e) {
	fetchmeme();
}
