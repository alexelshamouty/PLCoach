import { useApi } from './useApi';
import { API_URLS } from './config';

const getStores = () => ({
  api: useApi()
});

export const createTemplate = async (templateData) => {
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      `${API_URLS.TRACKER_API}/createTracker`,
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

  console.log('updateTemplate data:', templateData); // Log the data being sent

  try {
    const response = await api.authenticatedFetch(
      `${API_URLS.TRACKER_API}/updateTrackers`,
      {
        method: 'PUT',
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
      `${API_URLS.TRACKER_API}/getTrackers`,
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
      metrics: item.metrics // Remove mapping of Timestamp
    }));

    return { success: true, data: templates };
  } catch (error) {
    console.error('Error fetching templates:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const deleteTemplate = async (templateName) => {
  const { api } = getStores();
  
  console.log('deleteTemplate:', templateName);
  
  try {
    const response = await api.authenticatedFetch(
      `${API_URLS.TRACKER_API}/deleteTemplate?templateName=${encodeURIComponent(templateName)}`,
      {
        method: 'DELETE'
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to delete template'
      };
    }

    return { success: true, data };
  } catch (error) {
    console.error('Error deleting template:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};