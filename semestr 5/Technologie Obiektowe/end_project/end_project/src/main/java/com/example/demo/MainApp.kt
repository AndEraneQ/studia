package com.example.demo

import org.springframework.boot.CommandLineRunner
import org.springframework.stereotype.Component

@Component
class MainApp(
    private val consoleHandler: ConsoleHandler
) : CommandLineRunner {

    override fun run(vararg args: String?) {
        consoleHandler.start()
    }
}
