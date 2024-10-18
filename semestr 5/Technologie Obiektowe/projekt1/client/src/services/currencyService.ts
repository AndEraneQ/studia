import axios from 'axios';

const API_URL = 'http://localhost:8080/api/v1/currency';

const currencyService = {
  fetchCurrencies: async () => {
    try {
      const response = await axios.get(`${API_URL}/codes`);
      return response.data;
    } catch (error) {
        throw new Error("Server error, try again later");
    }
  },

  exchangeCurrency: async (codeFrom: string, codeTo: string, amount: string) => {
    try {
      const response = await axios.post(`${API_URL}/exchange`, {
        codeFrom,
        codeTo,
        amount: parseFloat(amount),
      });
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        throw new Error(error.response?.data);
      }
    }
  }
};

export default currencyService;
