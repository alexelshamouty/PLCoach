<template>
  <div class="container mx-auto p-4">
    <ErrorAlert :message="error" @clear="error = ''" />
    
    <!-- Loading state -->
    <div v-if="loading" class="text-center py-8">
      <p>Loading templates...</p>
    </div>

    <!-- Error state -->
    <div v-else-if="error" class="bg-red-500 bg-opacity-20 p-4 rounded-lg mb-6">
      <p class="text-red-400">{{ error }}</p>
    </div>

    <!-- Main trackers templates table -->
    <div v-else class="mb-6">
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
import { ref, onMounted } from 'vue';
import TrackerDialog from '~/components/admin/TrackerDialog.vue';
import ErrorAlert from '~/components/shared/ErrorAlert.vue';
import { createTemplate, updateTemplate, getTrackers } from '~/composables/trackerManagement';

const showDialog = ref(false);
const trackerTemplates = ref([]);
const isEditing = ref(false);
const loading = ref(true);
const error = ref('');
const selectedTemplate = ref({
  name: '',
  metrics: []
});

async function fetchTemplates() {
  loading.value = true;
  error.value = '';
  
  try {
    const result = await getTrackers();
    if (result.error) {
      error.value = result.error;
    } else {
      trackerTemplates.value = result.data;
    }
  } catch (e) {
    error.value = 'Failed to load tracker templates';
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  fetchTemplates();
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

async function handleSaveTemplate(templateData) {
  let apiResult;

  try {
    if (isEditing.value) {
      apiResult = await updateTemplate(templateData);
    } else {
      apiResult = await createTemplate(templateData);
    }

    if (apiResult.error) {
      error.value = apiResult.error;
      return;
    }

    // Refresh the templates list after successful save
    await fetchTemplates();
    showDialog.value = false;
  } catch (e) {
    error.value = 'Failed to save template';
    console.error('Error saving template:', e);
  }
}
</script>