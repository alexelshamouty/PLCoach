import { useApi } from './useApi';
import { useTrainingStore } from '~/stores/training';
import { useAthleteStore } from '~/stores/athlete';

const BASE_URL = 'https://j1v6bnyoh2.execute-api.eu-north-1.amazonaws.com/dev/updateAddBlock';

const getStores = () => ({
  athleteStore: useAthleteStore(),
  trainingStore: useTrainingStore(),
  api: useApi()
});

export const addBlock = async (userId, newBlockLabel) => {
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      BASE_URL,
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
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      BASE_URL,
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
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      BASE_URL,
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
  const { trainingStore, api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      BASE_URL,
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

    trainingStore.addExercise(weekId, dayId, exercise);
    return { success: true };
  } catch (error) {
    console.error('Error adding exercise:', error);
    return {
      error: error.message || 'An unexpected error occurred'
    };
  }
};

export const deleteExercise = async (userId, blockId, weekId, dayId, exerciseName, exerciseLabel) => {
  const { api } = getStores();
  
  try {
    const response = await api.authenticatedFetch(
      BASE_URL,
      {
        method: 'POST',
        body: JSON.stringify({
          action: 'deleteExercise',
          userId,
          blockId,
          weekId,
          dayId,
          exerciseName,
          exerciseLabel
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
