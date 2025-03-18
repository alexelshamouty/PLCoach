import { useApi } from './useApi';
import { API_URLS } from './config';

export const useBlockInformation = () => {
  const { authenticatedFetch } = useApi();

  const getAllBlocks = async (userId) => {
    try {
      const response = await authenticatedFetch(
        `${API_URLS.BLOCK_INFO_API}?action=getAllBlocks&userId=${userId}`,
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
        `${API_URLS.BLOCK_INFO_API}?action=getDaysByWeek&userId=${userId}&blockId=${blockId}&weekId=${weekId}`,
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
