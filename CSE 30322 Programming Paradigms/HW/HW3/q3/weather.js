function toCelsius() {

	// grabs the input from the user
	let input = document.getElementById("temperature").value;
	// converts the temperature to C
	let celsius = (input - 32) * 5 / 9;

	document.getElementById("result-parent").firstChild.nodeValue = "The Temperature in Celsius is ";
	document.getElementById("result").innerText = celsius;

	document.getElementById("result-parent").style.visibility = "visible";
	document.getElementById("result-parent").style.color = "black";
	document.getElementById("result-parent").style.fontWeight = "400";

	// If not a number, change styles and text to error message.
	if (isNaN(celsius)) {
		document.getElementById("result-parent").firstChild.nodeValue = "Please input a valid number!";
		document.getElementById("result").innerText = '';
		document.getElementById("result-parent").style.color = "red";
		document.getElementById("result-parent").style.fontWeight = "bold";
	}

}