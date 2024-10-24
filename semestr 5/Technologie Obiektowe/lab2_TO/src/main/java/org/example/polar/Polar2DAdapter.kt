package org.example.polar

import org.example.vector.IVector
import org.example.vector.Vector2D
import kotlin.math.PI
import kotlin.math.atan2

class Polar2DAdapter(private val srcVector: Vector2D) : IPolar2D {
    override fun abs(): Double {
        return srcVector.abs()
    }

    fun cdot(other: IVector): Double {
        return srcVector.cdot(other)
    }

    fun getComponents(): Array<Double> {
        return srcVector.getComponents()
    }

    override fun getAngle(): Double {
        return Math.toDegrees(atan2(getComponents()[1], getComponents()[0]))
    }

}