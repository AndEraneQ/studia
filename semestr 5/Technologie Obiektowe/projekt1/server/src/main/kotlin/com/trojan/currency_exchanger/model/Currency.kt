package com.trojan.currency_exchanger.model

import com.fasterxml.jackson.annotation.JsonProperty

data class Currency(
    @JsonProperty("currency")
    val name: String,

    @JsonProperty("code")
    val code: String,

    @JsonProperty("mid")
    val value: Double

)
