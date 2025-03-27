<template>
  <div class="bg-gray-900 text-white p-6 rounded-lg shadow-md mt-4">
    <div v-for="(item, index) in sortedItems" :key="index" class="border-b border-gray-600">
      <div class="flex justify-between items-center">
        <button @click="toggle(index)" class="w-full flex justify-between items-center p-4 focus:outline-none">
          <span class="font-semibold">{{ item.title }}</span>
          <span :class="{'rotate-180': activeIndex === index}" class="transition-transform duration-300">
            ⬇️
          </span>
        </button>
        <button 
          @click="emitDeleteDay(item.title)" 
          class="bg-red-500 text-white text-xs px-3 py-1 rounded hover:bg-red-600 transition-all duration-200"
          title="Delete Day"
        >
          Delete
        </button>
      </div>
      <div v-if="activeIndex === index" class="p-4 text-gray-300">
        <div class="w-full max-w-full overflow-x-auto relative scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-gray-800">
          <div class="min-w-max md:min-w-full">
            <table class="min-w-full border-collapse text-sm block md:table">
              <thead class="bg-gray-800 text-gray-300 hidden md:table-header-group">
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
              <tbody class="block md:table-row-group">
                <tr v-for="(exercise, i) in item.content" 
                    :key="i" 
                    class="border-b border-gray-700 hover:bg-gray-800 block md:table-row mb-6 md:mb-0">
                  <td class="py-2 px-2 md:px-4 block md:table-cell md:whitespace-nowrap">
                    <span class="inline-block w-1/3 md:hidden font-bold">Exercise:</span>
                    <button 
                      class="text-blue-400 hover:underline focus:outline-none"
                      @click="emitExerciseUpdated(item.title, exercise)"
                    >
                      {{ exercise.name }}
                    </button>
                  </td>
                  <td class="py-2 px-2 md:px-4 block md:table-cell">
                    <span class="inline-block w-1/3 md:hidden font-bold">Label:</span>
                    <div class="flex items-center">
                      <button @click="handleLabelClick(exercise.label)" 
                             :style="{ backgroundColor: getLabelColor(exercise.label) }" 
                             class="text-black px-2 md:px-4 py-1 md:py-2 rounded-full hover:opacity-75 transition text-xs md:text-sm">
                        {{ exercise.label }}
                      </button>
                      <VideoUploadButton @click="openVideoManager(item.title, exercise.name, exercise.label)" />
                    </div>
                  </td>
                  <td class="py-2 px-2 md:px-4 block md:table-cell">
                    <span class="inline-block w-1/3 md:hidden font-bold">Sets:</span>
                    <span class="md:text-center inline-block md:w-full">{{ exercise.sets }}</span>
                  </td>
                  <td class="py-2 px-2 md:px-4 block md:table-cell">
                    <span class="inline-block w-1/3 md:hidden font-bold">Reps:</span>
                    <span class="md:text-center inline-block md:w-full">{{ exercise.reps }}</span>
                  </td>
                  <td class="py-2 px-2 md:px-4 block md:table-cell">
                    <span class="inline-block w-1/3 md:hidden font-bold">RPE:</span>
                    <span class="md:text-center inline-block md:w-full font-semibold text-yellow-400">{{ exercise.rpe }}</span>
                  </td>
                  <td class="py-2 px-2 md:px-4 block md:table-cell">
                    <span class="inline-block w-1/3 md:hidden font-bold">Comments:</span>
                    <span class="md:text-center inline-block md:w-full font-semibold text-yellow-400 max-w-[100px] md:max-w-none truncate">
                      {{ exercise.comments }}
                    </span>
                  </td>
                  <td class="py-2 px-2 md:px-4 block md:table-cell">
                    <span class="inline-block w-1/3 md:hidden font-bold">Actions:</span>
                    <span class="md:text-center inline-block md:w-full">
                      <button @click="handleDeleteExercise(index, i)" 
                              class="text-red-400 hover:text-red-600 p-2 rounded-full hover:bg-red-500/10 transition-all duration-200">
                        ✖️
                      </button>
                    </span>
                  </td>
                  <!-- Hidden dayIndex -->
                  <input type="hidden" :value="exercise.dayIndex" />
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <AddTraining :day-id="item.title" @exercise-added="handleExerciseAdded" />
      </div>
    </div>
    
    <!-- Video Manager Dialog -->
    <VideoManager 
      v-if="showVideoManager"
      :show="showVideoManager"
      :block="currentBlock"
      :week="currentWeek"
      :day-id="selectedDayId"
      :exercise-name="selectedExerciseName"
      :exercise-label="selectedExerciseLabel"
      :is-admin="true"
      @close="showVideoManager = false"
      @video-uploaded="handleVideoUploaded"
      @video-deleted="handleVideoDeleted"
    />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useLabelsStore } from '~/stores/labels';
