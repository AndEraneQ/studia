package com.example.demo

import org.springframework.stereotype.Component
import java.util.*

@Component
class ConsoleHandler(
    private val userService: UserService,
    private val taskService: TaskService
) : IConsoleHandler {
    override fun start() {
        val scanner = Scanner(System.`in`)
        userService.registerUser("admin", "admin", "admin")
        userService.registerUser("admin1", "admin1", "admin1")
        userService.registerUser("admin2", "admin2", "admin2")
        val task1 = BugTask(name = "bugfix", description = "Fix the bug")
        val task2 = BugTask(name = "bugfix1", description = "Fix the bug1")
        val task3 = BugTask(name = "bugfix2", description = "Fix the bug2")

        // Passing Task objects to addTask function
        taskService.taskRepository.addTask(task1)
        taskService.taskRepository.addTask(task2)
        taskService.taskRepository.addTask(task3)

        while (true) {
            if (userService.getLoggedInUser() != null) {
                displayTaskMenu(scanner)
            } else {
                displayLoginMenu(scanner)
            }
        }
    }

    // Login menu for not logged in users
    private fun displayLoginMenu(scanner: Scanner) {
        println(
            """
            |==============================
            |   TASK MANAGEMENT SYSTEM
            |==============================
            | 1. Register
            | 2. Login
            | 0. Exit
            |==============================
            | Enter your choice:
        """.trimMargin()
        )
        when (scanner.nextInt()) {
            1 -> registerUser(scanner)
            2 -> loginUser(scanner)
            0 -> exitApp()
            else -> println("Invalid choice. Please try again.")
        }
        userService.displayUsers()
    }

    // Task menu for logged in users
    private fun displayTaskMenu(scanner: Scanner) {
        println(
            """
            |==============================
            |   TASK MANAGEMENT SYSTEM
            |==============================
            | 1. Add Task
            | 2. List Tasks
            | 3. Update Task Description
            | 4. Remove Task
            | 5. Progress Task
            | 6. Regress Task
            | 7. Assign Task to User
            | 8. Logout
            | 0. Exit
            |==============================
            | Enter your choice:
        """.trimMargin()
        )
        when (scanner.nextInt()) {
            1 -> addTask(scanner)
            2 -> taskService.listAllTasks()
            3 -> updateTaskDescription(scanner)
            4 -> removeTask(scanner)
            5 -> progressTask(scanner)
            6 -> regressTask(scanner)
            7 -> assignTaskToUser(scanner)
            8 -> userService.logout()
            0 -> exitApp()
            else -> println("Invalid choice. Please try again.")
        }
        userService.displayUsers()
        println(taskService.taskRepository.listTasks())
    }

    private fun registerUser(scanner: Scanner) {
        val username = getInput(scanner, "Enter username: ")
        val password = getInput(scanner, "Enter password: ")
        val confirmPassword = getInput(scanner, "Confirm password: ")
        userService.registerUser(username, password, confirmPassword)
    }

    private fun loginUser(scanner: Scanner) {
        val username = getInput(scanner, "Enter username: ")
        val password = getInput(scanner, "Enter password: ")
        userService.login(username, password)
    }

    private fun addTask(scanner: Scanner) {
        val type = getInput(scanner, "Enter task type (bug, feature, improvement): ")
        val name = getInput(scanner, "Enter task name: ")
        val description = getInput(scanner, "Enter task description: ")
        taskService.createTask(type, name, description)
    }

    private fun updateTaskDescription(scanner: Scanner) {
        val name = getInput(scanner, "Enter task name to update: ")
        val newDescription = getInput(scanner, "Enter new task description: ")
        taskService.updateTaskDescription(name, newDescription)
    }

    private fun removeTask(scanner: Scanner) {
        val name = getInput(scanner, "Enter task name to delete: ")
        taskService.deleteTask(name)
    }

    private fun progressTask(scanner: Scanner) {
        val name = getInput(scanner, "Enter task name to progress: ")
        taskService.progressTask(name)
    }

    private fun regressTask(scanner: Scanner) {
        val name = getInput(scanner, "Enter task name to regress: ")
        taskService.regressTask(name)
    }

    private fun assignTaskToUser(scanner: Scanner) {
        val taskName = getInput(scanner, "Enter name of task: ")
        val username = getInput(scanner, "Enter username: ")
        taskService.assignTaskToUser(taskName, username)
    }

    private fun getInput(scanner: Scanner, prompt: String): String {
        println(prompt)
        return scanner.next()
    }

    private fun exitApp() {
        println("Exiting the application. Goodbye!")
        kotlin.system.exitProcess(0)
    }
}
