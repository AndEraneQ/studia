package com.example.demo

import Task
import TaskFactory

class TaskRepository {

    private val tasks = mutableListOf<Task>()

    fun addTask(type: String, name: String, description: String): String {
        val taskFactory = TaskFactory()
        val task = taskFactory.createTask(type, name, description)
        tasks.add(task)
        return "Task added: ${task.displayTask()}"
    }

    fun listTasks(): List<String> {
        return if (tasks.isEmpty()) {
            listOf("No tasks available.")
        } else {
            tasks.map { "Task: ${it.displayTask()}" }
        }
    }

    fun getTaskByName(name: String): Task? {
        return tasks.find { it.name == name }
    }

    fun updateTask(name: String, newDescription: String): String {
        val task = getTaskByName(name)
        return if (task != null) {
            task.description = newDescription
            "Task updated: ${task.name}"
        } else {
            "Task not found!"
        }
    }

    fun removeTask(name: String): String {
        val task = getTaskByName(name)
        return if (task != null) {
            tasks.remove(task)
            "Task removed: ${task.name}"
        } else {
            "Task not found!"
        }
    }
}
