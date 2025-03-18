<template>
  <div class="p-4 bg-gray-800 rounded-lg">
    <h3 class="font-semibold text-lg mb-4">Add Tracker</h3>
    <div class="flex flex-col md:flex-row gap-4 items-end">
      <div class="w-full md:w-2/3">
        <label class="block text-sm font-medium text-gray-300 mb-1">Select Tracker Template</label>
        <select 
          v-model="selectedTracker" 
          class="w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:ring-blue-500 focus:border-blue-500"
        >
          <option value="" disabled>Select a tracker template</option>
          <option v-for="tracker in trackerTemplates" :key="tracker.TemplateName" :value="tracker">
            {{ tracker.TemplateName }}
          </option>
        </select>
      </div>
      <button 
        @click="addTracker"
        :disabled="!selectedTracker"
        class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-500 disabled:cursor-not-allowed"
      >
        Add Tracker
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getTrackers } from '~/composables/trackerManagement';

const emit = defineEmits(['add-tracker']);

const trackerTemplates = ref([]);
const selectedTracker = ref('');

onMounted(async () => {
  await fetchTrackerTemplates();
});

// Fetch tracker templates
async function fetchTrackerTemplates() {
  try {
    const result = await getTrackers();
    if (result.error) {
      console.error('Failed to load tracker templates:', result.error);
    } else {
      trackerTemplates.value = result.data;
    }
  } catch (e) {
    console.error('Error loading tracker templates:', e);
  }
}

// Add tracker event
function addTracker() {
  if (!selectedTracker.value) return;
  
  emit('add-tracker', selectedTracker.value);
  
  // Reset selection
  selectedTracker.value = '';
}
</script>
