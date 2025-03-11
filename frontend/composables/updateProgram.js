import { useApi } from './useApi';
import { useBlocksStore } from '~/stores/blocks';
import { useWeeksStore } from '~/stores/weeks';
import { useTrainingStore } from '~/stores/training';
import { useAthleteStore } from '~/stores/athlete';

const BASE_URL = 'https://94rzvbb740.execute-api.eu-north-1.amazonaws.com/dev/updateAddBlock';

const getStores = () => ({
  blocksStore: useBlocksStore(),
  athleteStore: useAthleteStore(),
  weeksStore: useWeeksStore(),
  trainingStore: useTrainingStore(),
  api: useApi()
});

export const addBlock = async (userId, newBlockLabel, athlete) => {
  const { blocksStore, athleteStore, api } = getStores();
  
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

    if (!response.ok) {
      throw new Error('Failed to add block');
    }

    const data = await response.json();
    blocksStore.addBlock(newBlockLabel);
    const newBlock = blocksStore.blocks[blocksStore.blocks.length - 1];
    
    // Add null check for athlete
    if (athlete && athlete.id) {
      athleteStore.addBlockToAthlete(athlete.id, newBlock);
      return blocksStore.getBlocksByIds(athlete.blocks?.map(block => block.id) || []);
    }
    return [];

  } catch (error) {
    console.error('Error adding block:', error);
    throw error;
  }
};

export const addWeek = async (userId, blockId, newWeekId) => {
  const { weeksStore, api } = getStores();
  
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

    if (!response.ok) {
      throw new Error('Failed to add week');
    }

    const data = await response.json();
    weeksStore.addWeek(blockId, newWeekId);
  } catch (error) {
    console.error('Error adding week:', error);
    throw error;
  }
};

export const addDay = async (userId, blockId, weekId, newDayId) => {
  const { trainingStore, api } = getStores();
  
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

    if (!response.ok) {
      throw new Error('Failed to add day');
    }

    const data = await response.json();
    trainingStore.addDay(weekId, newDayId);
  } catch (error) {
    console.error('Error adding day:', error);
    throw error;
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

    if (!response.ok) {
      throw new Error('Failed to add exercise');
    }

    const data = await response.json();
    trainingStore.addExercise(weekId, dayId, exercise);
  } catch (error) {
    console.error('Error adding exercise:', error);
    throw error;
  }
};
