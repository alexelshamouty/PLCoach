<template>
  <div v-if="modelValue" class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50 p-4">
    <div class="bg-gray-800 bg-opacity-90 p-6 rounded-2xl shadow-lg w-full max-w-2xl mx-auto">
      <ErrorAlert :message="error" @clear="error = ''" />
      
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
            <tr v-for="(item, index) in metrics" 
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
          @click="handleClose"
          class="bg-red-500 text-white px-6 py-2 rounded-lg hover:bg-red-600 transition"
        >
          Cancel
        </button>
        <button 
          @click="handleSave"
          :disabled="!templateName.trim()"
          class="bg-green-500 text-white px-6 py-2 rounded-lg hover:bg-green-600 transition disabled:opacity-50"
        >
          {{ isEditing ? 'Update' : 'Save' }} Template
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits, defineProps, watch } from 'vue';
import ErrorAlert from '~/components/shared/ErrorAlert.vue';

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true
  },
  isEditing: {
    type: Boolean,
    default: false
  },
  template: {
    type: Object,
    default: () => ({
      templateName: '',
      metrics: []
    })
  }
});

const emits = defineEmits([
  'update:modelValue',
  'save'
]);

const templateName = ref('');
const metrics = ref([]);
const newMetric = ref({
  metric: '',
  unit: ''
});
const error = ref('');

watch(() => props.template, (newTemplate) => {
  templateName.value = newTemplate.templateName || newTemplate.TemplateName || '';
  metrics.value = [...(newTemplate.metrics || [])];
}, { immediate: true });

function addMetric() {
  if (!newMetric.value.metric || !newMetric.value.unit) {
    error.value = 'Both metric name and unit are required';
    return;
  }
  
  metrics.value.push({
    metric: newMetric.value.metric,
    unit: newMetric.value.unit
  });
  newMetric.value.metric = '';
  newMetric.value.unit = '';
}

function removeMetric(index) {
  metrics.value.splice(index, 1);
}

function handleClose() {
  emits('update:modelValue', false);
}

function handleSave() {
  if (!templateName.value.trim()) {
    error.value = 'Template name is required';
    return;
  }
  
  if (metrics.value.length === 0) {
    error.value = 'At least one metric is required';
    return;
  }

  emits('save', {
    templateName: templateName.value,
    metrics: metrics.value,
    oldName: props.template.templateName || props.template.TemplateName // Add oldName field
  });
}
</script>