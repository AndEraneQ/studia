package com.example.demo

import TaskFactory
import org.springframework.stereotype.Service

@Service
class TaskService(
    val taskRepository: TaskRepository,
    val taskFactory: TaskFactory
) {
    fun createTask(type: String, name: String, description: String) {
        if (taskRepository.getTaskByName(name) != null) {
            println("Task with name '$name' already exists!")
            return
        }

        try {
            val task = taskFactory.createTask(type, name, description)
            taskRepository.addTask(task)
            println("Task '$name' added successfully!")
        } catch (e: Exception) {
            println("Error: ${e.message}")
        }
    }

    fun listAllTasks() {
        println("Listing All Tasks:")
        val tasks = taskRepository.listTasks()
        tasks.forEach { println(it) }
    }

    fun assignTaskToUser(taskName: String, username: String) {
        taskRepository.assignTaskToUser(taskName,username)
    }

    fun updateTaskDescription(name: String, newDescription: String) {
        val result = taskRepository.updateTask(name, newDescription)
        println(result)
    }

    fun deleteTask(name: String) {
        val result = taskRepository.removeTask(name)
        println(result)
    }

    fun progressTask(name: String) {
        val task = taskRepository.getTaskByName(name)
        if (task != null) {
            task.state.progress(task)
            println("Task progressed. Current status: ${task.state.getStatus()}")
        } else {
            println("Task not found!")
        }
    }

    fun regressTask(name: String) {
        val task = taskRepository.getTaskByName(name)
        if (task != null) {
            task.state.regress(task)
            println("Task regressed. Current status: ${task.state.getStatus()}")
        } else {
            println("Task not found!")
        }
    }
}
