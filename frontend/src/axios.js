import axios from 'axios';

const instance = axios.create({
  baseURL: import.meta.env.VITE_API_TEST_URL,
  withCredentials: true, // Include cookies if authentication is required
});

export default instance;