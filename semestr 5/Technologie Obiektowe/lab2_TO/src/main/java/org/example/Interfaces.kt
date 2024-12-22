package org.example

interface IPolar2D {
    fun getAngle(): Double
    fun abs(): Double
}

interface IVector {
    fun abs(): Double
    fun cdot(param: IVector): Double
    fun getComponents(): DoubleArray
}
