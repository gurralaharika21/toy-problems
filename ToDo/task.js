// deletion
var deletes = document.getElementsByClassName("deletes");
var i;
for (i = 0; i < deletes.length; i++) {
  deletes[i].onclick = function(ev) {
    ev.target.parentElement.remove()
    
  }
}
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    ev.target.classList.toggle('checked');
  }
}, false);

function AddTask() {
  var li = document.createElement("li");
  var inputValue = document.getElementById("tasks").value;
  var t = document.createTextNode(inputValue);
  li.appendChild(t);
  if (inputValue === '') {
    alert("please enter your list!");
  } else {
    document.getElementById("ul").appendChild(li);
  }
  document.getElementById("tasks").value = "";

  var span = document.createElement("SPAN");
  var txt = document.createTextNode("Delete");
  span.className = "deletes";
  span.appendChild(txt);
  li.appendChild(span);

  for (i = 0; i < deletes.length; i++) {
    
      deletes[i].onclick = function(ev) {
        ev.target.parentElement.remove()
      
    }
  }
}
