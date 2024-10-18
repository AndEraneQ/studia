package com.trojan.currency_exchanger.dto

import com.fasterxml.jackson.annotation.JsonCreator
import com.fasterxml.jackson.annotation.JsonProperty

data class ExchangeRequest @JsonCreator constructor(
    @JsonProperty("codeFrom") val codeFrom: String,
    @JsonProperty("codeTo") val codeTo: String,
    @JsonProperty("amount") val amount: Double
)
