function actionStatus() {

    // storing cookie data into variable
    var cookies = document.cookie.split(";");
    // cleaning specific cookie from browser, for it must only be present
    // after the execution of an action
    document.cookie = "last_action_status=; expires=Thu, 01 Jan 1970 00:00:00 UTC";

    cookies.forEach(function(element) {
	console.log("Element:", element);
        data = element.split("=");
	if (data[0].trim() == "last_action_status") {
	    if (data[1] == "0") {
	        alert("INFO: Action successfully executed!");
	    } else {
                alert("INFO: Action presented ERROR on its execution.");
	    }
	}
    });
    
}

actionStatus();
