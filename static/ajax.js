function ajaxRequest(path) {

    var xhttp = new XMLHttpRequest();

    try {
	xhttp.onreadystatechange = function () {
	    if (this.readyState == 4 && this.status == 200) {
	        return JSON.parse(xhttp.responseText);
	    }
	};
	xhttp.open('GET', path );
	xhttp.send();
    } catch (err) {
	console.log(`Error on XHR request: ${err.message}`);
    }

};
