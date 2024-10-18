package com.trojan.currency_exchanger.service

import com.trojan.currency_exchanger.dto.ExchangeRequest

interface ICurrencyService {
    fun getCurrencyCodes(): List<String>
    fun exchangeCurrency(exchangeRequest: ExchangeRequest): Double
}