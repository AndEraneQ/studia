package com.trojan.currency_exchanger.controller

import com.trojan.currency_exchanger.dto.ExchangeRequest
import com.trojan.currency_exchanger.service.CurrencyService
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/v1/currency")
class CurrencyController(
    private val currencyService: CurrencyService
) {
    @GetMapping("/codes")
    @ResponseStatus(HttpStatus.OK)
    fun getCurrencyCodes(): List<String> {
        return currencyService.getCurrencyCodes()
    }

    @PostMapping("/exchange")
    @ResponseStatus(HttpStatus.OK)
    fun exchangeCurrency(@RequestBody exchangeRequest: ExchangeRequest): Double {
        return currencyService.exchangeCurrency(exchangeRequest)
    }
}
