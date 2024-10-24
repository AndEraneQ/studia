package com.trojan.currency_exchanger.model

import com.trojan.currency_exchanger.dto.CurrenciesDto
import com.trojan.currency_exchanger.fetchers.IDataFetcher
import com.trojan.currency_exchanger.serializers.ICurrenciesSerializer
import com.trojan.currency_exchanger.utils.FetcherUtils
import jakarta.annotation.PostConstruct
import org.springframework.stereotype.Component

@Component
class CurrenciesData(
    private val xmlFetcher: IDataFetcher,
    private val currenciesSerializer: ICurrenciesSerializer,
) : ICurrenciesData {

    private var currencies: List<Currency> = emptyList()

    @PostConstruct
    fun init() {
        loadCurrencies()
    }

    private fun loadCurrencies() {
        val jsonString = xmlFetcher.fetchDataFromUrl(FetcherUtils.NBP_URL)
        this.currencies = parseCurrencies(jsonString)
        addPlnCurrency();
    }

    private fun parseCurrencies(jsonString: String): List<Currency> {
        val currenciesDto: CurrenciesDto = currenciesSerializer.parseToCurrenciesData(jsonString)
        return currenciesDto.rates
    }

    private fun addCurrencyManually(currency: Currency) {
        if (!currencies.any { it.code == currency.code }) {
            currencies = currencies + currency
        }
    }

    private fun addPlnCurrency() {
        val pln = Currency(
            name = "Złoty",
            code = "PLN",
            value = 1.0
        )
        addCurrencyManually(pln)
    }

    override fun getCurrencyByCode(code: String): Currency {
        return currencies.firstOrNull { it.code.equals(code, ignoreCase = true) }
            ?: throw IllegalArgumentException("Currency with code '$code' not found")
    }

    fun getCurrencies(): List<Currency> {
        return currencies;
    }

}
