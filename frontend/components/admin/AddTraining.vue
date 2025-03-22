<template>
  <div class="mt-4 bg-gray-800 p-4 rounded-lg relative">
    <!-- Loading Overlay -->
    <LoadingOverlay :show="isLoading" />
    <h3 class="text-lg font-semibold">Add Exercise</h3>
    <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4 mb-2">
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Exercise Name</label>
        <input v-model="exercise.name" 
               placeholder="e.g. Bench Press" 
               :class="{'border-red-500 border': errors.name}"
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
        <span v-if="errors.name" class="text-red-500 text-xs mt-1">{{ errors.name }}</span>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Movement Type</label>
        <div class="flex items-center">
          <select v-model="exercise.label" 
                 :class="{'border-red-500 border': errors.label}"
                 class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none">
            <option value="" disabled>Select Label</option>
            <option v-for="(color, label) in labels" :key="label" :value="label">
              {{ label }}
            </option>
          </select>
          <VideoUploadButton @click="openVideoManager" />
        </div>
        <span v-if="errors.label" class="text-red-500 text-xs mt-1">{{ errors.label }}</span>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Sets</label>
        <input v-model="exercise.sets" 
               type="text" 
               placeholder="e.g. 3" 
               :class="{'border-red-500 border': errors.sets}"
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
        <span v-if="errors.sets" class="text-red-500 text-xs mt-1">{{ errors.sets }}</span>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Reps</label>
        <input v-model="exercise.reps" 
               type="text" 
               placeholder="e.g. 8" 
               :class="{'border-red-500 border': errors.reps}"
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
        <span v-if="errors.reps" class="text-red-500 text-xs mt-1">{{ errors.reps }}</span>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">RPE</label>
        <input v-model="exercise.rpe" 
               type="text" 
               placeholder="6-10" 
               :class="{'border-red-500 border': errors.rpe}"
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
        <span v-if="errors.rpe" class="text-red-500 text-xs mt-1">{{ errors.rpe }}</span>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Comments</label>
        <input v-model="exercise.comments" 
               placeholder="Additional notes" 
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
      </div>
    </div>
    <button @click="handleSubmit" 
            class="w-full mt-2 p-2 bg-green-600 rounded-lg hover:bg-green-700">
      Add Exercise
    </button>
    
    <!-- Video Manager Dialog -->
    <VideoManager 
      v-if="showVideoManager"
      :show="showVideoManager"
      :block="currentBlock"
      :week="currentWeek"
      :day-id="dayId"
      :exercise-name="exercise.name"
      :exercise-label="exercise.label"
      @close="showVideoManager = false"
    />
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import { useLabelsStore } from '~/stores/labels';
import LoadingOverlay from '~/components/shared/LoadingOverlay.vue';
import VideoManager from '~/components/shared/VideoManager.vue';
import VideoUploadButton from '~/components/shared/VideoUploadButton.vue';

const props = defineProps({
  dayId: {
    type: String,
    required: true
  },
  currentBlock: {
    type: String,
    default: 'selectionOption1'
  },
  currentWeek: {
    type: String,
    default: 'SelectionOption3'
  }
});

const emit = defineEmits(['exercise-added']);

const labelsStore = useLabelsStore();
const labels = labelsStore.labels;

const showVideoManager = ref(false);

const errors = reactive({
  name: '',
  label: '',
  sets: '',
  reps: '',
  rpe: ''
});

// Initialize exercise with the correct structure matching what's shown in TrainingDisplay
// Changed to use string values for sets, reps, rpe
const exercise = reactive({
  name: '',
  label: '',
  sets: '',
  reps: '',
  rpe: '',
  comments: ''
});

const isLoading = ref(false);

function emitExercise(exerciseData) {
  emit('exercise-added', { ...exerciseData, dayId: props.dayId });
}

// Fix reset form to use proper initial values
function resetForm() {
  Object.assign(exercise, {
    name: '',
    label: '',
    sets: '',
    reps: '',
    rpe: '',
    comments: ''
  });
  
  // Clear any validation errors
  Object.keys(errors).forEach(key => {
    errors[key] = '';
  });
}

function validateForm() {
  let isValid = true;
  errors.name = !exercise.name ? 'Exercise name is required' : '';
  errors.label = !exercise.label ? 'Movement type is required' : '';
  errors.sets = !exercise.sets ? 'Sets is required' : '';
  errors.reps = !exercise.reps ? 'Reps is required' : '';
  errors.rpe = !exercise.rpe ? 'RPE is required' : '';
  
  return !Object.values(errors).some(error => error !== '');
}

async function handleSubmit() {
  if (validateForm()) {
    try {
      isLoading.value = true;
      await emitExercise(exercise);
      resetForm();
    } finally {
      isLoading.value = false;
    }
  }
}

function openVideoManager() {
  if (!exercise.name || !exercise.label) {
    // Require at least exercise name and label to be set before opening video manager
    if (!exercise.name) errors.name = 'Exercise name is required for video management';
    if (!exercise.label) errors.label = 'Movement type is required for video management';
    return;
  }
  
  showVideoManager.value = true;
}
</script>
