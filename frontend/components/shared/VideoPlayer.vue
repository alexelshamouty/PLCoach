<template>
  <div v-if="show" class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50 p-2">
    <div class="bg-gray-800 rounded-lg p-4 sm:p-6 w-full max-w-3xl max-h-[90vh] sm:max-h-[80vh] overflow-y-auto hide-scrollbar">
      <div class="flex justify-between items-center mb-4 sm:mb-6">
        <h2 class="text-lg sm:text-xl font-bold truncate pr-2">{{ title }}</h2>
        <button @click="$emit('close')" class="text-gray-400 hover:text-white flex-shrink-0">
          <Icon name="mdi:close" size="24" />
        </button>
      </div>
      
      <div class="mb-4">
        <video controls class="w-full rounded-lg bg-black">
          <source :src="videoUrl" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>

      <div class="text-gray-300">
        <p class="text-sm sm:text-base mb-2"><span class="font-semibold">Description:</span></p>
        <p class="text-sm sm:text-base">{{ description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  show: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  videoUrl: {
    type: String,
    required: true
  }
});

const emit = defineEmits(['close']);
</script>

<style scoped>
.hide-scrollbar {
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE and Edge */
}
.hide-scrollbar::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera */
}
</style>
