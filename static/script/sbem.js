const todoInput = document.getElementById('todoInput');
const todoList = document.getElementById('todoList');
let emptyState = document.getElementById('empty-state');
let log = document.getElementById("logout");

log.addEventListener("click", function() {
    fetch("/logout", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        window.location.href = data.redirect;
    });
});

todoInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addTodo();
});

function addTodo() {
    const text = todoInput.value.trim();
    if (!text) return;

    if (emptyState) {
        emptyState.style.display = 'none';
    }

    const li = document.createElement('li');
    li.className = 'todo-item';
    li.innerHTML = `
        <input type="checkbox" onchange="toggleTodo(this)">
        <span class="todo-text">${text}</span>
        <button class="delete-btn" onclick="deleteTodo(this)">Elimina</button>
    `;

    todoList.appendChild(li);
    todoInput.value = '';

    fetch(`/add_todo`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ todo: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message !== 'Todo added successfully') {
            alert('Errore nell\'aggiunta dell\'attività.');
        }
    });
}

function toggleTodo(checkbox) {
    const li = checkbox.parentElement;
    li.classList.toggle('completed');

    const todoText = li.querySelector('.todo-text').innerText;
    const isChecked = checkbox.checked;

    fetch(`/checked`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            todo: todoText,
            is_checked: isChecked
        })
    });
}

function deleteTodo(btn) {
    btn.parentElement.remove();
    
    if (todoList.children.length === 0) {
        todoList.innerHTML = '<div class="empty-state">Nessuna attività. Inizia aggiungendone una! ✨</div>';
    }

    fetch(`/delete_todo`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ todo: btn.previousElementSibling.textContent })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message !== 'Todo deleted successfully') {
            alert('Errore nell\'eliminazione dell\'attività.');
        }
    });
}