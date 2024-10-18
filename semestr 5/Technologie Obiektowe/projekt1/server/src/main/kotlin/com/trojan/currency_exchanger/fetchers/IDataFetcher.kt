package com.trojan.currency_exchanger.fetchers

interface IXmlFetcher {
    fun fetchXmlFromUrl(url : String) : String
}