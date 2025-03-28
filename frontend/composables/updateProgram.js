import { useApi } from './useApi';
import { API_URLS } from './config';

const getAPI = () => ({
  api: useApi()
});

export const addBlock = async (userId, newBlockLabel) => {
  const { api } = getAPI();
  
  try {
    const response = await api.authenticatedFetch(
      API_URLS.UPDATE_PROGRAM_API,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'addBlock',
          user_id: userId,
          blockName: newBlockLabel
        })
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to add block'
      };
    }

    return { success: true };
  } catch (error) {
    console.error('Error adding block:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const addWeek = async (userId, blockId, newWeekId) => {
  const { api } = getAPI();
  
  try {
    const response = await api.authenticatedFetch(
      API_URLS.UPDATE_PROGRAM_API,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'addWeek',
          userId,
          blockId,
          newWeekId
        })
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to add week'
      };
    }

    return { success: true };
  } catch (error) {
    console.error('Error adding week:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const addDay = async (userId, blockId, weekId, newDayId) => {
  const { api } = getAPI();
  
  try {
    const response = await api.authenticatedFetch(
      API_URLS.UPDATE_PROGRAM_API,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'addDay',
          userId,
          blockId,
          weekId,
          newDayId
        })
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to add day'
      };
    }

    return { success: true };
  } catch (error) {
    console.error('Error adding day:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const addExercise = async (userId, blockId, weekId, dayId, exercise) => {
  const { api } = getAPI();
  
  try {
    const response = await api.authenticatedFetch(
      API_URLS.UPDATE_PROGRAM_API,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'addExercise',
          userId,
          blockId,
          weekId,
          dayId,
          exercise: {
            name: exercise.name,
            label: exercise.label,
            sets: exercise.sets,
            reps: exercise.reps,
            rpe: exercise.rpe,
            comments: exercise.comments
          }
        })
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to add exercise'
      };
    }

    return { success: true };
  } catch (error) {
    console.error('Error adding exercise:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const deleteExercise = async (userId, blockId, weekId, dayId, exerciseName, exerciseLabel, dayIndex) => {
  const { api } = getAPI();
  
  try {
    const response = await api.authenticatedFetch(
      API_URLS.UPDATE_PROGRAM_API,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'deleteExercise',
          userId,
          blockId,
          weekId,
          dayId,
          exerciseName,
          exerciseLabel,
          dayIndex
        })
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to delete exercise'
      };
    }

    return { success: true };
  } catch (error) {
    console.error('Error deleting exercise:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const updateExercise = async (userId, blockId, weekId, dayId, exerciseName, sets, comments) => {
  const { api } = getAPI();
  
  try {
    const response = await api.authenticatedFetch(
      API_URLS.UPDATE_PROGRAM_API,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'updateExercise',
          userId,
          blockId,
          weekId,
          dayId,
          exerciseName,
          sets,
          comments
        })
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to update exercise'
      };
    }

    return { success: true };
  } catch (error) {
    console.error('Error updating exercise:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const exerciseUpdate = async (userId, blockId, weekId, dayId, exercise) => {
  const { api } = getAPI();
  
  try {
    const response = await api.authenticatedFetch(
      API_URLS.UPDATE_PROGRAM_API,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'exerciseUpdate',
          userId,
          blockId,
          weekId,
          dayId,
          exercise: {
            name: exercise.name,
            label: exercise.label,
            sets: exercise.sets,
            reps: exercise.reps,
            rpe: exercise.rpe,
            comments: exercise.comments
          }
        })
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to update exercise'
      };
    }

    return { success: true };
  } catch (error) {
    console.error('Error updating exercise:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const deleteDay = async (userId, blockId, weekId, dayId) => {
  const { api } = getAPI();
  
  try {
    const response = await api.authenticatedFetch(
      API_URLS.UPDATE_PROGRAM_API,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'deleteDay',
          userId,
          blockId,
          weekId,
          dayId
        })
      }
    );

    const data = await response.json();
    
    if (response.status !== 200) {
      return {
        error: data.error || 'Failed to delete day'
      };
    }

    return { success: true };
  } catch (error) {
    console.error('Error deleting day:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};
