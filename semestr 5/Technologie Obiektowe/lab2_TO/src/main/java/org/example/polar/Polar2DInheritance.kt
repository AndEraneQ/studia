package org.example.polar


import org.example.vector.Vector2D
import kotlin.math.atan2
import kotlin.math.PI

class Polar2DInheritance(x: Double, y: Double) : Vector2D(x, y) {
    fun getAngle(): Double {
        val angle = atan2(y, x)
        return angle * (180 / PI)
    }
}
