import React, { useState } from 'react';
import './App.css';
import CurrencySelect from './CurrencySelect'; // importuj nowy komponent

function App() {
  const currencies: string[] = ['USD', 'EUR', 'PLN', 'GBP'];

  const [fromCurrency, setFromCurrency] = useState<string>(currencies[0]);
  const [toCurrency, setToCurrency] = useState<string>(currencies[1]);

  const handleExchange = () => {
    console.log(`Wymień ${fromCurrency} na ${toCurrency}`);
  };

  return (
    <div className='exchanger-container'>
      <div className='exchanger-header'>
        <h1 className='exchanger-title'>Exchange your money</h1>
      </div>
      <div className='exchanger-input-container'>
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
        <button onClick={handleExchange} className='exchanger-button'>Wymień</button>
      </div>
    </div>
  );
}

export default App;
