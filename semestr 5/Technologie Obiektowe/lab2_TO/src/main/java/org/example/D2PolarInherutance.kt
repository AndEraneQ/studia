package org.example

class D2PolarInheritance(x: Double, y: Double) : Vector2D(x, y){
    fun getAngle(): Double {
        return Math.atan2(y, x)
    }
}
