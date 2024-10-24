package org.example.vector

import kotlin.math.sqrt

class Vector3DInheritance(x: Double, y: Double, val z: Double) : Vector2D(x, y) {
    override fun abs(): Double {
        return sqrt(x * x + y * y + z * z)
    }

    override fun cdot(other: IVector): Double {
        val components = other.getComponents()
        return super.cdot(other) + z * components[2]
    }

    override fun getComponents(): Array<Double> {
        return super.getComponents() + z
    }

    fun cross(other: IVector): DoubleArray {
        val components = getComponents()
        val otherComponents = other.getComponents()
        return doubleArrayOf(
            components[1] * otherComponents[2] - components[2] * otherComponents[1],
            components[2] * otherComponents[0] - components[0] * otherComponents[2],
            components[0] * otherComponents[1] - components[1] * otherComponents[0]
        )
    }
}