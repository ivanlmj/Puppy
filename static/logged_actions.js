// Function executed as Callback, after finishing ajax* request (ajax.js)
//
// Definition: processes request data as JSON format, parsing elements for
// building <table> element (list of logged actions)
//

function buildTable(data) {
    var xhrResponse = JSON.parse(data);
    console.log(xhrResponse);

    var tableDiv = document.getElementById("actions");
    var table = document.createElement('TABLE');
    var header = document.createElement('TR');

    var id = document.createElement('TH');
    var action = document.createElement('TH');
    var command = document.createElement('TH');
    var run_by = document.createElement('TH');
    var run_time = document.createElement('TH');
    id.appendChild(document.createTextNode("Id"));
    action.appendChild(document.createTextNode("Action"));
    command.appendChild(document.createTextNode("Status"));
    run_by.appendChild(document.createTextNode("Run By"));
    run_time.appendChild(document.createTextNode("Run Time"));
    header.appendChild(id);
    header.appendChild(action);
    header.appendChild(command);
    header.appendChild(run_by);
    header.appendChild(run_time);
    table.appendChild(header);

    if (xhrResponse.length == 0) {
	var message = "No actions have been performed yet.";
        var tr = document.createElement('TR');
	var td = document.createElement('TD');
	td.colSpan = 5;
	td.appendChild(document.createTextNode(message));
	tr.appendChild(td);
	table.appendChild(tr);
    } else {
        for (var i = 0; i < xhrResponse.length; i++) {
            var tr = document.createElement('TR');
            table.appendChild(tr);
            for (var j = 0; j < 5; j++) {
                var td = document.createElement('TD');
                if ( j == 0 ) {
                    td.setAttribute("id", "id");
                }
                td.width = '75';
                td.appendChild(document.createTextNode(xhrResponse[i][j]));
                tr.appendChild(td);
            }
        }
    }
    tableDiv.appendChild(table);
};
