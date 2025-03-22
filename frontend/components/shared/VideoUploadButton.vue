<template>
  <button 
    @click="openVideoManager" 
    class="ml-2 p-1 bg-gray-700 rounded hover:bg-gray-600" 
    title="Manage Videos">
    <!-- Replacing the Icon component with inline SVG -->
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5 text-white">
      <path d="M4.5 4.5a3 3 0 00-3 3v9a3 3 0 003 3h8.25a3 3 0 003-3v-9a3 3 0 00-3-3H4.5zM19.94 18.75l-2.69-2.69V7.94l2.69-2.69c.944-.945 2.56-.276 2.56 1.06v11.38c0 1.336-1.616 2.005-2.56 1.06z" />
    </svg>
  </button>
</template>

<script setup>
const emit = defineEmits(['click']);

function openVideoManager() {
  emit('click');
}
</script>
