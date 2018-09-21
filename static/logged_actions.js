// Function invoked as Callback through ajaxGet() from ajax.js,
// after finishing its request for a defined URI.
//
// It processes the returned data (JSON) from ajaxGet() request,
// parsing elements for building <table> element (list of logged actions).


function buildTable(data) {
    var xhrResponse = JSON.parse(data);

    // creating table head
    var tableHead = document.getElementById("t_head");

    // creating header row
    var header = document.createElement('TR');

    // creating headers and texts for header row
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

    // building header row
    header.appendChild(id);
    header.appendChild(action);
    header.appendChild(command);
    header.appendChild(run_by);
    header.appendChild(run_time);

    // populating table head with header row
    tableHead.appendChild(header);

    // creating table body
    var tableBody = document.getElementById("t_body");

    if (xhrResponse.length == 0) {
	// If no response from AJAX request, build single row
	// with the following message.
	var message = "No actions have been performed yet.";
        var tr = document.createElement('TR');
	var td = document.createElement('TD');
	td.colSpan = 5;
	td.appendChild(document.createTextNode(message));
	tr.appendChild(td);
	tableBody.appendChild(tr);
    } else {
	// parsing data (JSON) from ajaxGet() request
        for (var i = 0; i < xhrResponse.length; i++) {
	    // creating row for each logged action
            var tr = document.createElement('TR');
            for (var j = 0; j < 5; j++) {
		// building logged action row
                var td = document.createElement('TD');
                if ( j == 0 ) {
		    // setting id for table cell,
		    // for the first slice of each logged action row
                    td.setAttribute("id", "id");
                }
                td.width = '75';
                td.appendChild(document.createTextNode(xhrResponse[i][j]));
		// building logged action row
                tr.appendChild(td);
		// populating table body with logged action row
		tableBody.appendChild(tr);
            }
        }
    }

};
