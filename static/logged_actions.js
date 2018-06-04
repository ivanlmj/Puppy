function buildTable(data) {
    var xhrResponse = JSON.parse(data);

    var tableDiv = document.getElementById("actions");
    var table = document.createElement('TABLE');
    var header = document.createElement('TR');

    var id = document.createElement('TH');
    var name = document.createElement('TH');
    var command = document.createElement('TH');
    var create_time = document.createElement('TH');
    var update_time = document.createElement('TH');
    id.appendChild(document.createTextNode("Id"));
    name.appendChild(document.createTextNode("Name"));
    command.appendChild(document.createTextNode("Command"));
    create_time.appendChild(document.createTextNode("Create Time"));
    update_time.appendChild(document.createTextNode("Update Time"));
    header.appendChild(id);
    header.appendChild(name);
    header.appendChild(command);
    header.appendChild(create_time);
    header.appendChild(update_time);
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
