from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/todo_db")


# Replace with your MongoDB URI (e.g., from MongoDB Atlas)
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"

mongo = PyMongo(app)
tasks_collection = mongo.db.tasks

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = []
    for task in tasks_collection.find():
        tasks.append({
            "id": str(task["_id"]),
            "content": task["content"]
        })
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    task_data = request.json
    content = task_data.get("content")
    if content:
        result = tasks_collection.insert_one({"content": content})
        new_task = {
            "id": str(result.inserted_id),
            "content": content
        }
        return jsonify(new_task), 201
    return jsonify({"error": "Content is required"}), 400

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
