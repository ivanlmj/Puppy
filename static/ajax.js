function ajaxGet(path, cbFunction) {

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
	    cbFunction(xhttp.responseText);
        }
    };
    xhttp.open('GET', path, true );
    xhttp.send();

};
