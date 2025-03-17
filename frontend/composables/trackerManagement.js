import { useApi } from './useApi';

const CREATE_URL = 'https://hehvg40uyl.execute-api.eu-north-1.amazonaws.com/dev';
const GET_URL = 'https://cjmc559rhg.execute-api.eu-north-1.amazonaws.com/dev';
const UPDATE_URL = 'https://lh6jm1r61f.execute-api.eu-north-1.amazonaws.com/dev';

const getStores = () => ({
  api: useApi()
});

export const createTemplate = async (templateData) => {
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      `${CREATE_URL}/createTracker`,
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
      `${UPDATE_URL}/updateTracker`,
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

export const getTrackers = async () => {
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      `${GET_URL}/getTrackers`,
      {
        method: 'GET'
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to fetch templates'
      };
    }

    console.log(data)

    // Transform the data to match our frontend structure
    const templates = data.map(item => ({
      TemplateName: item.TemplateName,
      metrics: item.metrics
    }));

    return { success: true, data: templates };
  } catch (error) {
    console.error('Error fetching templates:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};