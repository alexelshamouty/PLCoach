<template>
  <div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <LoadingOverlay :show="isLoading" />
    <ErrorAlert :message="errorMessage" @clear="errorMessage = null" />

    <div v-if="!isLoading" class="w-full max-w-4xl p-6 rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold text-center mb-4">{{ username }} aka {{ name }} Program Management</h2>
      
      <!-- Tabs Navigation -->
      <div class="flex border-b-2 border-gray-700 mb-6 overflow-hidden">
        <div class="flex overflow-x-auto no-scrollbar">
          <button 
            v-for="tab in tabs" 
            :key="tab.id"
            @click="setActiveTab(tab.id)"
            :class="[
              'px-4 py-2 font-medium text-base sm:text-lg flex-shrink-0 transition-all duration-200 relative',
              activeTab === tab.id 
                ? 'text-blue-400 border-b-2 border-blue-400 -mb-0.5' 
                : 'text-gray-300 hover:text-blue-300 hover:bg-gray-800'
            ]"
          >
            <span class="relative z-10">{{ tab.name }}</span>
            <div 
              v-if="activeTab === tab.id" 
              class="absolute bottom-0 left-0 w-full h-1 bg-blue-400 transform"
            ></div>
          </button>
        </div>
      </div>

      <!-- Programs Tab -->
      <div v-if="activeTab === 'programs'" class="space-y-4">
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
          :block="selectedOption1"
          :week="selectedOption2"
          @delete-exercise="handleDeleteExercise"
          @exercise-added="handleAddExercise"
          @delete-day="handleDeleteDay"
          @exercise-updated="handleExerciseUpdated"
        />
      </div>

      <!-- Activity Tab -->
      <div v-if="activeTab === 'activity'" class="space-y-4">
        <ActivityDisplay 
          :blocks="options1"
          :selectedBlock="selectedOption1"
          :selectedWeek="selectedOption2"
          :exercises="filteredOptions3"
          :getDaysByWeek="getDaysByWeek"
          :userId="userId"
          :weight="Number(weight)"
          :time-stamp="timeStamp"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import UserManagement from '~/components/admin/UserManagement.vue';
import TrainingDisplay from '~/components/admin/TrainingDisplay.vue';
import ActivityDisplay from '~/components/admin/ActivityDisplay.vue';
import { ref, computed, watch, onMounted } from "vue";
import LoadingOverlay from '~/components/shared/LoadingOverlay.vue';
import ErrorAlert from '~/components/shared/ErrorAlert.vue';
import { useRoute } from "vue-router";
import { useApi } from '~/composables/useApi';
import { addBlock, addWeek, addDay, addExercise, deleteExercise, deleteDay } from '~/composables/updateProgram';
import { useBlockInformation } from '~/composables/getBlockInformation';
import { useAthleteManagement } from '~/composables/manageAthletes';
import { useTabs } from '~/composables/useTabs';

const username = ref("");
const name = ref("");
const weight = ref(0);
const timeStamp = ref("");
const route = useRoute();
const userId = route.params.id;
const { getAllBlocks, getDaysByWeek } = useBlockInformation();
const { fetchAthlete } = useAthleteManagement();

definePageMeta({ middleware: ['auth-admin'] });

// Add these for blocks management
const options1 = ref([]);
const selectedOption1 = ref("");
const isLoading = ref(false);

const filteredOptions3 = ref([]);

const errorMessage = ref(null);

