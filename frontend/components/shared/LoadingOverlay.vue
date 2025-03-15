<template>
  <div v-if="show" class="fixed inset-0 bg-gray-900 bg-opacity-90 z-50 flex items-center justify-center">
    <div class="flex flex-col items-center">
      <div class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-blue-400 mb-4"></div>
      <p class="text-blue-400 text-lg">{{ message }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  show: {
    type: Boolean,
    default: false
  },
  message: {
    type: String,
    default: 'Loading...'
  }
});
</script>

<style scoped>
.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>
