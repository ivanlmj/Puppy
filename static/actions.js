// Function executed as Callback, after finishing ajax* request (ajax.js)
//
// Definition: processes request data as JSON format, parsing elements for
// building <select> element (list actions)
//

function buildSelect(data) {
    var xhrResponse = JSON.parse(data);

    var actions = document.getElementById("action");
    for (i = 0; i < xhrResponse.length; i++) {
        var option = document.createElement('OPTION');
	option.value = xhrResponse[i][1];
	var text = document.createTextNode(xhrResponse[i][1]);
	option.appendChild(text);
	actions.appendChild(option);
    }

}
