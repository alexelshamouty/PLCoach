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
        <div v-for="template in trackerTemplates" :key="template.TemplateName" class="bg-gray-800 rounded-lg p-4">
          <div class="flex justify-between items-center mb-3">
            <h3 
              @click="editTemplate(template)" 
              class="text-lg font-semibold cursor-pointer hover:text-blue-400 transition-colors flex items-center gap-2"
            >
              {{ template.TemplateName }}
              <span class="text-sm text-blue-400">(click to edit)</span>
            </h3>
            <button 
              @click="confirmDeleteTemplate(template)"
              class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-lg text-sm transition-colors"
            >
              Delete
            </button>
          </div>
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

    <!-- Template Dialog -->
    <TrackerDialog
      v-model="showDialog"
      :is-editing="isEditing"
      :template="selectedTemplate"
      @save="handleSaveTemplate"
    />

    <!-- Delete Confirmation Dialog -->
    <div v-if="showDeleteConfirm" class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50 p-4">
      <div class="bg-gray-800 bg-opacity-90 p-6 rounded-2xl shadow-lg w-full max-w-md mx-auto">
        <h3 class="text-xl font-bold mb-4">Confirm Delete</h3>
        <p class="mb-6">Are you sure you want to delete the template "{{ templateToDelete?.TemplateName }}"?</p>
        <div class="flex justify-end gap-4">
          <button 
            @click="showDeleteConfirm = false"
            class="bg-gray-500 text-white px-6 py-2 rounded-lg hover:bg-gray-600 transition"
          >
            Cancel
          </button>
          <button 
            @click="handleDeleteTemplate"
            class="bg-red-500 text-white px-6 py-2 rounded-lg hover:bg-red-600 transition"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import TrackerDialog from '~/components/admin/TrackerDialog.vue';
import ErrorAlert from '~/components/shared/ErrorAlert.vue';
import { createTemplate, updateTemplate, getTrackers, deleteTemplate } from '~/composables/trackerManagement';

const showDialog = ref(false);
const trackerTemplates = ref([]);
const isEditing = ref(false);
const loading = ref(true);
const error = ref('');
const selectedTemplate = ref({
  templateName: '',
  metrics: []
});

// Delete confirmation
const showDeleteConfirm = ref(false);
const templateToDelete = ref(null);

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
    templateName: '',
    metrics: []
  };
  showDialog.value = true;
}

function editTemplate(template) {
  isEditing.value = true;
  selectedTemplate.value = {
    templateName: template.TemplateName,
    metrics: template.metrics,
    oldName: template.TemplateName
  };
  showDialog.value = true;
}

function confirmDeleteTemplate(template) {
  templateToDelete.value = template;
  showDeleteConfirm.value = true;
}

async function handleDeleteTemplate() {
  if (!templateToDelete.value || !templateToDelete.value.TemplateName) return;
  
  try {
    const result = await deleteTemplate(templateToDelete.value.TemplateName);
    if (result.error) {
      error.value = result.error;
    } else {
      // Remove the deleted template from the local list
      trackerTemplates.value = trackerTemplates.value.filter(
        template => template.TemplateName !== templateToDelete.value.TemplateName
      );
    }
  } catch (e) {
    error.value = 'Failed to delete template';
    console.error('Error deleting template:', e);
  } finally {
    showDeleteConfirm.value = false;
    templateToDelete.value = null;
  }
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