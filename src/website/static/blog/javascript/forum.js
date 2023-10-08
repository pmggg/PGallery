function addComment() {
    var table = document.getElementById("show");
  
    var name = document.getElementById("input-name").value;
    var email = document.getElementById("input-email").value;
    var comment = document.getElementById("input-comment").value;

    if(!name || !email || !comment){
        alert("Form Incomplete!");
        return;
    }

    var newUsername = table.insertRow(0);
    var newEmail = table.insertRow(1);
    var newComment = table.insertRow(2);
    var newLine1 = table.insertRow(3);

    var cell1 = newUsername.insertCell(0);
    var cell2 = newEmail.insertCell(0);
    var cell3 = newComment.insertCell(0);
    var cell4 = newLine1.insertCell(0);
    
    cell1.innerHTML = "Username: " + name;
    cell2.innerHTML = "e-mail: " + email[0] +"****";
    cell3.innerHTML = "Comment: " + comment;
    cell4.innerHTML = "______________________________________________________________________";

  }