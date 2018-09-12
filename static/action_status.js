function actionStatus() {

    // storing cookie data into variable
    var cookies = document.cookie.split(";");
    // cleaning specific cookie from browser, for it must only be present
    // after the execution of an action

    cookies.forEach(function(element) {
	console.log("Element:", element);

        data = element.split("=");
	cookie_key = data[0].trim()
	cookie_value = data[1].trim()

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

actionStatus();
