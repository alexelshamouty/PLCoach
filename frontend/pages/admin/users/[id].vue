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
      <!-- Management Section -->
      <div class="mt-4 bg-gray-800 p-4 rounded-lg">
        <button @click="toggleManage" class="w-full flex justify-between items-center p-4 focus:outline-none">
          <h3 class="text-lg font-semibold">Manage Athlete</h3>
          <span :class="{'rotate-180': manageOpen}" class="transition-transform duration-300">
            ⬇️
          </span>
        </button>
        <div v-if="manageOpen" class="p-4">
          <!-- Add block -->
          <div class="mt-4 bg-gray-800 p-4 rounded-lg">
            <h3 class="text-lg font-semibold">Add Block</h3>
            <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
              <input v-model="newBlockLabel" placeholder="Block Label" class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
              <button @click="handleAddBlock" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-purple-600 rounded-lg hover:bg-purple-700">
                Add Block
              </button>
            </div>
          </div>
          <!-- Add week -->
          <div class="mt-4 bg-gray-800 p-4 rounded-lg">
            <h3 class="text-lg font-semibold">Add a New Week</h3>
            <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
              <input v-model="newWeekTitle" placeholder="Enter week number (e.g., Week 4)" class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
              <button @click="handleAddWeek" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-purple-600 rounded-lg hover:bg-purple-700">
                Add Week
              </button>
            </div>
          </div>
          <!-- Add day -->
          <div class="mt-4 bg-gray-800 p-4 rounded-lg">
            <h3 class="text-lg font-semibold">Add a New Day</h3>
            <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
              <input v-model="newDayTitle" placeholder="Enter day (e.g., Wednesday)" class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
              <button @click="handleAddDay" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-blue-600 rounded-lg hover:bg-blue-700">
                Add Day
              </button>
            </div>
          </div>
        </div>
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
            <div class="overflow-x-auto relative">
              <table class="min-w-full border-collapse text-sm">
                <thead class="bg-gray-800 text-gray-300">
                  <tr>
                    <th class="py-2 px-2 md:px-4 text-left whitespace-nowrap">Exercise</th>
                    <th class="py-2 px-2 md:px-4 text-left whitespace-nowrap">Label</th>
                    <th class="py-2 px-2 md:px-4 text-center whitespace-nowrap">Sets</th>
                    <th class="py-2 px-2 md:px-4 text-center whitespace-nowrap">Reps</th>
                    <th class="py-2 px-2 md:px-4 text-center whitespace-nowrap">RPE</th>
                    <th class="py-2 px-2 md:px-4 text-center whitespace-nowrap">Comments</th>
                    <th class="py-2 px-2 md:px-4 text-center whitespace-nowrap">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(exercise, i) in item.content" :key="i" class="border-b border-gray-700 hover:bg-gray-800">
                    <td class="py-2 px-2 md:px-4 whitespace-nowrap">{{ exercise.name }}</td>
                    <td class="py-2 px-2 md:px-4">
                      <button @click="countSetsPerWeek(exercise.label)" 
                             :style="{ backgroundColor: getLabelColor(exercise.label) }" 
                             class="text-black px-2 md:px-4 py-1 md:py-2 rounded-full hover:opacity-75 transition text-xs md:text-sm">
                        {{ exercise.label }}
                      </button>
                    </td>
                    <td class="py-2 px-2 md:px-4 text-center">{{ exercise.sets }}</td>
                    <td class="py-2 px-2 md:px-4 text-center">{{ exercise.reps }}</td>
                    <td class="py-2 px-2 md:px-4 text-center font-semibold text-yellow-400">{{ exercise.rpe }}</td>
                    <td class="py-2 px-2 md:px-4 text-center font-semibold text-yellow-400 max-w-[100px] md:max-w-none truncate">{{ exercise.comments }}</td>
                    <td class="py-2 px-2 md:px-4 text-center">
                      <button @click="handleDeleteExercise(index, i)" class="text-red-600 hover:text-red-800 transition">
                        ✖️
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <!-- Add training -->
            <div class="mt-4 bg-gray-800 p-4 rounded-lg">
              <h3 class="text-lg font-semibold">Add Exercise</h3>
              <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4 mb-2">
                <div class="flex flex-col w-full md:w-1/6">
                  <label class="text-sm text-gray-300 mb-1">Exercise Name</label>
                  <input v-model="newExerciseName" 
                         placeholder="e.g. Bench Press" 
                         class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
                </div>
                <div class="flex flex-col w-full md:w-1/6">
                  <label class="text-sm text-gray-300 mb-1">Movement Type</label>
                  <select v-model="newExerciseLabel" 
                          class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none">
                    <option value="" disabled>Select Label</option>
                    <option v-for="(color, label) in labels" :key="label" :value="label">
                      {{ label }}
                    </option>
                  </select>
                </div>
                <div class="flex flex-col w-full md:w-1/6">
                  <label class="text-sm text-gray-300 mb-1">Sets</label>
                  <input v-model.number="newExerciseSets" 
                         type="number" 
                         placeholder="e.g. 3" 
                         class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
                </div>
                <div class="flex flex-col w-full md:w-1/6">
                  <label class="text-sm text-gray-300 mb-1">Reps</label>
                  <input v-model.number="newExerciseReps" 
                         type="number" 
                         placeholder="e.g. 8" 
                         class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
                </div>
                <div class="flex flex-col w-full md:w-1/6">
                  <label class="text-sm text-gray-300 mb-1">RPE</label>
                  <input v-model.number="newExerciseRpe" 
                         type="number" 
                         min="6" 
                         max="10" 
                         placeholder="6-10" 
                         class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
                </div>
                <div class="flex flex-col w-full md:w-1/6">
                  <label class="text-sm text-gray-300 mb-1">Comments</label>
                  <input v-model="newExerciseComments" 
                         placeholder="Additional notes" 
                         class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
                </div>
              </div>
              <button @click="handleAddExercise(item.title)" class="w-full mt-2 p-2 bg-green-600 rounded-lg hover:bg-green-700">
                Add Exercise
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

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

