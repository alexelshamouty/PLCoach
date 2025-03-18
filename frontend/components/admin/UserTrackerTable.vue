<template>
  <div class="p-4 bg-gray-800 rounded-lg shadow-md">
    <h3 class="font-semibold text-lg mb-4 text-white">User Trackers</h3>
    
    <!-- Empty state with better visual feedback -->
    <div v-if="trackers.length === 0" class="text-center py-8 bg-gray-700 rounded-md">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mx-auto text-gray-400 mb-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
      </svg>
      <p class="text-gray-400">No trackers assigned to user</p>
      <p class="text-gray-500 text-sm mt-1">Add a tracker template from the form above</p>
    </div>
    
    <!-- Improved table with better visual hierarchy -->
    <div v-else class="overflow-x-auto">
      <table class="min-w-full divide-y divide-gray-600 rounded-lg overflow-hidden">
        <thead class="bg-gray-700">
          <tr>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Tracker Name</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Metrics</th>
            <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider w-24">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-gray-750 divide-y divide-gray-600">
          <tr v-for="tracker in trackers" :key="tracker.TemplateName" class="hover:bg-gray-700 transition-colors">
            <td class="px-4 py-3 whitespace-nowrap font-medium">{{ tracker.TemplateName }}</td>
            <td class="px-4 py-3">
              <div class="flex flex-wrap gap-1">
                <span 
                  v-for="(metric, index) in tracker.metrics" 
                  :key="metric.metric" 
                  class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-blue-900 text-blue-200"
                >
                  {{ metric.metric }}
                  <span class="ml-1 text-blue-300 text-xs">({{ metric.unit || 'n/a' }})</span>
                </span>
              </div>
            </td>
            <td class="px-4 py-3 whitespace-nowrap">
              <button 
                @click="removeTracker(tracker)"
                class="flex items-center gap-1 text-red-400 hover:text-red-300 hover:bg-red-900 hover:bg-opacity-20 px-2 py-1 rounded transition-colors"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
                Remove
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  trackers: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['remove-tracker']);

// Remove tracker
function removeTracker(tracker) {
  emit('remove-tracker', tracker);
}
</script>
