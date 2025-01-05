package com.example.demo
import Task

interface ITaskFactory {
    fun createTask(type: String, id: Int, name: String, description: String): Task
}
