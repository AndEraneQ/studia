package com.example.demo

import org.springframework.boot.CommandLineRunner
import org.springframework.stereotype.Component
import java.util.*

@Component
class MainApp(
    val userRepository: UserRepository
) : CommandLineRunner {
    override fun run(vararg args: String?) {
        userRepository.add("piotr_trojan", "qwerty", "qwerty")
        userRepository.add("adam_adamski", "12345", "12345")
        userRepository.add("bartek_bartkowski", "67890", "67890")
    }
}
