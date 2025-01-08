package com.example.demo


interface TaskState {
    fun progress(task: Task)
    fun regress(task: Task)
    fun getStatus(): String
}

class ToDoState : TaskState {
    override fun progress(task: Task) {
        println("Progressing task '${task.name}' from To Do to Doing.")
        task.state = DoingState()
    }

    override fun regress(task: Task) {
        println("Task '${task.name}' is already in To Do. Cannot regress further.")
    }

    override fun getStatus(): String {
        return "To Do"
    }
}

class DoingState : TaskState {
    override fun progress(task: Task) {
        println("Progressing task '${task.name}' from Doing to Testing.")
        task.state = TestingState()
    }

    override fun regress(task: Task) {
        println("Regressing task '${task.name}' from Doing to To Do.")
        task.state = ToDoState()
    }

    override fun getStatus(): String {
        return "Doing"
    }
}

class TestingState : TaskState {
    override fun progress(task: Task) {
        println("Progressing task '${task.name}' from Testing to Done.")
        task.state = DoneState()
    }

    override fun regress(task: Task) {
        println("Regressing task '${task.name}' from Testing to Doing.")
        task.state = DoingState()
    }

    override fun getStatus(): String {
        return "Testing"
    }
}

class DoneState : TaskState {
    override fun progress(task: Task) {
        println("Task '${task.name}' is already done. No further progress.")
    }

    override fun regress(task: Task) {
        println("Regressing task '${task.name}' from Done to Testing.")
        task.state = TestingState()
    }

    override fun getStatus(): String {
        return "Done"
    }
}
