<template>
    <div class="flex justify-center items-center min-h-screen bg-gray-900">
      <div class="text-center">
        <div class="bg-gray-800 p-1 rounded-full">
          <img src="https://d2cu7vju76n2na.cloudfront.net/powerfull-duck.webp" 
               alt="Sweaty Duck Coaching" 
               class="w-64 mx-auto rounded-full border-4 border-blue-400 shadow-lg">
        </div>
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