import AddTraining from './AddTraining.vue';
import VideoManager from '~/components/shared/VideoManager.vue';
import VideoUploadButton from '~/components/shared/VideoUploadButton.vue';

const props = defineProps({
  items: {
    type: Array,
    required: true
  },
  block: {
    type: String,
    default: ''
  },
  week: {
    type: String,
    default: ''
  }
});

const emit = defineEmits(['delete-exercise', 'exercise-added', 'delete-day', 'exercise-updated']);

const activeIndex = ref(null);
const labelsStore = useLabelsStore();

// Create a local reactive copy of items that we can sort
const localItems = ref([]);
// Track the current block and week
const currentBlock = ref('');
const currentWeek = ref('');

// Variables for VideoManager
const showVideoManager = ref(false);
const selectedDayId = ref('');
const selectedExerciseName = ref('');
const selectedExerciseLabel = ref('');

// Update local items whenever props.items changes
watch(() => props.items, (newItems) => {
  if (newItems && newItems.length) {
    localItems.value = [...newItems];
  } else {
    localItems.value = [];
  }
}, { immediate: true, deep: true });

// Watch for block and week changes
watch(() => props.block, (newBlock) => {
  if (newBlock) {
    currentBlock.value = newBlock;
  }
}, { immediate: true });

watch(() => props.week, (newWeek) => {
  if (newWeek) {
    currentWeek.value = newWeek;
  }
}, { immediate: true });

// Sort items based on index
const sortedItems = computed(() => {
  // Create a copy of the items and ensure each has an index
  const itemsWithIndices = localItems.value.map(item => ({
    ...item,
    index: item.index !== undefined ? parseInt(item.index, 10) : 999
  }));
  
  // Sort by index
  return itemsWithIndices.sort((a, b) => a.index - b.index);
});

function toggle(index) {
  activeIndex.value = activeIndex.value === index ? null : index;
}

function getLabelColor(label) {
  return labelsStore.getColorByLabel(label);
}

function handleLabelClick(label) {
  // Implement any label click functionality here
}

function handleDeleteExercise(dayIndex, exerciseIndex) {
  emit('delete-exercise', dayIndex, exerciseIndex);
}

function handleExerciseAdded(exercise) {
  emit('exercise-added', exercise);
}

function openVideoManager(dayId, exerciseName, exerciseLabel) {
  selectedDayId.value = dayId;
  selectedExerciseName.value = exerciseName;
  selectedExerciseLabel.value = exerciseLabel;
  showVideoManager.value = true;
}

// Real implementation for handling video events
function handleVideoUploaded(data) {
  console.log('Video uploaded successfully:', data);
  // You can add UI notifications or other logic here
}

function handleVideoDeleted(data) {
  console.log('Video deleted successfully:', data);
  // You can add UI notifications or other logic here
}

function emitDeleteDay(dayId) {
  emit('delete-day', currentBlock.value, currentWeek.value, dayId);
}

function emitExerciseUpdated(dayId, exercise) {
  emit('exercise-updated', { dayId, exercise });
}
</script>
