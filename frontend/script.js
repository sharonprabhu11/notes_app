const API = "http://localhost:8000";

function register() {
  const username = document.getElementById("username").value;
  fetch(`${API}/register`, {
    method: "POST",
    body: JSON.stringify({ username }),
    headers: { "Content-Type": "application/json" }
  }).then(res => res.json()).then(data => alert(data.message));
}

function addNote() {
  const username = document.getElementById("username").value;
  const title = document.getElementById("title").value;
  const content = document.getElementById("content").value;
  fetch(`${API}/add_note`, {
    method: "POST",
    body: JSON.stringify({ username, title, content }),
    headers: { "Content-Type": "application/json" }
  }).then(res => res.json()).then(() => getNotes());
}

function getNotes() {
  const username = document.getElementById("username").value;
  fetch(`${API}/notes/${username}`)
    .then(res => res.json())
    .then(data => {
      const notesDiv = document.getElementById("notes");
      notesDiv.innerHTML = "";
      data.forEach(note => {
        const div = document.createElement("div");
        div.className = "note";
        div.innerHTML = `<h3>${note.title}</h3><p>${note.content}</p>
          <button onclick="deleteNote(${note.id})">Delete</button>`;
        notesDiv.appendChild(div);
      });
    });
}

function deleteNote(id) {
  fetch(`${API}/note/${id}`, { method: "DELETE" })
    .then(() => getNotes());
}