// Load blocks when page loads
onMounted(async () => {
  isLoading.value = true;
  try {
    console.log("Fetching athlete and blocks... " + userId);
    const athlete = await fetchAthlete(userId);
    if (athlete) {
      username.value = athlete[0].username;
      name.value = athlete[0].name;
      weight.value = athlete[0].weight;
      timeStamp.value = athlete[0].timeStamp;
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

const filteredOptions2 = computed(() => options2.value);

// Change selectedOption2 from computed to ref
const selectedOption2 = ref("");

// Update the watcher for `selectedOption1` to reset `selectedOption2` when the block changes
watch(selectedOption1, (newBlock) => {
  const options = options2.value;
  selectedOption2.value = options.length ? options[0].id : ""; // Set the first week as default
});

// Update the watcher for `selectedOption2` to fetch data when it changes
watch([selectedOption1, selectedOption2], async ([newBlock, newWeek]) => {
  if (newBlock && newWeek) {
    const response = await getDaysByWeek(userId, newBlock, newWeek);
    if (!response.error) {
      filteredOptions3.value = Object.entries(response || {}).map(([dayId, dayData]) => ({
        title: dayId,
        content: dayData.Exercises || [],
        index: dayData.dayIndex ? parseInt(dayData.dayIndex, 10) : 999
      }));
      filteredOptions3.value.sort((a, b) => a.index - b.index);
    } else {
      filteredOptions3.value = [];
    }
  } else {
    filteredOptions3.value = [];
  }
}, { immediate: true });



// Replace error handling refs
// Remove showError ref since ErrorAlert handles visibility
async function handleAddExercise(exerciseData) {
  const { dayId, ...exercise } = exerciseData;
  
  try {
    const day = filteredOptions3.value.find(day => day.title === dayId);
    const dayIndex = day ? String(day.content.length) : "0"; // Calculate dayIndex as a string

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
        comments: String(exercise.comments),
        dayIndex // Include dayIndex
      }
    );
    
    if (result.error) {
      errorMessage.value = result.error;
      return;
    }

    // Find the day in filteredOptions3 and update it directly
    const dayIndexInArray = filteredOptions3.value.findIndex(day => day.title === dayId);
    if (dayIndexInArray !== -1) {
      // Create a deep copy of the current state to maintain reactivity
      const updatedOptions = JSON.parse(JSON.stringify(filteredOptions3.value));
      
      // Add the new exercise to the appropriate day's content array
      updatedOptions[dayIndexInArray].content.push({
        name: exercise.name,
        label: exercise.label,
        sets: exercise.sets,
        reps: exercise.reps,
        rpe: exercise.rpe,
        comments: exercise.comments,
        dayIndex // Add dayIndex to the exercise
      });
      
      // Update the state with the new array
      filteredOptions3.value = updatedOptions;
    } else {
      console.error('Day not found in current view:', dayId);
      errorMessage.value = 'Day not found in current view';
    }
  } catch (error) {
    console.error('Error in handleAddExercise:', error);
    errorMessage.value = error.message || 'An error occurred while adding the exercise';
  }
}

async function handleDeleteExercise(dayIndex, exerciseIndex) {
  const day = filteredOptions3.value[dayIndex];
  if (!day || !day.content[exerciseIndex]) {
    errorMessage.value = "Exercise not found";
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
      exercise.label,
      exercise.dayIndex,
    );

    if (result.error) {
      errorMessage.value = result.error;
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
  }
}

const newBlockLabel = ref("");
const { authenticatedFetch } = useApi();

async function handleAddBlock(blockLabel) {
  if (!blockLabel) {
    errorMessage.value = "Block name is required";
    return;
  }

  try {
    const result = await addBlock(userId, blockLabel);
    if (result.error) {
      errorMessage.value = result.error;
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
  }
}

async function handleAddWeek(weekTitle) {
  try {
    const result = await addWeek(userId, selectedOption1.value, weekTitle);
    if (result.error) {
      errorMessage.value = result.error;
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
  }
}

async function handleAddDay(title) {
  try {
    // Simply pass the title to the addDay function without index
    const result = await addDay(userId, selectedOption1.value, selectedOption2.value, title);
    if (result.error) {
      errorMessage.value = result.error;
      return;
    }

    // Fetch updated days after adding new day
    const days = await getDaysByWeek(userId, selectedOption1.value, selectedOption2.value);
    if (!days.error) {
      // Map days without adding index calculation for the new day
      filteredOptions3.value = Object.entries(days).map(([dayId, dayData]) => ({
        title: dayId,
        content: dayData.Exercises || [],
        // Use dayIndex from data if available, otherwise default
        index: dayData.dayIndex ? parseInt(dayData.dayIndex, 10) : 999
      }));
      
      // Sort based on index
      filteredOptions3.value.sort((a, b) => a.index - b.index);
    }
  } catch (error) {
    console.error('Error in handleAddDay:', error);
    errorMessage.value = error.message || 'An error occurred while adding the day';
  }
}

function handleDeleteDay(blockId, weekId, dayId) {
  if (!confirm(`Are you sure you want to delete the day "${dayId}"?`)) {
    return;
  }

  deleteDay(userId, blockId, weekId, dayId)
    .then((result) => {
      if (result.error) {
        errorMessage.value = result.error;
        console.error('Error deleting day:', result.error);
      } else {
        console.log('Day deleted successfully');
        // Update the UI locally
        filteredOptions3.value = filteredOptions3.value.filter(day => day.title !== dayId);
      }
    })
    .catch((error) => {
      console.error('Error in handleDeleteDay:', error);
      errorMessage.value = error.message || 'An error occurred while deleting the day';
    });
}

function handleExerciseUpdated({ dayId, exercise }) {
  console.log('Block ID:', selectedOption1.value);
  console.log('Week ID:', selectedOption2.value);
  console.log('Day ID:', dayId);
  console.log('Exercise Data:', exercise);
}

const { tabs, activeTab, setActiveTab } = useTabs();
</script>

<style scoped>
.no-scrollbar {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
.no-scrollbar::-webkit-scrollbar {
  display: none;  /* Chrome, Safari and Opera */
}
</style>
