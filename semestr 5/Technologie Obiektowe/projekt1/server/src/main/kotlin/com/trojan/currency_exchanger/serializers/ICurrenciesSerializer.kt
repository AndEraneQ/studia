package com.trojan.currency_exchanger.serializers

import com.trojan.currency_exchanger.dto.CurrencyResponse
import com.trojan.currency_exchanger.model.CurrenciesData

interface IJsonToCurrenciesSerializer {
    fun parseJsonToCurrenciesData(stringToParse: String) : CurrencyResponse
}