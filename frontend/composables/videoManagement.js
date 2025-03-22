import { useState } from '#app';
import { useApi } from './useApi';
import { API_URLS } from './config';

export const useVideoManagement = () => {
  const loading = useState('videoManagement.loading', () => false);
  const error = useState('videoManagement.error', () => null);
  
  const getAPI = () => ({
    api: useApi()
  });
  
  /**
   * Fetch videos for a specific exercise
   */
  const getVideos = async ({ userID, blockName, week, dayId, exerciseName }) => {
    loading.value = true;
    try {
      const { api } = getAPI();
      const queryParams = new URLSearchParams({
        userID,
        blockName,
        week,
        dayId,
        exerciseName
      }).toString();
  
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/getVideos?${queryParams}`,
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
   * Helper function to sanitize a filename
   */
  const sanitizeFilename = (filename) => {
    // Remove special characters and spaces
    return filename
      .replace(/[^\w\s.-]/g, '')
      .replace(/\s+/g, '_')
      .toLowerCase();
  };

  /**
   * Helper function to handle pre-signed URL upload process
   * This combines the common logic for handling the presigned URL upload
   */
  const handlePresignedUpload = async (formData, presignedData, videoType) => {
    const { api } = getAPI();
    
    // Extract data from the form
    const file = formData.get('file');
    const type = formData.get('type');
    const title = formData.get('title');
    const description = formData.get('description');
    const dayId = formData.get('dayId');
    const exerciseName = formData.get('exerciseName');
    const exerciseLabel = formData.get('exerciseLabel');
    const block = formData.get('block');
    const week = formData.get('week');
    
    // Parse the body from the response
    const { url, fields, s3Key } = presignedData;
    
    // Prepare form data for S3 upload
    const s3FormData = new FormData();
    
    // Add all the fields from the pre-signed URL (ensure fields is valid)
    if (fields && typeof fields === 'object') {
      Object.entries(fields).forEach(([key, value]) => {
        s3FormData.append(key, value);
      });
    }
    
    // Add the file content last
    s3FormData.append('file', file);
    // Log the contents of s3FormData
    for (const [key, value] of s3FormData.entries()) {
      console.log(`${key}: ${value}`);
    }
    
    // Upload directly to S3 using the pre-signed URL
    const uploadResponse = await fetch(url, {
      method: 'POST',
      body: s3FormData
    });
    
    if (!uploadResponse.ok) {
      throw new Error(`Upload failed: ${await uploadResponse.text()}`);
    }
    
    // After successful upload to S3, notify our backend
    const queryParams = new URLSearchParams({
      userID: formData.get('userId'),
      s3Key: s3Key,
      title: title,
      filetype: file.type,
      description: description,
      dayId: dayId,
      exerciseName: exerciseName,
      exerciseLabel: exerciseLabel,
      block: block,
      week: week,
      type: type,
    }).toString();
    
    const finalizeResponse = await api.authenticatedFetch(
      `${API_URLS.VIDEO_MANAGEMENT_API}/finalizeUpload?${queryParams}`,
      {
        method: 'POST'
      }
    );
    
    if (!finalizeResponse.ok) {
      throw new Error(`Finalize upload failed: ${await finalizeResponse.text()}`);
    }
    
    return await finalizeResponse.json();
  };

  /**
   * Upload a new video
   */
  const uploadVideo = async (formData) => {
    loading.value = true;
    try {
      const { api } = getAPI();
      
      // Extract data for generating the presigned URL
      const title = formData.get('title');
      const type = formData.get('type');
      const filename = formData.get('filename');
      const description = formData.get('description');
      const block = formData.get('block');
      const week = formData.get('week');
      const dayId = formData.get('dayId');
      const exerciseName = formData.get('exerciseName');
      const exerciseLabel = formData.get('exerciseLabel');
      const userId = formData.get('userId'); // Extract userId from formData
      const file = formData.get('file');
      const contentType = file.type;
      
      // Create the exercise path
      const exercise_path = `${block}#${week}#${dayId}#${exerciseName}#${exerciseLabel}`;
      
      // Sanitize filename
      const sanitizedFilename = sanitizeFilename(filename);
      
      // Construct query parameters
      const queryParams = new URLSearchParams({
        userID: userId,
        filename: sanitizedFilename,
        title: title,
        exercise_path: exercise_path,
        comment: description,
        contentType: contentType,
        type: type,
      }).toString();
      
      // Call the API endpoint with query parameters
      const presignedUrlResponse = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/uploadVideo?${queryParams}`,
        {
          method: 'POST'
        }
      );
      const presignedData = await presignedUrlResponse.json();
      console.log('Presigned URL response:', presignedData);
      // Handle the upload using the helper function
      return await handlePresignedUpload(formData, presignedData);
    } catch (err) {
      error.value = err.message || 'An error occurred';
      throw err;
    } finally {
      loading.value = false;
    }
  };
  
  /**
   * Delete a video
   */
  const deleteVideo = async (videoId) => {
    loading.value = true;
    try {
      const { api } = getAPI();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/deleteVideo/${videoId}`,
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
   * Update a video
   */
  const updateVideo = async (videoId, data) => {
    loading.value = true;
    try {
      const { api } = getAPI();
      
      const response = await api.authenticatedFetch(
        `${API_URLS.VIDEO_MANAGEMENT_API}/updateVideo/${videoId}`,
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
    getVideos, // Updated method
    uploadVideo,
    deleteVideo,
    updateVideo,
    resetLoadingState,
    sanitizeFilename
  };
};
