package com.trojan.currency_exchanger.service

import com.trojan.currency_exchanger.dto.ExchangeRequest
import com.trojan.currency_exchanger.exception.InvalidExchangeRequestException
import com.trojan.currency_exchanger.model.CurrenciesData
import com.trojan.currency_exchanger.model.Currency
import org.springframework.stereotype.Service
import java.math.BigDecimal
import java.math.RoundingMode

@Service
class CurrencyService(
    private val currenciesData: CurrenciesData
) : ICurrencyService {
    override fun getCurrencyCodes(): List<String> {
        return currenciesData.getCurrencies().map { it.code }
    }

    override fun exchangeCurrency(exchangeRequest: ExchangeRequest): Double {
        validateExchangeRequest(exchangeRequest)

        val currencyFrom = currenciesData.getCurrencyByCode(exchangeRequest.codeFrom)
        val currencyTo = currenciesData.getCurrencyByCode(exchangeRequest.codeTo)

        return calculateExchangeAmount(exchangeRequest.amount, currencyFrom, currencyTo)
    }

    private fun validateExchangeRequest(exchangeRequest: ExchangeRequest) {

        if (exchangeRequest.amount <= 0.0) {
            throw InvalidExchangeRequestException("Type amount correctly!")
        }
    }

    private fun calculateExchangeAmount(amount: Double, currencyFrom: Currency, currencyTo: Currency): Double {
        val result = amount * currencyFrom.value / currencyTo.value
        return BigDecimal(result).setScale(4, RoundingMode.HALF_UP).toDouble()
    }
}
