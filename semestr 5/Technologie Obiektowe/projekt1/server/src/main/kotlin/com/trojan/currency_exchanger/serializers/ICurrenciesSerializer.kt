package com.trojan.currency_exchanger.serializers

import com.trojan.currency_exchanger.dto.CurrenciesDto

interface ICurrenciesSerializer {
    fun parseToCurrenciesData(stringToParse: String) : CurrenciesDto
}