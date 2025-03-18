import { ref } from 'vue';
import { useApi } from './useApi';
import { API_URLS } from './config';

export const useAthleteManagement = () => {
  const athletes = ref([]);
  const loading = ref(false);
  const error = ref(null);
  const { authenticatedFetch } = useApi();

  const mapUser = (userData) => ({
    id: userData.Userid,
    timeStamp: userData.Timestamp,
    username: userData.Preferred_username,
    name: userData.Name,
    email: userData.Email,
    weight: userData.Weight,
    gender: userData.Gender
  });

  const fetchAthletes = async () => {
    loading.value = true;
    error.value = null;
    try {
      const response = await authenticatedFetch(API_URLS.USERS_API, { method: 'GET' });
      const data = await response.json();

      if (!data || !data.body || !Array.isArray(data.body)) {
        throw new Error('Invalid response format');
      }

      athletes.value = data.body.map(mapUser);
    } catch (e) {
      error.value = e.message;
      console.error('Error fetching athletes:', e);
    } finally {
      loading.value = false;
    }
  };

  const fetchAthlete = async (userId) => {
    loading.value = true;
    error.value = null;
    try {
        console.log("Fetching athlete with id: ", userId);
      const response = await authenticatedFetch(
        `${API_URLS.GET_USER_API}?userId=${userId}`,
        { method: 'GET' }
      );
      const data = await response.json();
      console.log(data);
      if (response.status !== 200 || !data || !data.body) {
        throw new Error(data.error || 'Failed to fetch athlete');
      }

      return data.body.map(mapUser);
    } catch (e) {
      error.value = e.message;
      console.error('Error fetching athlete:', e);
      return null;
    } finally {
      loading.value = false;
    }
  };

  return {
    athletes,
    loading,
    error,
    fetchAthletes,
    fetchAthlete
  };
};
