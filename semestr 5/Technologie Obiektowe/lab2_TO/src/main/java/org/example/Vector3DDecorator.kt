package org.example

import kotlin.math.acos
import kotlin.math.atan2

class Vector3DDecorator(private val srcVector: IVector, private val z: Double) : IVector {
    override fun abs(): Double {
        val components = srcVector.getComponents()
        return Math.sqrt(components[0] * components[0] + components[1] * components[1] + z * z)
    }

    override fun cdot(param: IVector): Double {
        val components = param.getComponents()
        val srcComponents = srcVector.getComponents()
        return srcComponents[0] * components[0] + srcComponents[1] * components[1] + z * components[2]
    }

    override fun getComponents(): DoubleArray {
        val components = srcVector.getComponents()
        return doubleArrayOf(components[0], components[1], z)
    }

    fun getPolars(): DoubleArray {
        val r = abs()
        val theta = atan2(srcVector.getComponents()[1], srcVector.getComponents()[0])
        val phi = acos(z / r)
        return doubleArrayOf(r, theta, phi)
    }

    fun cross(param: IVector): IVector {
        val a = this.getComponents()
        val b = param.getComponents()

        return if (b.size == 2) {
            val crossX = -a[2] * b[1];
            val crossY =a[2]*b[0];
            val crossZ = a[0] * b[1] - a[1] * b[0]
            Vector3DDecorator(Vector2D(crossX,crossY), crossZ)
        } else {
            val crossX = a[1] * b[2] - a[2] * b[1]
            val crossY = a[2] * b[0] - a[0] * b[2]
            val crossZ = a[0] * b[1] - a[1] * b[0]
            Vector3DDecorator(Vector2D(crossX, crossY), crossZ)
        }
    }
}
