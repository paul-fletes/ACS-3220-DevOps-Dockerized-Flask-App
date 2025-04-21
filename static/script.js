const taskForm = document.getElementById("taskForm");
const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

// Fetch and display tasks
function loadTasks() {
    fetch("/tasks")
        .then((response) => response.json())
        .then((tasks) => {
            taskList.innerHTML = "";
            tasks.forEach((task) => {
                const li = document.createElement("li");
                li.textContent = task.content;
                const deleteButton = document.createElement("button");
                deleteButton.textContent = "Delete";
                deleteButton.onclick = () => deleteTask(task.id);
                li.appendChild(deleteButton);
                taskList.appendChild(li);
            });
        });
}

// Add a new task
taskForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const newTask = { content: taskInput.value };
    fetch("/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newTask),
    }).then(() => {
        taskInput.value = "";
        loadTasks();
    });
});

// Delete a task
function deleteTask(taskId) {
    fetch(`/tasks/${taskId}`, { method: "DELETE" }).then(() => loadTasks());
}

// Initial load
loadTasks();
