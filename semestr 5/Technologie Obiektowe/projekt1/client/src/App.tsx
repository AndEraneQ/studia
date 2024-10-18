import React, { useEffect, useState } from 'react';
import currencyService from './services/currencyService';
import './App.css';
import CurrencySelect from './components/CurrencySelect';

function App() {
  const [currencies, setCurrencies] = useState<string[]>([]);
  const [fromCurrency, setFromCurrency] = useState<string>('');
  const [toCurrency, setToCurrency] = useState<string>('');
  const [amount, setAmount] = useState<string>('');
  const [result, setResult] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCurrencies = async () => {
      setError(null);
      try {
        const data = await currencyService.fetchCurrencies();
        setCurrencies(data);
        if (data.length > 0) {
          setFromCurrency(data[0]);
          setToCurrency(data[0]);
        }
      } catch (error: unknown) {
        if (error instanceof Error) {
          setError(error.message);
        }
      } 
    };

    fetchCurrencies();
  }, []);

  useEffect(() => {
    const clearResultAndError = () => {
      setResult(null);
      setError(null);
    }

    clearResultAndError();
  }, [toCurrency,fromCurrency,amount])

  const handleExchange = async () => {
    setError(null);
    try {
      const exchangedAmount = await currencyService.exchangeCurrency(fromCurrency, toCurrency, amount);
      setResult(exchangedAmount);
    } catch (error: unknown) {
      setResult(null);
      if (error instanceof Error) {
        setError(error.message);
      }
    }
  };

  return (
    <div className='exchanger-container'>
      <div className='exchanger-header'>
        <h1 className='exchanger-title'>Exchange calculator</h1>
      </div>
      <div className='exchanger-inputs-container'>
        <CurrencySelect 
          label='From:' 
          currency={fromCurrency} 
          onCurrencyChange={setFromCurrency} 
          currencies={currencies} 
        />
        <CurrencySelect 
          label='To:' 
          currency={toCurrency} 
          onCurrencyChange={setToCurrency} 
          currencies={currencies} 
        />
        <div className='exchanger-currency-select'>
          <label className='exchanger-label'>Amount:</label>
          <input
            type='number'
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder='Enter amount'
            className='amount-input'
          />
        </div>
      </div>
      {(result || error) && (
        <div className='response-container'>
          {result ? (
            <p className='result information'>{`${amount} ${fromCurrency} is ${result} ${toCurrency}`}</p>
          ) : (
            <p className='error information'>{error}</p>
          )}
        </div>
      )}
      <div className='button-container'>
        <button onClick={handleExchange} className='exchanger-button'>Exchange</button>
      </div>
    </div>
  );
}

export default App;
