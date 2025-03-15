<template>
  <div class="bg-gray-900 text-white p-6 rounded-lg shadow-md mt-4">
    <div v-for="(item, index) in items" :key="index" class="border-b border-gray-600">
      <button @click="toggle(index)" class="w-full flex justify-between items-center p-4 focus:outline-none">
        <span class="font-semibold">{{ item.title }}</span>
        <span :class="{'rotate-180': activeIndex === index}" class="transition-transform duration-300">
          ⬇️
        </span>
      </button>
      <div v-if="activeIndex === index" class="p-4 text-gray-300">
        <div class="w-full max-w-full overflow-x-auto relative scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-gray-800">
          <div class="min-w-max md:min-w-full">
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
                    <button @click="handleLabelClick(exercise.label)" 
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
        </div>
        <AddTraining :day-id="item.title" @exercise-added="handleExerciseAdded" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useLabelsStore } from '~/stores/labels';
import AddTraining from './AddTraining.vue';

const props = defineProps({
  items: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['delete-exercise', 'exercise-added']);

const activeIndex = ref(null);
const labelsStore = useLabelsStore();

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
</script>
