package com.trojan.currency_exchanger.fetchers

import org.springframework.stereotype.Component
import org.springframework.web.client.RestTemplate

@Component
class XmlFetcher(private val restTemplate: RestTemplate) : IXmlFetcher {
    override fun fetchXmlFromUrl(url: String): String {
        return restTemplate.getForObject(url, String::class.java) ?: throw Exception("Failed to fetch XML")
    }
}
