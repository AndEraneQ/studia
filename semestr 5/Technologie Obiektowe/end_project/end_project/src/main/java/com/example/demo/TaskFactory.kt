import com.example.demo.ITaskFactory

class TaskFactory {
    fun createTask(type: String, name: String, description: String): Task {
        return when (type) {
            "bug" -> BugTask(name, description)
            "feature" -> FeatureTask(name, description)
            "improvement" -> ImprovementTask(name, description)
            else -> throw IllegalArgumentException("Unknown task type")
        }
    }
}

