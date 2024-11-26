package org.example.vector

import kotlin.math.sqrt

class Vector3DDecorator(private val srcVector: IVector, private val z: Double) : IVector {
    override fun abs(): Double {
        val components = srcVector.getComponents()
        return sqrt(components[0] * components[0] + components[1] * components[1] + z * z)
    }

    override fun cdot(other: IVector): Double {
        val components = other.getComponents()
        val zComponent = if (other is Vector3DInheritance) other.z else 0.0
        return srcVector.cdot(other) + z * zComponent
    }

    override fun getComponents(): Array<Double> {
        val components = srcVector.getComponents()
        return components + z
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