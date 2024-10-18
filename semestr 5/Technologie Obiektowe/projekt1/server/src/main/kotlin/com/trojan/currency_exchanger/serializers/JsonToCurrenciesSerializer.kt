package com.trojan.currency_exchanger.serializers

import com.fasterxml.jackson.dataformat.xml.XmlMapper
import com.trojan.currency_exchanger.model.CurrenciesData
import com.trojan.currency_exchanger.model.Currency
import org.springframework.stereotype.Component

@Component
class XmlToCurrenciesSerializer(private val xmlMapper: XmlMapper) : IXmlToCurrenciesSerializer{
    override fun parseXmlToCurrenciesData(stringToParse: String): CurrenciesData {
        return xmlMapper.readValue(
            stringToParse,
            xmlMapper.typeFactory.constructCollectionType(
                List::class.java,
                Currency::class.java
            )
        )
    }
}