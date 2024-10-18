package com.trojan.currency_exchanger.serializers

import com.fasterxml.jackson.databind.ObjectMapper
import com.trojan.currency_exchanger.dto.CurrenciesDto
import org.springframework.stereotype.Component

@Component
class JsonToCurrenciesSerializer(
    private val objectMapper: ObjectMapper
) : ICurrenciesSerializer {
    override fun parseToCurrenciesData(stringToParse: String): CurrenciesDto {
        val currenciesList: List<CurrenciesDto> =
            objectMapper.readValue(stringToParse,
                objectMapper.typeFactory.constructCollectionType(List::class.java, CurrenciesDto::class.java))
        return currenciesList.first()
    }
}
