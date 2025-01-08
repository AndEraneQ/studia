package com.example.demo

interface Task {
    val name: String
    var description: String
    var state: TaskState
    var assignedUsername: String? // Nullable field for the assigned user
    fun displayTask(): String
}

// Task implementations
class BugTask(
    override val name: String,
    override var description: String,
    override var assignedUsername: String? = null // Default to unassigned
) : Task {
    override var state: TaskState = ToDoState()
    override fun displayTask(): String {
        return """
            |Type: Bug
            |Name: $name
            |Description: $description
            |Status: ${state.getStatus()}
            |Assigned To: ${assignedUsername ?: "Unassigned"}
        """.trimMargin()
    }
}

class FeatureTask(
    override val name: String,
    override var description: String,
    override var assignedUsername: String? = null // Default to unassigned
) : Task {
    override var state: TaskState = ToDoState()
    override fun displayTask(): String {
        return """
            |Type: Feature
            |Name: $name
            |Description: $description
            |Status: ${state.getStatus()}
            |Assigned To: ${assignedUsername ?: "Unassigned"}
        """.trimMargin()
    }
}

class ImprovementTask(
    override val name: String,
    override var description: String,
    override var assignedUsername: String? = null // Default to unassigned
) : Task {
    override var state: TaskState = ToDoState()
    override fun displayTask(): String {
        return """
            |Type: Improvement
            |Name: $name
            |Description: $description
            |Status: ${state.getStatus()}
            |Assigned To: ${assignedUsername ?: "Unassigned"}
        """.trimMargin()
    }
}
