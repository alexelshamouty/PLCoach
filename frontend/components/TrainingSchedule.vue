<template>
  <div class="bg-gray-900 text-white p-6 rounded-lg shadow-md mt-4">
    <div v-for="(item, index) in days" :key="index" class="border-b border-gray-600">
      <div class="w-full flex justify-between items-center p-4">
        <button @click="toggle(index)" class="flex-1 flex justify-between items-center focus:outline-none">
          <span class="font-semibold">{{ item.title }}</span>
          <span :class="{'rotate-180': activeIndex === index}" class="transition-transform duration-300">
            ⬇️
          </span>
        </button>
        <button 
          @click="handleDayFinish(index, item.title)"
          class="ml-4 bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded-full transition-colors duration-200 text-xs font-medium">
          Finish Day
        </button>
      </div>
      <div v-if="activeIndex === index" class="p-4 text-gray-300">
        <div class="overflow-x-auto">
          <table class="hidden md:table w-full border-collapse text-sm">
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
                    @click="$emit('exercise-click', exercise, index)"
                    class="text-left hover:text-blue-400 transition-colors duration-200 cursor-pointer w-full flex items-center gap-2">
                    <span>{{ exercise.name }}</span>
                    <span class="text-blue-400 text-sm">📝</span>
                  </button>
                </td>
                <td class="py-2 px-4">
                  <button :style="{ backgroundColor: getLabelColor(exercise.label) }" 
                          class="text-black px-4 py-2 rounded-full hover:opacity-75 transition">
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

          <div class="md:hidden space-y-4">
            <div v-for="(exercise, i) in item.content" 
                 :key="i" 
                 class="bg-gray-800 p-4 rounded-lg space-y-2">
              <button 
                @click="$emit('exercise-click', exercise, index)"
                class="text-left hover:text-blue-400 transition-colors duration-200 cursor-pointer w-full text-lg font-semibold mb-2 flex items-center gap-2">
                <span>{{ exercise.name }}</span>
                <span class="text-blue-400 text-sm">📝</span>
              </button>
              <div class="flex justify-between items-center">
                <span class="text-gray-400">Label:</span>
                <button :style="{ backgroundColor: getLabelColor(exercise.label) }" 
                        class="text-black px-3 py-1 rounded-full hover:opacity-75 transition text-sm">
                  {{ exercise.label }}
                </button>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-400">Sets:</span>
                <span>{{ exercise.sets }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-400">Reps:</span>
                <span>{{ exercise.reps }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-400">RPE:</span>
                <span class="font-semibold text-yellow-400">{{ exercise.rpe }}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-400">Comments:</span>
                <span class="font-semibold text-yellow-400">{{ exercise.comments }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useLabelsStore } from '~/stores/labels';

const props = defineProps({
  days: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['exercise-click', 'day-finished']);

const activeIndex = ref(null);
const labelsStore = useLabelsStore();

function handleDayFinish(index, dayId) {
  emit('day-finished', { index, dayId });
}

function toggle(index) {
  activeIndex.value = activeIndex.value === index ? null : index;
}

function getLabelColor(label) {
  return labelsStore.getColorByLabel(label);
}
</script>
