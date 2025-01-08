package com.example.demo

import org.springframework.stereotype.Component

@Component
class UserRepository : IUserRepository {

    val _users: MutableList<User> = mutableListOf()
    var _userLoggedIn: User? = null

    override fun add(username: String, password: String, confirmPassword: String) {
        _users.add(User(username, password))
    }

    override fun update(newUsername: String?, newPassword: String?) {
        val currentUser = _userLoggedIn
        if (currentUser == null) {
            println("Error: No user is logged in.")
            return
        }

        val userToUpdate = _users.find { it.username == currentUser.username }
        if (userToUpdate == null) {
            println("Error: Logged-in user not found in the user list.")
            return
        }

        if (newUsername != null && newUsername != currentUser.username) {
            if (_users.any { it.username == newUsername }) {
                println("Error: Username '$newUsername' already exists.")
                return
            }
            _users.remove(userToUpdate)
            _users.add(userToUpdate.copy(username = newUsername))
            _userLoggedIn = userToUpdate.copy(username = newUsername)
            println("Username updated successfully from '${currentUser.username}' to '$newUsername'.")
        }

        if (newPassword != null) {
            _users[_users.indexOf(userToUpdate)] = userToUpdate.copy(password = newPassword)
            _userLoggedIn = userToUpdate.copy(password = newPassword)
            println("Password updated successfully for user '${userToUpdate.username}'.")
        }

        if (newUsername == null && newPassword == null) {
            println("No changes were made.")
        }
    }

    override fun getUsers(username: String) {
        if (_users.isEmpty()) {
            println("No users found.")
        } else {
            _users.forEach { println(it.username) }
        }
    }

    override fun delete(username: String) {
        val userToDelete = _users.find { it.username == username }
        if (userToDelete != null) {
            if (_userLoggedIn?.username == username) {
                _userLoggedIn = null
                println("Logged-in user '$username' has been deleted.")
            }
            _users.remove(userToDelete)
            println("User '$username' deleted successfully.")
        } else {
            println("Error: User '$username' not found.")
        }
    }

    override fun login(username: String) {
        var user = getUserByUsername(username)
        _userLoggedIn = user
    }

    override fun getLoggedInUser(): String? {
        val username = _userLoggedIn?.username
        return if (username != null) {
            println("User '$username' is logged in.")
            username
        } else {
            println("No user is currently logged in.")
            null
        }
    }
    fun getUserByUsername(username: String): User? {
        return _users.find { it.username == username }
    }
}
