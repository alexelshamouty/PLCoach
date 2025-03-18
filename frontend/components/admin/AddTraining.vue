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
        <select v-model="exercise.label" 
                :class="{'border-red-500 border': errors.label}"
                class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none">
          <option value="" disabled>Select Label</option>
          <option v-for="(color, label) in labels" :key="label" :value="label">
            {{ label }}
          </option>
        </select>
        <span v-if="errors.label" class="text-red-500 text-xs mt-1">{{ errors.label }}</span>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Sets</label>
        <input v-model.number="exercise.sets" 
               type="number" 
               placeholder="e.g. 3" 
               :class="{'border-red-500 border': errors.sets}"
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
        <span v-if="errors.sets" class="text-red-500 text-xs mt-1">{{ errors.sets }}</span>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Reps</label>
        <input v-model.number="exercise.reps" 
               type="number" 
               placeholder="e.g. 8" 
               :class="{'border-red-500 border': errors.reps}"
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
        <span v-if="errors.reps" class="text-red-500 text-xs mt-1">{{ errors.reps }}</span>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">RPE</label>
        <input v-model.number="exercise.rpe" 
               type="number" 
               min="6" 
               max="10" 
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
            :disabled="!isValid"
            :class="{'opacity-50 cursor-not-allowed': !isValid}"
            class="w-full mt-2 p-2 bg-green-600 rounded-lg hover:bg-green-700">
      Add Exercise
    </button>
  </div>
</template>

<script setup>
import { reactive, computed, ref } from 'vue';
import { useLabelsStore } from '~/stores/labels';
import LoadingOverlay from '~/components/shared/LoadingOverlay.vue';

const props = defineProps({
  dayId: {
    type: String,
    required: true
  }
});

const emit = defineEmits(['exercise-added']);

const labelsStore = useLabelsStore();
const labels = labelsStore.labels;

const errors = reactive({
  name: '',
  label: '',
  sets: '',
  reps: '',
  rpe: ''
});

// Initialize exercise with the correct structure matching what's shown in TrainingDisplay
const exercise = reactive({
  name: '',
  label: '',
  sets: null,
  reps: null,
  rpe: null,
  comments: ''
});

const isLoading = ref(false);

const isValid = computed(() => {
  return exercise.name && 
         exercise.label && 
         exercise.sets > 0 && 
         exercise.reps > 0 && 
         exercise.rpe >= 6 && 
         exercise.rpe <= 10;
});

function emitExercise(exerciseData) {
  emit('exercise-added', { ...exerciseData, dayId: props.dayId });
}

// Fix reset form to use proper initial values
function resetForm() {
  Object.assign(exercise, {
    name: '',
    label: '',
    sets: null,
    reps: null,
    rpe: null,
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
  errors.sets = !exercise.sets || exercise.sets <= 0 ? 'Sets must be greater than 0' : '';
  errors.reps = !exercise.reps || exercise.reps <= 0 ? 'Reps must be greater than 0' : '';
  errors.rpe = !exercise.rpe || exercise.rpe < 6 || exercise.rpe > 10 ? 'RPE must be between 6 and 10' : '';
  
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
</script>
