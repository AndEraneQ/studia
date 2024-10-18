package com.trojan.currency_exchanger.config

import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.web.servlet.config.annotation.CorsRegistry
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer

@Configuration
class WebConfig : WebMvcConfigurer {

    override fun addCorsMappings(registry: CorsRegistry) {
        registry.addMapping("/api/v1/currency/**")
            .allowedOrigins("http://localhost:5173")
            .allowedMethods("GET", "POST")
            .allowCredentials(true)
    }
}
