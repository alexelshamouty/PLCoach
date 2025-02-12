<template>
    <div class="flex justify-center items-center min-h-screen">
      <div class="text-center">
        <img src="/logo_bg_gray_900.png" alt="Supreme Strength Coaching" class="w-64 mx-auto">
        <div v-if="authSore.user" class="text-gray-400"> Hello {{  authSore.user.username  }}</div>
      </div>
    </div>
</template>
  
<script setup>
import { useAuthStore } from '~/stores/auth';
const authSore = useAuthStore();
</script>