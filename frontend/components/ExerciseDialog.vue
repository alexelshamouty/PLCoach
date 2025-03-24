<template>
  <div v-if="modelValue" class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50 p-4">
    <div class="bg-gray-800 bg-opacity-90 p-4 sm:p-6 rounded-2xl shadow-lg w-full max-w-2xl mx-auto overflow-y-auto max-h-[90vh]">
      <p class="mb-4 text-gray-300 text-center text-sm sm:text-base">Comments from coach:</p>
      <p class="mb-4 text-gray-300 text-center text-sm sm:text-base">{{ exercise.comments }}</p>
      <p class="mb-4 text-gray-300 text-center text-sm sm:text-base">
        Protocol: {{ exercise.sets }} sets of {{ exercise.reps }} reps at RPE {{ exercise.rpe }}
      </p>
      
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <div class="overflow-x-auto">
          <table class="hidden md:table w-full border-collapse text-sm">
            <thead>
              <tr class="bg-gray-700 text-gray-300">
                <th class="py-2 px-2 sm:px-4 text-left whitespace-nowrap">Set</th>
                <th class="py-2 px-2 sm:px-4 text-center whitespace-nowrap">Reps</th>
                <th class="py-2 px-2 sm:px-4 text-center whitespace-nowrap">Weight (kg)</th>
                <th class="py-2 px-2 sm:px-4 text-center whitespace-nowrap">RPE</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(result, index) in localResults" 
                  :key="index" 
                  class="border-b border-gray-600">
                <td class="py-2 px-2 sm:px-4 text-left whitespace-nowrap">Set {{ index + 1 }}</td>
                <td class="py-2 px-2 sm:px-4 text-center">
                  <input type="text" 
                         v-model="result.reps" 
                         class="w-16 sm:w-20 px-2 py-1 bg-gray-700 text-white rounded-md text-center" />
                </td>
                <td class="py-2 px-2 sm:px-4 text-center">
                  <input type="text" 
                         v-model="result.weight" 
                         class="w-16 sm:w-20 px-2 py-1 bg-gray-700 text-white rounded-md text-center" />
                </td>
                <td class="py-2 px-2 sm:px-4 text-center">
                  <input type="text" 
                         v-model="result.rpe" 
                         class="w-16 sm:w-20 px-2 py-1 bg-gray-700 text-white rounded-md text-center" />
                </td>
              </tr>
            </tbody>
          </table>

          <!-- Mobile view -->
          <div class="md:hidden space-y-4">
            <div v-for="(result, index) in localResults" 
                 :key="index" 
                 class="bg-gray-700 p-4 rounded-lg space-y-3">
              <div class="font-semibold text-center mb-2">Set {{ index + 1 }}</div>
              <div class="space-y-3">
                <div class="flex flex-col">
                  <label class="text-gray-400 mb-1">Reps:</label>
                  <input type="text" 
                         v-model="result.reps" 
                         class="w-full px-2 py-1 bg-gray-600 text-white rounded-md" />
                </div>
                <div class="flex flex-col">
                  <label class="text-gray-400 mb-1">Weight (kg):</label>
                  <input type="text" 
                         v-model="result.weight" 
                         class="w-full px-2 py-1 bg-gray-600 text-white rounded-md" />
                </div>
                <div class="flex flex-col">
                  <label class="text-gray-400 mb-1">RPE:</label>
                  <input type="text" 
                         v-model="result.rpe" 
                         class="w-full px-2 py-1 bg-gray-600 text-white rounded-md" />
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="mt-4">
          <textarea 
            v-model="localComments" 
            placeholder="Comments on this exercise" 
            class="w-full px-3 py-2 bg-gray-700 text-white rounded-md min-h-[80px] resize-y"
          ></textarea>
        </div>

        <div class="mt-4 flex flex-col sm:flex-row justify-end gap-2 sm:gap-4">
          <button @click="handleClose" 
                  type="button" 
                  class="w-full sm:w-auto bg-red-500 text-white px-6 py-2 rounded-lg hover:bg-red-600 transition">
            Close
          </button>
          <button type="submit" 
                  :disabled="isSubmitting"
                  class="w-full sm:w-auto bg-green-500 text-white px-6 py-2 rounded-lg hover:bg-green-600 transition disabled:opacity-50">
            {{ isSubmitting ? 'Submitting...' : 'Submit' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  modelValue: Boolean,
  exercise: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['update:modelValue', 'submit']);

const isSubmitting = ref(false);
const localResults = ref([]);
const localComments = ref('');

// Initialize local state when exercise changes
watch(() => props.exercise, (newExercise) => {
  const sets = parseInt(newExercise.sets || 0);
  const existingResults = newExercise.results?.sets || [];
  
  localResults.value = existingResults.length ? 
    [...existingResults] : 
    Array.from({ length: sets }, () => ({
      reps: newExercise.reps,
      rpe: newExercise.rpe,
      weight: ''
    }));
    
  localComments.value = newExercise.results?.comments || '';
}, { immediate: true });

function handleClose() {
  emit('update:modelValue', false);
}

async function handleSubmit() {
  isSubmitting.value = true;
  
  try {
    const mappedSets = localResults.value.map((result, index) => ({
      setNumber: String(index + 1),
      reps: String(result.reps),
      weight: String(result.weight),
      rpe: String(result.rpe)
    }));

    await emit('submit', {
      sets: mappedSets,
      comments: localComments.value
    });
    
    handleClose();
  } finally {
    isSubmitting.value = false;
  }
}
</script>
