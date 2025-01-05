package com.example.demo

import org.springframework.stereotype.Component

@Component
class UserRepository : IUserRepository {

    private val _users: MutableList<User> = mutableListOf()
    private var _userLoggedIn: User? = null

    override fun add(username: String, password: String, confirmPassword: String) {
        if (_users.any { it.username == username }) {
            println("Error: User with username '$username' already exists.")
            return
        }
        if (password != confirmPassword) {
            println("Error: Passwords do not match.")
            return
        }
        // Add new user to the list
        _users.add(User(username, password))
        println("User '$username' added successfully.")
    }

    override fun update(newUsername: String?, newPassword: String?) {
        val currentUser = _userLoggedIn ?: run {
            println("Error: No user is logged in.")
            return
        }

        val userToUpdate = _users.find { it.username == currentUser.username } ?: run {
            println("Error: Logged-in user not found in the user list.")
            return
        }

        newUsername?.let {
            if (it != currentUser.username) {
                _users.remove(userToUpdate)
                _users.add(userToUpdate.copy(username = it))
                println("Username updated successfully from '${currentUser.username}' to '$it'.")
            }
        }

        newPassword?.let {
            _users[_users.indexOf(userToUpdate)] = userToUpdate.copy(password = it)
            println("Password updated successfully for user '${userToUpdate.username}'.")
        }

        if (newUsername == null && newPassword == null) {
            println("No changes were made.")
        }
    }

    override fun getUsers(username: String) {
        val users = _users.map { it -> it.username }
        println(users)
    }

    override fun delete(username: String) {
        val userToDelete = _users.find { it.username == username }

        if (userToDelete != null) {
            _users.remove(userToDelete)
            println("User '$username' deleted successfully.")
        } else {
            println("Error: User '$username' not found.")
        }
    }

    override fun login(username: String, password: String) {
        val user = _users.find { it.username == username && it.password == password }

        if (user != null) {
            _userLoggedIn = user
            println("User '$username' logged in successfully.")
        } else {
            println("Error: Invalid credentials for user '$username'.")
        }
    }

    override fun getLoggedInUser() {
        val username = _userLoggedIn?.username

        if (username != null) {
            println("User '$username' is logged in.")
        } else {
            println("No user is currently logged in.")
        }
    }

}
