<template>
  <div class="space-y-4">
    <!-- Changed the outer div background to match parent -->
    <div class="bg-gray-700 p-4 rounded-lg">
      <div class="space-y-4">
        <!-- Changed block background styling -->
        <div v-for="block in blocks" :key="block.id" class="bg-gray-800 rounded-lg">
          <!-- Block Header with hover effect matching parent -->
          <button 
            @click="toggleBlock(block.id)"
            class="w-full px-4 py-3 flex justify-between items-center hover:bg-gray-600 rounded-t-lg"
          >
            <span class="font-semibold text-lg">{{ block.label }}</span>
            <svg 
              :class="['w-5 h-5 transition-transform', openBlocks.includes(block.id) ? 'transform rotate-180' : '']"
              fill="none" 
              stroke="currentColor" 
              viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          
          <!-- Week Content with consistent background -->
          <div v-show="openBlocks.includes(block.id)" class="border-t border-gray-600">
            <div v-for="week in block.weeks" :key="week" class="px-4 py-2">
              <!-- Week Header -->
              <button 
                @click="toggleWeek(`${block.id}-${week}`)"
                class="w-full flex justify-between items-center py-2 px-3 bg-gray-700 rounded-md hover:bg-gray-600 transition-colors duration-200"
              >
                <span class="text-md text-blue-300">Week {{ week }}</span>
                <svg 
                  :class="['w-4 h-4 transition-transform text-blue-300', openWeeks.includes(`${block.id}-${week}`) ? 'transform rotate-180' : '']"
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              
              <!-- Results Table with consistent background -->
              <div v-show="openWeeks.includes(`${block.id}-${week}`)" class="mt-2">
                <div class="overflow-x-auto">
                  <table class="min-w-full bg-gray-800 divide-y divide-gray-600">
                    <thead>
                      <tr>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">Day</th>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">Exercise</th>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">Sets</th>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">Reps</th>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">RPE</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-600">
                      <template v-if="isCurrentBlockAndWeek(block.id, week)">
                        <template v-for="day in exercises" :key="day.title">
                          <tr v-for="exercise in day.content" 
                              :key="`${day.title}-${exercise.name}`" 
                              class="hover:bg-gray-600">
                            <td class="px-4 py-2">{{ day.title }}</td>
                            <td class="px-4 py-2">{{ exercise.name }}</td>
                            <td class="px-4 py-2">{{ exercise.sets }}</td>
                            <td class="px-4 py-2">{{ exercise.reps }}</td>
                            <td class="px-4 py-2">{{ exercise.rpe }}</td>
                          </tr>
                        </template>
                      </template>
                    </tbody>
                  </table>
                </div>
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

const props = defineProps({
  blocks: {
    type: Array,
    required: true
  },
  selectedBlock: {
    type: String,
    required: true
  },
  selectedWeek: {
    type: String,
    required: true
  },
  exercises: {
    type: Array,
    required: true
  }
});

const openBlocks = ref([]);
const openWeeks = ref([]);

const toggleBlock = (blockId) => {
  const index = openBlocks.value.indexOf(blockId);
  if (index === -1) {
    openBlocks.value.push(blockId);
  } else {
    openBlocks.value.splice(index, 1);
  }
};

const toggleWeek = (weekKey) => {
  const index = openWeeks.value.indexOf(weekKey);
  if (index === -1) {
    openWeeks.value.push(weekKey);
  } else {
    openWeeks.value.splice(index, 1);
  }
};

const isCurrentBlockAndWeek = (blockId, week) => {
  return blockId === props.selectedBlock && week === props.selectedWeek;
};
</script>
