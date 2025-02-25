import { useAuthStore } from '~/stores/auth';

export const useApi = () => {
  const authStore = useAuthStore();

  const authenticatedFetch = async (endpoint, options = {}) => {
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

    return fetch(`https://r7q30loqre.execute-api.eu-north-1.amazonaws.com/dev/${endpoint}`, {
      ...defaultOptions,
      ...options,
    });
  };

  return {
    authenticatedFetch,
  };
};
