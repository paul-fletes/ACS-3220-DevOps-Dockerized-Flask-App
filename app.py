from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
  return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
  task_data = request.json
  task = {
    "id": len(tasks) + 1, 
    "content": task_data.get("content")
  }
  tasks.append(task)
  return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
  global tasks
  tasks = [task for task in tasks if task["id"] != task_id]
  return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
  app.run(debug=True)