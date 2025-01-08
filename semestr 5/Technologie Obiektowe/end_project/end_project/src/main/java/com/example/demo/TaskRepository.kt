package com.example.demo

import TaskFactory
import org.springframework.stereotype.Component
import java.util.concurrent.CopyOnWriteArrayList

@Component
class TaskRepository(
    private val taskFactory: TaskFactory,
    private val userRepository: UserRepository,
) {
    private val tasks: MutableList<Task> = CopyOnWriteArrayList()

    fun addTask(task: Task) {
        tasks.add(task)
    }

    fun listTasks(): List<String> {
        return if (tasks.isEmpty()) {
            listOf("No tasks available.")
        } else {
            tasks.map { "Task: ${it.displayTask()}" }
        }
    }

    fun assignTaskToUser(taskName: String, username: String): String {
        val task = getTaskByName(taskName)
        val user = userRepository.getUserByUsername(username)

        return when {
            task == null -> "Task not found!"
            user == null -> "User '$username' does not exist!"
            else -> {
                task.assignedUsername = username
                "Task '${task.name}' assigned to user '$username'."
            }
        }
    }

    fun getTaskByName(name: String): Task? = tasks.find { it.name == name }

    fun updateTask(name: String, newDescription: String): String {
        val task = getTaskByName(name)?.apply { description = newDescription }
        return task?.let { "Task updated successfully: ${it.displayTask()}" }
            ?: "Error: Task with name '$name' not found."
    }

    fun removeTask(name: String): String {
        val task = getTaskByName(name)
        return if (task != null) {
            tasks.remove(task)
            "Task removed successfully: ${task.name}"
        } else {
            "Error: Task with name '$name' not found."
        }
    }
}
