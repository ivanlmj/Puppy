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


function ajaxPost(path, name, action) {

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
	    alert("Request OK!");
        } else {
	    alert("Request NOK...")
	}
    };
    xhttp.open('POST', path, true );
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(`name=${name}&action=${action}`);

};
