<template>
  <div class="container mx-auto p-4">
    <!-- Main trackers templates table -->
    <div class="mb-6">
      <h2 class="text-xl font-bold mb-4">Current Tracker Templates</h2>
      <div class="space-y-6">
        <div v-for="template in trackerTemplates" :key="template.name" class="bg-gray-800 rounded-lg p-4">
          <h3 
            @click="editTemplate(template)" 
            class="text-lg font-semibold mb-3 cursor-pointer hover:text-blue-400 transition-colors"
          >
            {{ template.name }}
          </h3>
          <table class="w-full bg-gray-700 rounded-lg overflow-hidden">
            <thead>
              <tr class="bg-gray-600">
                <th class="px-4 py-2 text-left">Metric</th>
                <th class="px-4 py-2 text-left">Unit</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="metric in template.metrics" 
                  :key="metric.metric" 
                  class="border-b border-gray-600">
                <td class="px-4 py-2">{{ metric.metric }}</td>
                <td class="px-4 py-2">{{ metric.unit }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Create new tracker button -->
    <button 
      @click="openNewDialog"
      class="bg-green-500 text-white px-6 py-2 rounded-lg hover:bg-green-600 transition"
    >
      Create new tracker template
    </button>

    <!-- Dialog -->
    <TrackerDialog
      v-model="showDialog"
      :is-editing="isEditing"
      :template="selectedTemplate"
      @save="handleSaveTemplate"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import TrackerDialog from '~/components/admin/TrackerDialog.vue';

const showDialog = ref(false);
const trackerTemplates = ref([]);
const isEditing = ref(false);
const selectedTemplate = ref({
  name: '',
  metrics: []
});

function openNewDialog() {
  isEditing.value = false;
  selectedTemplate.value = {
    name: '',
    metrics: []
  };
  showDialog.value = true;
}

function editTemplate(template) {
  isEditing.value = true;
  selectedTemplate.value = { ...template };
  showDialog.value = true;
}

function handleSaveTemplate(templateData) {
  if (isEditing.value) {
    const index = trackerTemplates.value.findIndex(t => t.name === selectedTemplate.value.name);
    if (index !== -1) {
      trackerTemplates.value[index] = templateData;
    }
  } else {
    trackerTemplates.value.push(templateData);
  }
  
  console.log('Template saved:', templateData);
  showDialog.value = false;
}
</script>