<template>
  <div class="bg-gray-900 text-white p-6 rounded-lg shadow-md mt-4">
    <div v-for="(item, index) in days" :key="index" class="border-b border-gray-600">
      <button @click="toggle(index)" class="w-full flex justify-between items-center p-4 focus:outline-none">
        <span class="font-semibold">{{ item.title }}</span>
        <span :class="{'rotate-180': activeIndex === index}" class="transition-transform duration-300">
          ⬇️
        </span>
      </button>
      <div v-if="activeIndex === index" class="p-4 text-gray-300">
        <div class="overflow-x-auto">
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
                    @click="$emit('exercise-click', exercise, index)"
                    class="text-left hover:text-blue-400 transition-colors duration-200 cursor-pointer w-full">
                    {{ exercise.name }}
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

defineEmits(['exercise-click']);

const activeIndex = ref(null);
const labelsStore = useLabelsStore();

function toggle(index) {
  activeIndex.value = activeIndex.value === index ? null : index;
}

function getLabelColor(label) {
  return labelsStore.getColorByLabel(label);
}
</script>
