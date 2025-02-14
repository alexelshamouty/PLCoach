<template>
    <div class="flex justify-center items-center min-h-screen">
      <div class="text-center">
        <img src="/logo_bg_gray_900.png" alt="Sweaty Duck Coaching" class="w-64 mx-auto">
        <div v-if="user" class="text-gray-400"> Hello {{  user?.username  }}</div>
        <div v-if="admin" class="text-gray-400"> Check on your <NuxtLink to="/adminDashboard" class="text-white py-2" > Atheletes </NuxtLink></div>
      </div>
    </div>
</template>
  
<script setup>
import { useAuthStore } from '~/stores/auth';
const authStore = useAuthStore();
const {user, groups, admin, loading} = storeToRefs(authStore);
onMounted(async () => {
  await authStore.fetchUser();
});
</script>