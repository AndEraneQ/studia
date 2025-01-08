import com.example.demo.BugTask
import com.example.demo.FeatureTask
import com.example.demo.ImprovementTask
import com.example.demo.Task
import org.springframework.stereotype.Component

@Component
class TaskFactory {
    fun createTask(type: String, name: String, description: String): Task {
        return when (type) {
            "bug" -> BugTask(name, description)
            "feature" -> FeatureTask(name, description)
            "improvement" -> ImprovementTask(name, description)
            else -> throw IllegalArgumentException("Unknown task type!")
        }
    }
}

