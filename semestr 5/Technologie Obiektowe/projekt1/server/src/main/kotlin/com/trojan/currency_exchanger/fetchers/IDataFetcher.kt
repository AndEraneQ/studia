package com.trojan.currency_exchanger.fetchers

interface IDataFetcher {
    fun fetchDataFromUrl(url : String) : String
}