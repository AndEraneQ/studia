package com.trojan.currency_exchanger.model

interface ICurrenciesData {
    fun getCurrencyByCode(code: String): Currency;
}