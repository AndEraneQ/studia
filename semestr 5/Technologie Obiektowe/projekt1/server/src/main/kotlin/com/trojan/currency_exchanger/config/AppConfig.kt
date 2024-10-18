package com.trojan.currency_exchanger.config

import com.fasterxml.jackson.databind.ObjectMapper
import com.fasterxml.jackson.dataformat.xml.XmlMapper
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.web.client.RestTemplate

@Configuration
class AppConfig {

    @Bean
    fun restTemplate(): RestTemplate {
        return RestTemplate()
    }

    @Bean
    fun xmlMapper(): XmlMapper {
        return XmlMapper()
    }

    @Bean
    fun objectMapper(): ObjectMapper {
        return ObjectMapper();
    }
}
