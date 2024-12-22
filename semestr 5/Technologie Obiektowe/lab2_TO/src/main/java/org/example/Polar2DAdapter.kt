package org.example

import kotlin.math.atan2

class Polar2DAdapter(private val srcVector: Vector2D) : IVector, IPolar2D {
    override fun abs(): Double {
        return srcVector.abs()
    }

    override fun cdot(param: IVector): Double {
        return srcVector.cdot(param)
    }

    override fun getComponents(): DoubleArray {
        return srcVector.getComponents()
    }

    override fun getAngle(): Double {
        return atan2(srcVector.y, srcVector.x)
    }
}
