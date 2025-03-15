<template>
  <div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <!-- Loading Overlay -->
    <div v-if="isLoading" class="fixed inset-0 bg-gray-900 bg-opacity-90 z-50 flex items-center justify-center">
      <div class="flex flex-col items-center">
        <div class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-blue-400 mb-4"></div>
        <p class="text-blue-400 text-lg">Loading user data...</p>
      </div>
    </div>

    <!-- Error Alert -->
    <div v-if="showError" class="fixed top-4 right-4 bg-red-500 text-white px-6 py-4 rounded-lg shadow-lg z-50">
      {{ errorMessage }}
    </div>

    <!-- Main Content -->
    <div v-if="!isLoading" class="w-full max-w-4xl p-6 rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold text-center mb-4">{{ username }} aka {{ name }} Program Management</h2>
      <div class="bg-gray-700 p-4 rounded-lg flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
        <!-- First Dropdown -->
        <select v-model="selectedOption1" class="w-full md:w-1/2 p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
          <option value="" disabled>Select Block</option>
          <option v-for="option in options1" :key="option.id" :value="option.id">
            {{ option.label }}
          </option>
        </select>

        <!-- Second Dropdown -->
        <select v-model="selectedOption2" class="w-full md:w-1/2 p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
          <option value="" disabled>Select Week</option>
          <option v-for="option in filteredOptions2" :key="option.id" :value="option.id">
            {{ option.label }}
          </option>
        </select>
      </div>
      <UserManagement 
        @add-block="handleAddBlock" 
        @add-week="handleAddWeek" 
        @add-day="handleAddDay"
      />
      <TrainingDisplay 
        :items="filteredOptions3"
        @delete-exercise="handleDeleteExercise"
        @exercise-added="handleAddExercise"
      />
    </div>
  </div>
</template>

<script setup>
import UserManagement from '~/components/admin/UserManagement.vue';
import TrainingDisplay from '~/components/admin/TrainingDisplay.vue';
import { ref, computed, watch, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useLabelsStore } from '~/stores/labels';
import { useApi } from '~/composables/useApi';
import { addBlock, addWeek, addDay, addExercise, deleteExercise } from '~/composables/updateProgram';
import { useBlockInformation } from '~/composables/getBlockInformation';
import { useAthleteManagement } from '~/composables/manageAthletes';

const username = ref("");
const name = ref("");
const route = useRoute();
const userId = route.params.id;
const { getAllBlocks, getDaysByWeek } = useBlockInformation();
const { fetchAthlete } = useAthleteManagement();

definePageMeta({ middleware: ['auth-admin'] });

// Add these for blocks management
const options1 = ref([]);
const selectedOption1 = ref("");
const isLoading = ref(false);

// Load blocks when page loads
onMounted(async () => {
  isLoading.value = true;
  try {
    console.log("Fetching athlete and blocks... " + userId);
    const athlete = await fetchAthlete(userId);
    if (athlete) {
      console.log(athlete)
      username.value = athlete[0].username;
      name.value = athlete[0].name;
    }
    
    const blocks = await getAllBlocks(userId);
    if (!blocks.error) {
      options1.value = Object.entries(blocks).map(([name, weeks]) => ({
        id: name,
        label: name,
        weeks: weeks
      }));
      selectedOption1.value = options1.value.length ? options1.value[0].id : "";
    }
  } catch (error) {
    console.error('Error loading blocks:', error);
    errorMessage.value = 'Failed to load blocks';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  } finally {
    isLoading.value = false;
  }
});

const messageOpen = ref(false);
const allSets = ref(0);
const labelColor = ref("");

// Replace weeksStore and options2 computed with this:
const options2 = computed(() => {
  const selectedBlock = options1.value.find(block => block.id === selectedOption1.value);
  if (!selectedBlock) return [];
  
  return selectedBlock.weeks.slice().reverse().map(weekId => ({
    id: weekId,
    label: weekId
  }));
});

// Remove filteredOptions2 ref and watch, replace with this:
const filteredOptions2 = computed(() => options2.value);

const selectedOption2 = computed(() => {
  return filteredOptions2.value.length ? filteredOptions2.value[0].id : "";
});

const labelsStore = useLabelsStore();
const labels = computed(() => labelsStore.labels);

function countSetsPerWeek(label) {
  trainingStore.countSetsPerWeek(label, selectedOption1.value, selectedOption2.value, allSets, messageOpen);
  labelColor.value = labelsStore.getColorByLabel(label);
}

function getLabelColor(label) {
  return labelsStore.getColorByLabel(label);
}

function toggleMessage() {
  messageOpen.value = !messageOpen.value;
}

const filteredOptions3 = ref([]);
watch([selectedOption1, selectedOption2], async ([newBlock, newWeek]) => {
  if (newBlock && newWeek) {
    const response = await getDaysByWeek(userId, newBlock, newWeek);
    if (!response.error) {
      filteredOptions3.value = Object.entries(response).map(([dayId, dayData]) => ({
        title: dayId,
        content: dayData.Exercises || []
      }));
    }
  } else {
    filteredOptions3.value = [];
  }
}, { immediate: true });

const activeIndex = ref(null);

const toggle = (index) => {
  activeIndex.value = activeIndex.value === index ? null : index;
  messageOpen.value = false;
};

