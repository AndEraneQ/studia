package org.example

open class Vector2D(val x: Double, val y: Double) : IVector {
    override fun abs(): Double {
        return Math.sqrt(x * x + y * y)
    }

    override fun cdot(param: IVector): Double {
        val components = param.getComponents()
        return x * components[0] + y * components[1]
    }

    override fun getComponents(): DoubleArray {
        return doubleArrayOf(x, y)
    }
}
