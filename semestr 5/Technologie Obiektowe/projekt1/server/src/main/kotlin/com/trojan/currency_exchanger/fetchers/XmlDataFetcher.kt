package com.trojan.currency_exchanger.fetchers

import org.springframework.stereotype.Component
import org.springframework.web.client.RestTemplate

@Component
class XmlDataFetcher(
    private val restTemplate: RestTemplate
) : IDataFetcher {
    override fun fetchDataFromUrl(url: String): String {
        return restTemplate.getForObject(url, String::class.java) ?: throw Exception("Failed to fetch XML")
    }
}
