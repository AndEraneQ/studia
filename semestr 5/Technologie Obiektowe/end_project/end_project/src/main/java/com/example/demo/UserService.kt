package com.example.demo

import org.springframework.stereotype.Service

@Service
class UserService(private val userRepository: UserRepository) {

    fun registerUser(username: String, password: String, confirmPassword: String) {
        if(userRepository.getUserByUsername(username) != null){
            println("User ${username} already exists!")
            return
        }
        if(password != confirmPassword){
            println("Passwords need to be same!")
            return
        }
        userRepository.add(username, password, confirmPassword)
        println("Registered successfully!")
    }

    fun login(username: String, password: String) {
        var user = userRepository.getUserByUsername(username)
        if(user == null){
            println("User ${username} doesn't exists!")
            return
        }
        if(user.password != password){
            println("Wrong password!")
            return
        }
        userRepository.login(username)
        println("Logged in successfully!")
    }

    fun logout() {
        println("Logging out...")
        userRepository.getLoggedInUser()?.let {
            println("User '${it}' logged out successfully.")
        } ?: println("No user is logged in.")
    }

    fun displayUsers() {
        println("Registered Users:")
        userRepository.getUsers("")
    }

    fun getLoggedInUser(): User? {
        return userRepository._userLoggedIn
    }
}
