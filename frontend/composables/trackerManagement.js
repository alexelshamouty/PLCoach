import { useApi } from './useApi';

const BASE_URL = 'https://hehvg40uyl.execute-api.eu-north-1.amazonaws.com/dev';

const getStores = () => ({
  api: useApi()
});

export const createTemplate = async (templateData) => {
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      `${BASE_URL}/createTracker`,
      {
        method: 'POST',
        body: JSON.stringify(templateData)
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to create template'
      };
    }

    return { success: true, data };
  } catch (error) {
    console.error('Error creating template:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const updateTemplate = async (templateData) => {
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      `${BASE_URL}/updateTracker`,
      {
        method: 'POST',
        body: JSON.stringify(templateData)
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to update template'
      };
    }

    return { success: true, data };
  } catch (error) {
    console.error('Error updating template:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};