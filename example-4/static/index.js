function ajax(type, url, data, callback) {

    var xhr = new XMLHttpRequest();

    xhr.open(type, url);
    xhr.setRequestHeader("Content-Type","raw; charset=UTF-8");

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            callback(xhr.responseText);

        }
    };

    xhr.send(data);
}

function display_output(output) {
    document.getElementById("output").innerHTML = output;
}

var onLoad = function() {
    ajax("GET", "/new_game", null, display_output);

    document.getElementById("command-form").onsubmit = function(e) {
        e.preventDefault();

        var input = document.getElementById("command").value;
        document.getElementById("command").value = "";

        ajax("POST", "/input", input, display_output);

        return false;
    }
};

window.onload = onLoad;