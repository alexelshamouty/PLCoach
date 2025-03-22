import { useState } from '#app';
import { useApi } from './useApi';
import { API_URLS } from './config';

export const useVideoManagement = () => {
  const loading = useState('videoManagement.loading', () => false);
  const error = useState('videoManagement.error', () => null);
  
  const getStores = () => ({
    api: useApi()
  });
  
  /**
   * List videos uploaded by regular users (athletes)
   */
  const listUserVideos = async (params = {}) => {
    loading.value = true;
    try {
      const { api } = getStores();
      const queryParams = new URLSearchParams({ 
        type: 'athlete',
        ...params
      }).toString();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/listVideos?${queryParams}`,
        { method: 'GET' }
      );
      const data = await response.json();
      return data;
    } catch (err) {
      error.value = err.message || 'An error occurred';
      return [];
    } finally {
      loading.value = false;
    }
  };
  
  /**
   * List videos uploaded by coaches
   */
  const listCoachVideos = async (params = {}) => {
    loading.value = true;
    try {
      const { api } = getStores();
      const queryParams = new URLSearchParams({ 
        type: 'coach',
        ...params
      }).toString();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/listVideos?${queryParams}`,
        { method: 'GET' }
      );
      const data = await response.json();
      return data;
    } catch (err) {
      error.value = err.message || 'An error occurred';
      return [];
    } finally {
      loading.value = false;
    }
  };
  
  /**
   * Upload a new user/athlete video
   */
  const uploadUserVideo = async (formData) => {
    loading.value = true;
    try {
      const { api } = getStores();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/uploadUserVideo`,
        {
          method: 'POST',
          body: formData
        }
      );
      const data = await response.json();
      return data;
    } catch (err) {
      error.value = err.message || 'An error occurred';
      throw err;
    } finally {
      loading.value = false;
    }
  };
  
  /**
   * Upload a new coach video
   */
  const uploadCoachVideo = async (formData) => {
    loading.value = true;
    try {
      const { api } = getStores();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/uploadCoachVideo`,
        {
          method: 'POST',
          body: formData
        }
      );
      const data = await response.json();
      return data;
    } catch (err) {
      error.value = err.message || 'An error occurred';
      throw err;
    } finally {
      loading.value = false;
    }
  };
  
  /**
   * Delete a user/athlete video
   */
  const deleteUserVideo = async (videoId) => {
    loading.value = true;
    try {
      const { api } = getStores();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/deleteVideo/${videoId}?type=athlete`,
        { method: 'DELETE' }
      );
      const data = await response.json();
      return data;
    } catch (err) {
      error.value = err.message || 'An error occurred';
      throw err;
    } finally {
      loading.value = false;
    }
  };
  
  /**
   * Delete a coach video
   */
  const deleteCoachVideo = async (videoId) => {
    loading.value = true;
    try {
      const { api } = getStores();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/deleteVideo/${videoId}?type=coach`,
        { method: 'DELETE' }
      );
      const data = await response.json();
      return data;
    } catch (err) {
      error.value = err.message || 'An error occurred';
      throw err;
    } finally {
      loading.value = false;
    }
  };
  
  /**
   * Update a user/athlete video
   */
  const updateUserVideo = async (videoId, data) => {
    loading.value = true;
    try {
      const { api } = getStores();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/updateVideo/${videoId}?type=athlete`,
        {
          method: 'PUT',
          body: JSON.stringify(data)
        }
      );
      const responseData = await response.json();
      return responseData;
    } catch (err) {
      error.value = err.message || 'An error occurred';
      throw err;
    } finally {
      loading.value = false;
    }
  };
  
  /**
   * Update a coach video
   */
  const updateCoachVideo = async (videoId, data) => {
    loading.value = true;
    try {
      const { api } = getStores();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/updateVideo/${videoId}?type=coach`,
        {
          method: 'PUT',
          body: JSON.stringify(data)
        }
      );
      const responseData = await response.json();
      return responseData;
    } catch (err) {
      error.value = err.message || 'An error occurred';
      throw err;
    } finally {
      loading.value = false;
    }
  };
  
  const resetLoadingState = () => {
    loading.value = false;
  };
  
  // Reset loading state on initial creation
  resetLoadingState();
  
  return {
    loading,
    error,
    listUserVideos,
    listCoachVideos,
    uploadUserVideo,
    uploadCoachVideo,
    deleteUserVideo,
    deleteCoachVideo,
    updateUserVideo,
    updateCoachVideo,
    resetLoadingState
  };
};
