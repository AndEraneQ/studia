package org.example.vector

interface IVector {
    fun abs(): Double
    fun cdot(iVector: IVector): Double
    fun getComponents(): Array<Double>
}
