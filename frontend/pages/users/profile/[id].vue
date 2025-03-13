<template>
  <div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <!-- Error Alert -->
    <div v-if="error" class="fixed top-4 right-4 bg-red-500 text-white px-6 py-4 rounded-lg shadow-lg z-50 animate-fade-in">
      <div class="flex items-center space-x-2">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span>{{ error }}</span>
        <button @click="error = null" class="ml-4 hover:text-gray-200">×</button>
      </div>
    </div>

    <div class="w-full max-w-4xl p-6 rounded-lg shadow-md">
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
      <div class="bg-gray-900 text-white p-6 rounded-lg shadow-md mt-4">
        <div v-for="(item, index) in filteredOptions3" :key="index" class="border-b border-gray-600">
          <button @click="toggle(index)" class="w-full flex justify-between items-center p-4 focus:outline-none">
            <span class="font-semibold">{{ item.title }}</span>
            <span :class="{'rotate-180': activeIndex === index}" class="transition-transform duration-300">
              ⬇️
            </span>
          </button>
          <div v-if="activeIndex === index" class="p-4 text-gray-300">
            <table class="w-full border-collapse text-sm">
              <thead>
                <tr class="bg-gray-800 text-gray-300">
                  <th class="py-2 px-4 text-left">Exercise</th>
                  <th class="py-2 px-4 text-left">Label</th>
                  <th class="py-2 px-4 text-center">Sets</th>
                  <th class="py-2 px-4 text-center">Reps</th>
                  <th class="py-2 px-4 text-center">RPE</th>
                  <th class="py-2 px-4 text-center">Comments</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(exercise, i) in item.content" :key="i" class="border-b border-gray-700 hover:bg-gray-800">
                  <td class="py-2 px-4">
                    <button 
                      @click="openDialog(exercise)"
                      class="text-left hover:text-blue-400 transition-colors duration-200 cursor-pointer w-full">
                      {{ exercise.name }}
                    </button>
                  </td>
                  <td class="py-2 px-4">
                    <button :style="{ backgroundColor: getLabelColor(exercise.label) }" class="text-black px-4 py-2 rounded-full hover:opacity-75 transition">
                      {{ exercise.label }}
                    </button>
                  </td>
                  <td class="py-2 px-4 text-center">{{ exercise.sets }}</td>
                  <td class="py-2 px-4 text-center">{{ exercise.reps }}</td>
                  <td class="py-2 px-4 text-center font-semibold text-yellow-400">{{ exercise.rpe }}</td>
                  <td class="py-2 px-4 text-center font-semibold text-yellow-400">{{ exercise.comments }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <!-- Dialog -->
      <div v-if="dialogOpen" class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
        <div class="bg-gray-800 bg-opacity-90 p-6 rounded-2xl shadow-lg w-full max-w-2xl">
          <p class="mb-4 text-gray-300 text-center">Comments from coach:</p>
          <p class="mb-4 text-gray-300 text-center">{{ selectedExercise.originalExercise.comments }}</p>
          <p class="mb-4 text-gray-300 text-center">
            Protocol: {{ selectedExercise.originalExercise.sets }} sets of 
            {{ selectedExercise.originalExercise.reps }} reps at RPE 
            {{ selectedExercise.originalExercise.rpe }}
          </p>
          <form @submit.prevent="submitDialog">
            <table class="w-full border-collapse text-sm">
              <thead>
                <tr class="bg-gray-700 text-gray-300">
                  <th class="py-2 px-4 text-left">Set</th>
                  <th class="py-2 px-4 text-center">Reps</th>
                  <th class="py-2 px-4 text-center">RPE</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(result, index) in selectedExercise.results" 
                    :key="index" 
                    class="border-b border-gray-600">
                  <td class="py-2 px-4 text-left">Set {{ index + 1 }}</td>
                  <td class="py-2 px-4 text-center">
                    <input type="text" 
                           v-model="result.reps" 
                           class="w-full px-2 py-1 bg-gray-700 text-white rounded-md" />
                  </td>
                  <td class="py-2 px-4 text-center">
                    <input type="text" 
                           v-model="result.rpe" 
                           class="w-full px-2 py-1 bg-gray-700 text-white rounded-md" />
                  </td>
                </tr>
              </tbody>
            </table>
            <div class="mt-4">
              <textarea v-model="selectedExercise.userComments" 
                        placeholder="Comments on this exercise" 
                        class="w-full px-2 py-1 bg-gray-700 text-white rounded-md">
              </textarea>
            </div>
            <div class="mt-4 flex justify-end space-x-2">
              <button @click="closeDialog" type="button" class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition">
                Close
              </button>
              <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition">
                Submit
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useApi } from '~/composables/useApi';
import { useAthleteManagement } from '~/composables/manageAthletes';
import { useLabelsStore } from '~/stores/labels';
import { useBlockInformation } from '~/composables/getBlockInformation';
import { updateExercise } from '~/composables/updateProgram';

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

// Update onMounted to load both athlete and blocks
onMounted(async () => {
  try {
    // Load athlete data
    const athleteData = await fetchAthlete(userId);
    if (athleteData && athleteData.length > 0) {
      athlete.value = athleteData[0];
      username.value = athlete.value.username;
    }

    // Load blocks (keep existing blocks loading logic)
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

// Replace weeksStore with direct computation
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

const labelsStore = useLabelsStore();
const labels = computed(() => labelsStore.labels);

function getLabelColor(label) {
  return labelsStore.getColorByLabel(label);
}

// Update filteredOptions3 watch handler
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

// Add activeIndex ref with other refs
const activeIndex = ref(null);

// Add toggle function before dialog handling
const toggle = (index) => {
  activeIndex.value = activeIndex.value === index ? null : index;
};

// Keep existing dialog handling code
const dialogOpen = ref(false);
const selectedExercise = ref({
  originalExercise: {},
  results: [],
  userComments: ""
});


function openDialog(exercise) {
  const sets = parseInt(exercise.sets || 0);
  const existingResults = exercise.results?.sets || [];
  const existingComments = exercise.results?.comments || '';

  selectedExercise.value = {
    originalExercise: exercise,
    results: existingResults.length ? existingResults : Array.from({ length: sets }, () => ({
      reps: exercise.reps,
      rpe: exercise.rpe
    })),
    userComments: existingComments
  };
  dialogOpen.value = true;
}

function closeDialog() {
  dialogOpen.value = false;
}

async function submitDialog() {
  try {
    const currentDay = filteredOptions3.value[activeIndex.value];
    const mappedSets = selectedExercise.value.results.map((result, index) => ({
      setNumber: String(index + 1),
      reps: String(result.reps),
      rpe: String(result.rpe)
    }));

    console.log('Submitting exercise with parameters:', {
      userId,
      blockId: selectedOption1.value,
      weekId: selectedOption2.value,
      dayId: currentDay.title,
      exerciseName: selectedExercise.value.originalExercise.name,
      sets: mappedSets,
      comments: selectedExercise.value.userComments?.trim() || ''  // Ensure comments are trimmed and defaulted to empty string
    });

    const result = await updateExercise(
      userId,
      selectedOption1.value,
      selectedOption2.value,
      currentDay.title,
      selectedExercise.value.originalExercise.name,
      mappedSets,
      selectedExercise.value.userComments?.trim() || ''  // Ensure comments are trimmed and defaulted to empty string
    );

    if (result.error) {
      error.value = result.error;
      return;
    }

    closeDialog();
  } catch (e) {
    error.value = e.message || 'Failed to update exercise';
    console.error('Error submitting exercise:', e);
  }
}

// File handling methods
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
