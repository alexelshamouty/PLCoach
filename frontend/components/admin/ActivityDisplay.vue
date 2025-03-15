<template>
  <div class="space-y-4">
    <div class="bg-gray-700 p-4 rounded-lg">
      <UserDashboard
        :completed-workouts="totalBlocks"
        :active-since="activeSinceDays"
        :athlete-weight="props.weight"
      />
      
      <div class="space-y-4">
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
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">Set</th>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">Reps</th>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">Weight</th>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">RPE</th>
                        <th class="px-4 py-2 text-left text-sm font-medium text-gray-300">Comments</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-600">
                      <template v-for="day in getWeekExercises(block.id, week)" :key="day.title">
                        <template v-for="exercise in day.content" :key="`${day.title}-${exercise.name}`">
                          <!-- Show a row for each set in results if they exist -->
                          <template v-if="exercise.results?.sets?.length">
                            <tr v-for="(set, setIndex) in exercise.results.sets" 
                                :key="`${day.title}-${exercise.name}-${setIndex}`"
                                class="hover:bg-gray-600">
                              <td class="px-4 py-2">{{ setIndex === 0 ? day.title : '' }}</td>
                              <td class="px-4 py-2">{{ setIndex === 0 ? exercise.name : '' }}</td>
                              <td class="px-4 py-2">{{ set.setNumber }}</td>
                              <td class="px-4 py-2">{{ set.reps }}</td>
                              <td class="px-4 py-2">{{ set.weight || '-' }}</td>
                              <td class="px-4 py-2">{{ set.rpe }}</td>
                              <td class="px-4 py-2">
                                {{ setIndex === 0 ? (exercise.results?.comments || '-') : '' }}
                              </td>
                            </tr>
                          </template>
                          <!-- Show single row for exercises without results -->
                          <tr v-else class="hover:bg-gray-600">
                            <td class="px-4 py-2">{{ day.title }}</td>
                            <td class="px-4 py-2">{{ exercise.name }}</td>
                            <td class="px-4 py-2">-</td>
                            <td class="px-4 py-2">{{ exercise.reps }}</td>
                            <td class="px-4 py-2">-</td>
                            <td class="px-4 py-2">{{ exercise.rpe }}</td>
                            <td class="px-4 py-2">{{ exercise.comments || '-' }}</td>
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
import { ref, computed } from 'vue';
import UserDashboard from './UserDashboard.vue';  // Add this import at the top

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
  },
  getDaysByWeek: {
    type: Function,
    required: true
  },
  userId: {
    type: String,
    required: true
  },
  weight: {
    type: Number,
    required: true
  },
  timeStamp: {
    type: String,
    required: true
  }
});

// Update to use timeStamp prop directly
const activeSinceDays = computed(() => {
  const now = new Date();
  const created = new Date(props.timeStamp);
  const diffTime = Math.abs(now - created);
  return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
});

const openBlocks = ref([]);
const openWeeks = ref([]);
const weekData = ref({});

const totalBlocks = computed(() => {
  return props.blocks?.length || 0;
});

const toggleBlock = (blockId) => {
  const index = openBlocks.value.indexOf(blockId);
  if (index === -1) {
    openBlocks.value.push(blockId);
  } else {
    openBlocks.value.splice(index, 1);
  }
};

const toggleWeek = async (weekKey) => {
  const [blockId, week] = weekKey.split('-');
  const index = openWeeks.value.indexOf(weekKey);
  if (index === -1) {
    openWeeks.value.push(weekKey);
    // Fetch days data when week is opened
    const response = await props.getDaysByWeek(props.userId, blockId, week);
    if (!response.error) {
      weekData.value[weekKey] = Object.entries(response).map(
        ([dayId, dayData]) => ({
          title: dayId,
          content: dayData.Exercises || []
        })
      );
    }
  } else {
    openWeeks.value.splice(index, 1);
    // Clear data when week is closed
    delete weekData.value[weekKey];
  }
};

const getWeekExercises = (blockId, week) => {
  const weekKey = `${blockId}-${week}`;
  return weekData.value[weekKey] || [];
};

const isCurrentBlockAndWeek = (blockId, week) => {
  return blockId === props.selectedBlock && week === props.selectedWeek;
};
</script>
