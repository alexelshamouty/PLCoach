<template>
  <div class="container mx-auto p-4">
    <!-- Main trackers templates table -->
    <div class="mb-6">
      <h2 class="text-xl font-bold mb-4">Current Tracker Templates</h2>
      <div class="space-y-6">
        <div v-for="template in trackerTemplates" :key="template.name" class="bg-gray-800 rounded-lg p-4">
          <h3 @click="editTemplate(template)" 
              class="text-lg font-semibold mb-3 cursor-pointer hover:text-blue-400 transition-colors">
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
      @click="openNewDialog()"
      class="bg-green-500 text-white px-6 py-2 rounded-lg hover:bg-green-600 transition"
    >
      Create new tracker template
    </button>

    <!-- Dialog -->
    <div v-if="showDialog" class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50 p-4">
      <div class="bg-gray-800 bg-opacity-90 p-6 rounded-2xl shadow-lg w-full max-w-2xl mx-auto">
        <h3 class="text-xl font-bold mb-4">{{ isEditing ? 'Edit' : 'Create New' }} Tracker Template</h3>

        <!-- Template name input -->
        <div class="mb-6">
          <input 
            type="text" 
            v-model="templateName" 
            placeholder="Template Name"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded-md mb-4"
          />
        </div>

        <!-- New metrics form -->
        <form @submit.prevent="addMetric" class="mb-6 space-y-4">
          <div class="flex gap-4">
            <div class="flex-1">
              <input 
                type="text" 
                v-model="newMetric.metric" 
                placeholder="Metric"
                class="w-full px-3 py-2 bg-gray-700 text-white rounded-md"
              />
            </div>
            <div class="flex-1">
              <input 
                type="text" 
                v-model="newMetric.unit" 
                placeholder="Unit"
                class="w-full px-3 py-2 bg-gray-700 text-white rounded-md"
              />
            </div>
            <button 
              type="submit"
              class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600 transition"
            >
              Add
            </button>
          </div>
        </form>

        <!-- Table of added metrics -->
        <div class="mb-6">
          <table class="w-full bg-gray-700 rounded-lg overflow-hidden">
            <thead>
              <tr class="bg-gray-600">
                <th class="px-4 py-2 text-left">Metric</th>
                <th class="px-4 py-2 text-left">Unit</th>
                <th class="px-4 py-2 text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in tempMetrics" 
                  :key="index" 
                  class="border-b border-gray-600">
                <td class="px-4 py-2">{{ item.metric }}</td>
                <td class="px-4 py-2">{{ item.unit }}</td>
                <td class="px-4 py-2 text-center">
                  <button 
                    @click="removeMetric(index)"
                    class="text-red-400 hover:text-red-300 transition-colors"
                  >
                    Remove
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Dialog buttons -->
        <div class="flex justify-end gap-4">
          <button 
            @click="closeDialog"
            class="bg-red-500 text-white px-6 py-2 rounded-lg hover:bg-red-600 transition"
          >
            Cancel
          </button>
          <button 
            @click="saveTemplate"
            :disabled="!templateName.trim()"
            class="bg-green-500 text-white px-6 py-2 rounded-lg hover:bg-green-600 transition disabled:opacity-50"
          >
            {{ isEditing ? 'Update' : 'Save' }} Template
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const showDialog = ref(false);
const trackerTemplates = ref([]);
const tempMetrics = ref([]);
const templateName = ref('');
const isEditing = ref(false);
const editingIndex = ref(-1);
const newMetric = ref({
  metric: '',
  unit: ''
});

function openNewDialog() {
  isEditing.value = false;
  editingIndex.value = -1;
  templateName.value = '';
  tempMetrics.value = [];
  showDialog.value = true;
}

function editTemplate(template) {
  isEditing.value = true;
  editingIndex.value = trackerTemplates.value.findIndex(t => t.name === template.name);
  templateName.value = template.name;
  tempMetrics.value = [...template.metrics];
  showDialog.value = true;
}

function addMetric() {
  if (newMetric.value.metric && newMetric.value.unit) {
    tempMetrics.value.push({
      metric: newMetric.value.metric,
      unit: newMetric.value.unit
    });
    newMetric.value.metric = '';
    newMetric.value.unit = '';
  }
}

function removeMetric(index) {
  tempMetrics.value.splice(index, 1);
}

function closeDialog() {
  showDialog.value = false;
  tempMetrics.value = [];
  templateName.value = '';
  newMetric.value = { metric: '', unit: '' };
  isEditing.value = false;
  editingIndex.value = -1;
}

function saveTemplate() {
  if (templateName.value.trim() && tempMetrics.value.length > 0) {
    const templateData = {
      name: templateName.value,
      metrics: [...tempMetrics.value]
    };

    if (isEditing.value && editingIndex.value !== -1) {
      trackerTemplates.value[editingIndex.value] = templateData;
    } else {
      trackerTemplates.value.push(templateData);
    }
    
    console.log('Saving template:', templateData);
    closeDialog();
  }
}
</script>