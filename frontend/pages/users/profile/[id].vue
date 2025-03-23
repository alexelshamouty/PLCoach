<template>
  <div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <LoadingOverlay :show="isLoading" />
    <ErrorAlert :message="error" @clear="error = null" />
    
    <!-- Main Content -->
    <div v-if="!isLoading" class="w-full max-w-4xl p-6 rounded-lg shadow-md">
      <!-- New User Info Card -->
      <div class="bg-gray-800 rounded-xl p-6 mb-6 shadow-lg">
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-3xl font-bold text-blue-400">{{ athlete?.name }}</h1>
            <div class="mt-2 space-y-1">
                <p class="text-gray-300">
                  <span class="font-semibold text-blue-400">Gender:</span> 
                  <span class="ml-2 capitalize text-yellow-400">{{ athlete?.gender }}</span>
                </p>
                <p class="text-gray-300">
                  <span class="font-semibold text-blue-400">Weight:</span> 
                  <span class="ml-2 text-yellow-400">{{ athlete?.weight }} kg</span>
                </p>
                <p class="text-gray-300">
                  <span class="font-semibold text-blue-400">Email:</span> 
                  <span class="ml-2 text-yellow-400">{{ athlete?.email }}</span>
                </p> 
            </div>
          </div>
          <!-- Updated Avatar Section -->
          <div class="relative group">
            <button type="button"
                    class="bg-gray-700 rounded-full p-4 cursor-pointer hover:bg-gray-600 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    @click="openFileDialog"
                    :disabled="uploadingPhoto">
              <div class="relative w-16 h-16">
                <img v-if="athlete?.photo_url" 
                     :src="athlete.photo_url" 
                     class="w-full h-full rounded-full object-cover"
                     alt="Profile photo" />
                <img v-else src="https://d2cu7vju76n2na.cloudfront.net/powerfull-duck.webp" class="w-16 h-16 rounded-full object-cover" alt="Default profile photo" />
                <div class="absolute inset-0 bg-black bg-opacity-50 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-200">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
              </div>
            </button>
            <input type="file" 
                   ref="fileInput" 
                   class="hidden" 
                   accept="image/*"
                   @change="handleFileUpload" />
          </div>
        </div>
      </div>

      <h2 class="text-2xl font-semibold text-center mb-4">Athlete {{ username }} Profile</h2>
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
      <!-- Training -->
      <TrainingSchedule 
        :days="filteredOptions3"
        :block="selectedOption1"
        :week="selectedOption2"
        @exercise-click="openDialog"
        @day-finished="dayFinished"
      />
      <!-- Dialog -->
      <ExerciseDialog
        v-model="dialogOpen"
        :exercise="selectedExercise.originalExercise"
        @submit="handleExerciseUpdate"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import LoadingOverlay from '~/components/shared/LoadingOverlay.vue';
import ErrorAlert from '~/components/shared/ErrorAlert.vue';
import { useRoute } from "vue-router";
import { useApi } from '~/composables/useApi';
import { useAthleteManagement } from '~/composables/manageAthletes';
import { useBlockInformation } from '~/composables/getBlockInformation';
import { updateExercise } from '~/composables/updateProgram';
import TrainingSchedule from '~/components/TrainingSchedule.vue';
import ExerciseDialog from '~/components/ExerciseDialog.vue';

async function dayFinished({ index, dayId }) {
  /*
  #TODO
  #Now we need to start thinking about our leaderboard! How do we want to structure this? Per block? Per week? Number of finished workouts?
  */
  try {
    console.log(`Day ${dayId} finished at index ${index}`, {
      userId,
      weekId: selectedOption2.value,
      blockId: selectedOption1.value
    });
    // TODO: Implement the API call to mark the day as finished
  } catch (e) {
    error.value = e.message || "Failed to mark day as finished";
  }
}

const athlete = ref(null);
const username = ref("");
const route = useRoute();
const userId = route.params.id;
const { getAllBlocks, getDaysByWeek } = useBlockInformation();
const { fetchAthlete } = useAthleteManagement();

// Keep other refs
const error = ref(null);
const fileInput = ref(null);
const uploadingPhoto = ref(false);
const options1 = ref([]);
const selectedOption1 = ref("");
const isLoading = ref(true);

