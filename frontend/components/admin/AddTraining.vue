<template>
  <div class="mt-4 bg-gray-800 p-4 rounded-lg">
    <h3 class="text-lg font-semibold">Add Exercise</h3>
    <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4 mb-2">
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Exercise Name</label>
        <input v-model="exercise.name" 
               placeholder="e.g. Bench Press" 
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Movement Type</label>
        <select v-model="exercise.label" 
                class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none">
          <option value="" disabled>Select Label</option>
          <option v-for="(color, label) in labels" :key="label" :value="label">
            {{ label }}
          </option>
        </select>
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Sets</label>
        <input v-model.number="exercise.sets" 
               type="number" 
               placeholder="e.g. 3" 
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Reps</label>
        <input v-model.number="exercise.reps" 
               type="number" 
               placeholder="e.g. 8" 
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">RPE</label>
        <input v-model.number="exercise.rpe" 
               type="number" 
               min="6" 
               max="10" 
               placeholder="6-10" 
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
      </div>
      <div class="flex flex-col w-full md:w-1/6">
        <label class="text-sm text-gray-300 mb-1">Comments</label>
        <input v-model="exercise.comments" 
               placeholder="Additional notes" 
               class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none" />
      </div>
    </div>
    <button @click="handleSubmit" class="w-full mt-2 p-2 bg-green-600 rounded-lg hover:bg-green-700">
      Add Exercise
    </button>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useLabelsStore } from '~/stores/labels';

const props = defineProps({
  dayId: {
    type: String,
    required: true
  }
});

const emit = defineEmits(['exercise-added']);

const labelsStore = useLabelsStore();
const labels = labelsStore.labels;

const exercise = reactive({
  name: '',
  label: '',
  sets: 0,
  reps: 0,
  rpe: 0,
  comments: ''
});

function emitExercise(exerciseData) {
  emit('exercise-added', { ...exerciseData, dayId: props.dayId });
}

function resetForm() {
  Object.assign(exercise, {
    name: '',
    label: '',
    sets: 0,
    reps: 0,
    rpe: 0,
    comments: ''
  });
}

function handleSubmit() {
  emitExercise(exercise);
  resetForm();
}
</script>
