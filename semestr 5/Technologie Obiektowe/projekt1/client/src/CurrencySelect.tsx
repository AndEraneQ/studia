import React from 'react';

interface CurrencySelectProps {
  label: string;
  currency: string;
  onCurrencyChange: (currency: string) => void;
  currencies: string[];
}

const CurrencySelect: React.FC<CurrencySelectProps> = ({
  label,
  currency,
  onCurrencyChange,
  currencies,
}) => {
  return (
    <div className='exchanger-currency-select'>
      <label className='exchanger-label'>{label}</label>
      <select 
        className='exchanger-select'
        value={currency}
        onChange={(e) => onCurrencyChange(e.target.value)}
      >
        {currencies.map((curr) => (
          <option key={curr} value={curr}>{curr}</option>
        ))}
      </select>
    </div>
  );
};

export default CurrencySelect;