onMounted(async () => {
  isLoading.value = true;
  try {
    const athleteData = await fetchAthlete(userId);
    if (athleteData && athleteData.length > 0) {
      athlete.value = athleteData[0];
      username.value = athlete.value.username;
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
  } catch (e) {
    error.value = e.message || "An error occurred while loading data";
  } finally {
    isLoading.value = false;
  }
});

const options2 = computed(() => {
  const selectedBlock = options1.value.find(block => block.id === selectedOption1.value);
  if (!selectedBlock) return [];
  
  return selectedBlock.weeks.slice().reverse().map(weekId => ({
    id: weekId,
    label: weekId
  }));
});

const filteredOptions2 = computed(() => options2.value || []);

const selectedOption2 = computed(() => {
  return filteredOptions2.value.length ? filteredOptions2.value[0].id : "";
});

const filteredOptions3 = ref([]);
watch([selectedOption1, selectedOption2], async ([newBlock, newWeek]) => {
  if (newBlock && newWeek) {
    const response = await getDaysByWeek(userId, newBlock, newWeek);
    if (!response.error) {
      filteredOptions3.value = Object.entries(response).map(([dayId, dayData]) => ({
        title: dayId,
        content: dayData.Exercises || [],
        // Add dayIndex as index, default to 999 if not provided
        index: dayData.dayIndex ? parseInt(dayData.dayIndex, 10) : 999
      }));
      
      // Sort based on index
      filteredOptions3.value.sort((a, b) => a.index - b.index);
    }
  } else {
    filteredOptions3.value = [];
  }
}, { immediate: true });

const dialogOpen = ref(false);
const selectedExercise = ref({
  originalExercise: {},
  dayIndex: null
});

function openDialog(exercise, dayIndex) {
  selectedExercise.value = {
    originalExercise: exercise,
    dayIndex
  };
  dialogOpen.value = true;
}

async function handleExerciseUpdate({ sets, comments }) {
  const currentDay = filteredOptions3.value[selectedExercise.value.dayIndex];
  const exercise = selectedExercise.value.originalExercise;
  
  // Optimistically update the UI
  const updatedExercise = {
    ...exercise,
    results: {
      sets,
      comments
    }
  };
  
  // Update local state immediately
  const exerciseIndex = currentDay.content.findIndex(e => e.name === exercise.name);
  
  if (exerciseIndex !== -1) {
    currentDay.content[exerciseIndex] = updatedExercise;
  }

  try {
    const result = await updateExercise(
      userId,
      selectedOption1.value,
      selectedOption2.value,
      currentDay.title,
      exercise.name,
      sets,
      comments
    );

    if (result.error) {
      throw new Error(result.error);
    }
  } catch (e) {
    // Revert the optimistic update on error
    if (exerciseIndex !== -1) {
      currentDay.content[exerciseIndex] = exercise;
    }
    error.value = e.message || 'Failed to update exercise';
    console.error('Error updating exercise:', e);
  }
}

function openFileDialog() {
  console.log('Opening file dialog');
  if (!uploadingPhoto.value) {
    fileInput.value?.click();
  }
}

async function handleFileUpload(event) {
  const file = event.target.files[0];
  if (!file) return;

  if (!file.type.startsWith('image/')) {
    error.value = 'Please upload an image file';
    return;
  }

  if (file.size > 5 * 1024 * 1024) {
    error.value = 'File size should be less than 5MB';
    return;
  }

  uploadingPhoto.value = true;
  error.value = null;

  try {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('userId', userId);

    const response = await authenticatedFetch('https://o82i4pdcmg.execute-api.eu-north-1.amazonaws.com/dev/uploadPhoto', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('Failed to upload image');
    }

    const updatedAthlete = await fetchAthlete(userId);
    if (updatedAthlete) {
      athlete.value = updatedAthlete;
    }
  } catch (e) {
    error.value = e.message || 'Failed to upload image. Please try again.';
    console.error('Error uploading file:', e);
  } finally {
    uploadingPhoto.value = false;
    event.target.value = '';
  }
}

// Watch for changes in selectedOption1 and selectedOption2
watch([selectedOption1, selectedOption2], ([newBlock, newWeek]) => {
  if (newBlock && newWeek) {
    currentBlock.value = newBlock;
    currentWeek.value = newWeek;
  }
}, { immediate: true });

const currentBlock = ref('');
const currentWeek = ref('');
</script>

<style scoped>
.group:hover .group-hover\:opacity-100 {
  opacity: 1;
}

.animate-fade-in {
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
