package org.example.vector

import kotlin.math.sqrt

open class Vector2D(
    protected  var x : Double,
    protected  var y : Double
) : IVector {

    override fun abs(): Double {
        return sqrt(x * x + y * y)
    }

    override fun cdot(iVector: IVector): Double {
        val components = iVector.getComponents()
        return x * components[0] + y * components[1]
    }

    override fun getComponents(): Array<Double> {
        return arrayOf(x, y)
    }
}