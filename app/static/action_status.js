// Function invoked at every requested performed to /panel.
//
// It loops over the cookies of the page.
//
// On each iteration, each cookie element is splitted,
// generating a cookie_key and a cookie value: the cookie_key
// is verified via switch/case and an alert is displayed
// for the user, depending of its cookie_value.
//
// Independently of the cookie_value, the cookie_key is expired,
// in order to avoid the alert behaviour defined below when accessing
// /panel, after running, creating, updating or deleting any Action,
// performed via the URI below:
//
//     /panel/action/run
//     /panel/action/create
//     /panel/action/update
//     /panel/action/delete


function actionStatus() {

    // Storing cookie data into variable.
    // Cookies are set on demand, depending on /path/action/<option> request.
    var cookies = document.cookie.split(";");

    // Checking each cookie found for the page.
    cookies.forEach(function(element) {

        data = element.split("=");
	cookie_key = data[0].trim()
	cookie_value = data[1].trim()

	// Each cookie_key is evaluated; its cookie_value
	// is verified and the specific cookie is cleaned.
	switch (cookie_key) {
	    case "run_status":
		if (cookie_value == "0") {
	            alert("INFO: Action successfully EXECUTED!");
		} else {
                    alert("INFO: Failure on EXECUTING action.");
		}
		document.cookie = "run_status=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
		break;
	    case "create_status":
		if (cookie_value == "0") {
	            alert("INFO: Action successfully CREATED!");
		} else {
                    alert("INFO: Failure on CREATING action.");
		}
		document.cookie = "create_status=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
		break;
	    case "update_status":
		if (cookie_value == "0") {
	            alert("INFO: Action successfully UPDATED!");
		} else {
                    alert("INFO: Failure on UPDATING action.");
		}
		document.cookie = "update_status=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
		break;
	    case "delete_status":
		if (cookie_value == "0") {
	            alert("INFO: Action successfully DELETED!");
		} else {
                    alert("INFO: Failure on DELETING action.");
		}
		document.cookie = "delete_status=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
		break;
	}

    });
    
}
