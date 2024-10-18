package com.trojan.currency_exchanger.dto

data class ExchangeDto(
    val codeFrom: String,
    val codeTo: String,
    val amount: Double
)
