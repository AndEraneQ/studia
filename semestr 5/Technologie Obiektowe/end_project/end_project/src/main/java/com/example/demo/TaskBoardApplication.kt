package com.example.demo

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication

@SpringBootApplication
open class TaskBoardApplication

fun main(args: Array<String>) {
    SpringApplication.run(TaskBoardApplication::class.java, *args)
}