<script setup>
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

async function handleAddExercise(dayId) {
  // Convert all values to strings as required by backend
  const exercise = {
    name: String(newExerciseName.value),
    label: String(newExerciseLabel.value),
    sets: String(newExerciseSets.value),
    reps: String(newExerciseReps.value),
    rpe: String(newExerciseRpe.value),
    comments: String(newExerciseComments.value)
  };

  try {
    const result = await addExercise(
      userId,
      selectedOption1.value,
      selectedOption2.value,
      dayId,
      exercise
    );
    
    if (result.error) {
      errorMessage.value = result.error;
      showError.value = true;
      setTimeout(() => {
        showError.value = false;
      }, 3000);
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
    
    // Reset form
    newExerciseName.value = "";
    newExerciseLabel.value = "";
    newExerciseSets.value = 0;
    newExerciseReps.value = 0;
    newExerciseRpe.value = 0;
    newExerciseComments.value = "";
  } catch (error) {
    console.error('Error in handleAddExercise:', error);
    errorMessage.value = error.message || 'An error occurred while adding the exercise';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  }
}

async function handleDeleteExercise(dayId, exerciseIndex) {
  const day = filteredOptions3.value[dayId];
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

async function handleAddBlock() {
  if (!newBlockLabel.value) {
    errorMessage.value = "Block name is required";
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
    return;
  }

  try {
    const result = await addBlock(userId, newBlockLabel.value);
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
      selectedOption1.value = newBlockLabel.value;
      selectedOption2.value = ""; // Reset week selection
    }
    newBlockLabel.value = "";
  } catch (error) {
    console.error('Error in handleAddBlock:', error);
    errorMessage.value = error.message || 'An error occurred while adding the block';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  }
}

async function handleAddWeek() {
  try {
    const result = await addWeek(userId, selectedOption1.value, newWeekTitle.value);
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
      selectedOption2.value = newWeekTitle.value;
    }
    newWeekTitle.value = "";
  } catch (error) {
    console.error('Error in handleAddWeek:', error);
    errorMessage.value = error.message || 'An error occurred while adding the week';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  }
}

async function handleAddDay() {
  try {
    const result = await addDay(userId, selectedOption1.value, selectedOption2.value, newDayTitle.value);
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
    
    newDayTitle.value = "";
  } catch (error) {
    console.error('Error in handleAddDay:', error);
    errorMessage.value = error.message || 'An error occurred while adding the day';
    showError.value = true;
    setTimeout(() => {
      showError.value = false;
    }, 3000);
  }
}

const newWeekTitle = ref("");
const newDayTitle = ref("");

const manageOpen = ref(false);

function toggleManage() {
  manageOpen.value = !manageOpen.value;
}
</script>