const newExerciseName = ref("");
const newExerciseLabel = ref("");
const newExerciseSets = ref(0);
const newExerciseReps = ref(0);
const newExerciseRpe = ref(0);
const newExerciseComments = ref("");

// Add these refs near the top with other refs
const errorMessage = ref("");
const showError = ref(false);

async function handleAddExercise(exerciseData) {
  const { dayId, ...exercise } = exerciseData;
  
  try {
    const result = await addExercise(
      userId,
      selectedOption1.value,
      selectedOption2.value,
      dayId,
      {
        name: String(exercise.name),
        label: String(exercise.label),
        sets: String(exercise.sets),
        reps: String(exercise.reps),
        rpe: String(exercise.rpe),
        comments: String(exercise.comments)
      }
    );
    
    if (result.error) {
      errorMessage.value = result.error;
      showError.value = true;
      setTimeout(() => { showError.value = false; }, 3000);
      return;
    }

    // Refresh days after adding exercise
    const days = await getDaysByWeek(userId, selectedOption1.value, selectedOption2.value);
    if (!days.error) {
      filteredOptions3.value = Object.entries(days).map(([dayId, dayData]) => ({
        title: dayId,
        content: dayData.Exercises || []
      }));
    }
  } catch (error) {
    console.error('Error in handleAddExercise:', error);
    errorMessage.value = error.message || 'An error occurred while adding the exercise';
    showError.value = true;
    setTimeout(() => { showError.value = false; }, 3000);
  }
}

async function handleDeleteExercise(dayIndex, exerciseIndex) {
  const day = filteredOptions3.value[dayIndex];
  if (!day || !day.content[exerciseIndex]) {
    errorMessage.value = "Exercise not found";
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
    return;
  }

  const exercise = day.content[exerciseIndex];

  try {
    const result = await deleteExercise(
      userId,
      selectedOption1.value,
      selectedOption2.value,
      day.title,
      exercise.name,
      exercise.label
    );

    if (result.error) {
      errorMessage.value = result.error;
      showError.value = true;
      setTimeout(() => {
        showError.value = false;
      }, 3000);
      return;
    }

    // Refresh days after deleting exercise
    const days = await getDaysByWeek(userId, selectedOption1.value, selectedOption2.value);
    if (!days.error) {
      filteredOptions3.value = Object.entries(days).map(([dayId, dayData]) => ({
        title: dayId,
        content: dayData.Exercises || []
      }));
    }
  } catch (error) {
    console.error('Error in deleteExercise:', error);
    errorMessage.value = error.message || 'An error occurred while deleting the exercise';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  }
}

const newBlockLabel = ref("");
const { authenticatedFetch } = useApi();

async function handleAddBlock(blockLabel) {
  if (!blockLabel) {
    errorMessage.value = "Block name is required";
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
    return;
  }

  try {
    const result = await addBlock(userId, blockLabel);
    if (result.error) {
      errorMessage.value = result.error;
      showError.value = true;
      setTimeout(() => {
        showError.value = false;
      }, 3000);
      return;
    }
    
    // Refresh blocks after adding
    const blocks = await getAllBlocks(userId);
    if (!blocks.error) {
      options1.value = Object.entries(blocks).map(([name, weeks]) => ({
        id: name,
        label: name,
        weeks: weeks
      }));
      // Set the newly added block as selected
      selectedOption1.value = blockLabel;
      selectedOption2.value = ""; // Reset week selection
    }
  } catch (error) {
    console.error('Error in handleAddBlock:', error);
    errorMessage.value = error.message || 'An error occurred while adding the block';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  }
}

async function handleAddWeek(weekTitle) {
  try {
    const result = await addWeek(userId, selectedOption1.value, weekTitle);
    if (result.error) {
      errorMessage.value = result.error;
      showError.value = true;
      setTimeout(() => {
        showError.value = false;
      }, 3000);
      return;
    }
    
    // Refresh blocks to get updated weeks
    const blocks = await getAllBlocks(userId);
    if (!blocks.error) {
      options1.value = Object.entries(blocks).map(([name, weeks]) => ({
        id: name,
        label: name,
        weeks: weeks
      }));
      // Keep same block selected
      selectedOption1.value = selectedOption1.value;
      // Set the newly added week as selected
      selectedOption2.value = weekTitle;
    }
  } catch (error) {
    console.error('Error in handleAddWeek:', error);
    errorMessage.value = error.message || 'An error occurred while adding the week';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  }
}

async function handleAddDay(dayTitle) {
  try {
    const result = await addDay(userId, selectedOption1.value, selectedOption2.value, dayTitle);
    if (result.error) {
      errorMessage.value = result.error;
      showError.value = true;
      setTimeout(() => {
        showError.value = false;
      }, 3000);
      return;
    }

    // Fetch updated days after adding new day
    const days = await getDaysByWeek(userId, selectedOption1.value, selectedOption2.value);
    if (!days.error) {
      filteredOptions3.value = Object.entries(days).map(([dayId, dayData]) => ({
        title: dayId,
        content: dayData.Exercises || []
      }));
    }
  } catch (error) {
    console.error('Error in handleAddDay:', error);
    errorMessage.value = error.message || 'An error occurred while adding the day';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  }
}

const manageOpen = ref(false);

function toggleManage() {
  manageOpen.value = !manageOpen.value;
}
</script>

<style scoped>
.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
