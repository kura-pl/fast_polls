var counter = 2;
function add() {
    var paragraph = document.createElement("p");
    paragraph.innerHTML = "Choice " + (counter + 1) + ":";
    var new_choice = document.createElement("input");
    new_choice.setAttribute("type", "text");
    new_choice.setAttribute("size", "70");
    new_choice.setAttribute("name", "choice" + counter);
    new_choice.setAttribute("id", "choice" + counter);

    var form = document.getElementById("my_form");
    form.appendChild(paragraph);
    form.appendChild(new_choice);
    form.appendChild(document.createElement("br"));
    counter += 1;
    document.getElementById("count").setAttribute("value", counter);
}