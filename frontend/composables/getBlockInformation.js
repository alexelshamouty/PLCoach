import { useApi } from './useApi';

const BASE_URL = 'https://deecu3zbcl.execute-api.eu-north-1.amazonaws.com/dev/getBlockInformation';

export const useBlockInformation = () => {
  const { authenticatedFetch } = useApi();

  const getAllBlocks = async (userId) => {
    try {
      const response = await authenticatedFetch(
        `${BASE_URL}?action=getAllBlocks&userId=${userId}`,
        { method: 'GET' }
      );

      const data = await response.json();
      if (response.status !== 200) {
        return { error: data.error || 'Failed to fetch blocks' };
      }

      return data.blocks;
    } catch (error) {
      console.error('Error fetching blocks:', error);
      return { error: error.message || 'An unexpected error occurred' };
    }
  };

  const getDaysByWeek = async (userId, blockId, weekId) => {
    try {
      const response = await authenticatedFetch(
        `${BASE_URL}?action=getDaysByWeek&userId=${userId}&blockId=${blockId}&weekId=${weekId}`,
        { method: 'GET' }
      );

      const data = await response.json();
      if (response.status !== 200) {
        return { error: data.error || 'Failed to fetch days' };
      }

      return data.days;
    } catch (error) {
      console.error('Error fetching days:', error);
      return { error: error.message || 'An unexpected error occurred' };
    }
  };

  return {
    getAllBlocks,
    getDaysByWeek
  };
};
