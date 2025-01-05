interface Task {
    val name: String
    var description: String
    fun displayTask(): String
}

class BugTask(override val name: String, override var description: String) : Task {
    override fun displayTask(): String {
        return "Type: Bug\nName: $name\nDescription: $description"
    }
}

class FeatureTask(override val name: String, override var description: String) : Task {
    override fun displayTask(): String {
        return " ype: Feature\nName: $name\nDescription: $description"
    }
}

class ImprovementTask(override val name: String, override var description: String) : Task {
    override fun displayTask(): String {
        return "Type: Improvement\nName: $name\nDescription: $description"
    }
}
