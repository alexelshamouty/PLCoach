<template>
  <button 
    @click="openVideoManager" 
    class="ml-2 p-1 bg-gray-700 rounded hover:bg-gray-600" 
    title="Manage Videos">
    <Icon name="heroicons:video-camera-solid" class="text-lg text-white" />
  </button>
</template>

<script setup>
const emit = defineEmits(['click']);

function openVideoManager() {
  emit('click');
}
</script>
