<template>
  <div class="bg-gray-900 min-h-screen text-white">
    <!-- Navbar -->
      <Navbar />
    <!-- Page Content -->
    <slot />
  </div>
</template>

<script setup>
import Navbar from '~/components/Navbar.vue';
</script>