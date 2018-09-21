// Function invoked as Callback through ajaxGet() from ajax.js,
// after finishing its request for a defined URI.
//
// It processes the returned data (JSON) from ajaxGet() request,
// parsing elements for building <select> element (list of actions).


function buildSelect(data) {
    var xhrResponse = JSON.parse(data);

    var actions = document.getElementById("action");
    for (i = 0; i < xhrResponse.length; i++) {
        var option = document.createElement('OPTION');
	// setting action id as value
	option.value = xhrResponse[i][0];
	// setting action name as text for the created option
	var text = document.createTextNode(xhrResponse[i][1]);
	option.appendChild(text);
	actions.appendChild(option);
    }

}
