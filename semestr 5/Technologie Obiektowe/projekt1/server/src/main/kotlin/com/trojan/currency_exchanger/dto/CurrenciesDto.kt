package com.trojan.currency_exchanger.dto

import com.fasterxml.jackson.annotation.JsonProperty
import com.trojan.currency_exchanger.model.Currency

data class CurrenciesDto(
    @JsonProperty("table")
    val table: String,

    @JsonProperty("no")
    val no: String,

    @JsonProperty("effectiveDate")
    val effectiveDate: String,

    @JsonProperty("rates")
    val rates: List<Currency>
)
