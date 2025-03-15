import { ref } from 'vue';
import { useApi } from './useApi';

const USERS_URL = 'https://c1yi9fd6kc.execute-api.eu-north-1.amazonaws.com/dev/users';
const GET_USER_URL = 'https://6yztzyjul9.execute-api.eu-north-1.amazonaws.com/dev/getUser';

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
      const response = await authenticatedFetch(USERS_URL, { method: 'GET' });
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
        `${GET_USER_URL}?userId=${userId}`,
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
