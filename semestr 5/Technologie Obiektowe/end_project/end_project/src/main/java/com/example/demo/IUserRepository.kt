package com.example.demo

interface IUserRepository {
    fun add(username: String, password: String, confirmPassword: String)
    fun update(newUsername: String?, newPassword: String?)
    fun getUsers(username: String)
    fun delete(username: String)
    fun login(username: String, password: String)
    fun getLoggedInUser()
}