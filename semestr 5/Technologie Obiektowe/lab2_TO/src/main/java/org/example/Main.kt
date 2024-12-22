import org.example.Polar2DAdapter
import org.example.Vector2D
import org.example.Vector3DDecorator
import org.example.Vector3DInheritance

fun main() {
    val vector2D_1 = Polar2DAdapter(Vector2D(3.0, 5.0))

    val vector3DDecorator = Vector3DDecorator(vector2D_1, 15.0)
    val vector3DInheritance = Vector3DInheritance(8.0, 18.0, 3.0)
    val vector3DInher = Vector3DInheritance(3.0, 18.0, 8.0)


    println("------------------------------\n      Cartesian Coordinates\n------------------------------")
    println("Vector 2D:\t\t\t${vector2D_1.getComponents().contentToString()}")
    println("Vector 3D Decorator:\t\t${vector3DDecorator.getComponents().contentToString()}")
    println("Vector 3D Inheritance:\t\t${vector3DInheritance.getComponents().contentToString()}")

    println("\n------------------------------\n      Polar Coordinates\n------------------------------")
    println("Vector 2D:\t\t\t[${"%.2f".format(vector2D_1.abs())}, ${vector2D_1.getAngle()}]")
    println("Vector 3D Decorator:\t\t${vector3DDecorator.getPolars().contentToString()}")
    println("Vector 3D Inheritance:\t\t${vector3DInheritance.getPolars().contentToString()}")

    println("\n------------------------------\n      Scalar Product\n------------------------------")
    println("Vector 2D and Vector 2D:\t\t\t\t${vector2D_1.cdot(vector2D_1)}")
    println("Vector 2D and Vector 3D Inheritance:\t\t\t${vector2D_1.cdot(vector3DInheritance)}")
    println("Vector 2D and Vector 3D Decorator:\t\t\t${vector2D_1.cdot(vector3DDecorator)}")
    println("Vector 3D Inheritance and Vector 3D Decorator:\t\t${vector3DInheritance.cdot(vector3DDecorator)}")
    println("Vector 3D Inheritance and Vector 3D Inheritance:\t${vector3DInheritance.cdot(vector3DInheritance)}")
    println("Vector 3D Decorator and Vector 3D Decorator:\t\t${vector3DDecorator.cdot(vector3DDecorator)}")

    println("\n------------------------------\n      Vector Product\n------------------------------")
    println("Vector 3D Inheritance and Vector 2D:\t\t\t${vector3DInheritance.cross(vector2D_1).getComponents().contentToString()}")
    println("Vector 3D Decorator and Vector 2D:\t\t\t${vector3DDecorator.cross(vector2D_1).getComponents().contentToString()}")
    println("Vector 3D Inheritance and Vector 3D Decorator:\t\t${vector3DInheritance.cross(vector3DDecorator).getComponents().contentToString()}")
    println("Vector 3D Decorator and Vector 3D Inheritance:\t\t${vector3DDecorator.cross(vector3DInheritance).getComponents().contentToString()}")
    println("\n")
}
