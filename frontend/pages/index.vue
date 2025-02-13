<template>
    <div class="flex justify-center items-center min-h-screen">
      <div class="text-center">
        <img src="/logo_bg_gray_900.png" alt="Supreme Strength Coaching" class="w-64 mx-auto">
        <div v-if="authStore.user" class="text-gray-400"> Hello {{  authStore.user.username  }}</div>
      </div>
    </div>
</template>
  
<script setup>
import { useAuthStore } from '~/stores/auth';
const authStore = useAuthStore();
const user = computed(() => authStore.user);
onMounted(async () => {
  await authStore.fetchUser();
});
</script>