import { fetchAuthSession } from '@aws-amplify/auth';
import { useAuthStore } from '~/stores/auth';

export const useApi = () => {
  const authStore = useAuthStore();

  const authenticatedFetch = async (endpoint, options = {}) => {
    try {
      const session = await fetchAuthSession();
      const token = session.tokens?.idToken?.toString();

      if (!token) {
        throw new Error('No authentication token available');
      }

      const defaultOptions = {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      };

      const response = await fetch(`https://c1yi9fd6kc.execute-api.eu-north-1.amazonaws.com/dev${endpoint}`, {
        ...defaultOptions,
        ...options,
      });
      return response;
    } catch (error) {
      console.error('Authentication error:', error);
      throw new Error('Failed to authenticate request');
    }
  };

  return {
    authenticatedFetch,
  };
};
