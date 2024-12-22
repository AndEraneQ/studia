package org.example

import kotlin.math.acos
import kotlin.math.atan2

class Vector3DInheritance(x: Double, y: Double, val z: Double) : Vector2D(x, y) {
    override fun abs(): Double {
        return Math.sqrt(x * x + y * y + z * z)
    }

    override fun cdot(param: IVector): Double {
        val components = param.getComponents()
        return x * components[0] + y * components[1] + z * components[2]
    }

    override fun getComponents(): DoubleArray {
        return doubleArrayOf(x, y, z)
    }

    fun getPolars(): DoubleArray {
        val r = abs()
        val theta = atan2(y, x)
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
