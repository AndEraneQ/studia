package org.example.polar

import org.example.vector.Vector2D
import kotlin.math.PI
import kotlin.math.atan2

class Polar2DAdapter(private var srcVector: Vector2D) : IPolar2D {
    override fun getAngle(): Double {
        val angle = atan2(srcVector.getComponents())
        return angle * (180 / PI)
    }

    override fun abs(): Double {
        return srcVector.abs()
    }
}