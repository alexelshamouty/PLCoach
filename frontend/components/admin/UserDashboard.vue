<template>
  <div class="bg-gray-800 rounded-lg p-4 mb-6">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="bg-gray-700 p-4 rounded-lg">
        <h3 class="text-lg font-medium text-gray-300 mb-2">Total Blocks</h3>
        <p class="text-2xl font-bold text-blue-400">
          {{ completedWorkouts }}
        </p>
      </div>
      
      <div class="bg-gray-700 p-4 rounded-lg">
        <h3 class="text-lg font-medium text-gray-300 mb-2">Active Since</h3>
        <p class="text-2xl font-bold text-blue-400">
          {{ activeSince }} days
        </p>
      </div>
      
      <div class="bg-gray-700 p-4 rounded-lg">
        <h3 class="text-lg font-medium text-gray-300 mb-2">Current Weight</h3>
        <p class="text-2xl font-bold text-blue-400">
          {{ athleteWeight }} kg
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  completedWorkouts: {
    type: Number,
    default: 0
  },
  activeSince: {
    type: Number,
    default: 0
  },
  athleteWeight: {
    type: Number,
    default: 0
  }
});
</script>
