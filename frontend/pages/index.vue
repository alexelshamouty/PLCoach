<template>
    <div class="flex justify-center items-center min-h-screen bg-gray-900 px-4 sm:px-0">
      <div class="text-center w-full max-w-md">
        <div class="bg-gray-800 p-1 rounded-full mx-auto">
          <img src="https://d2cu7vju76n2na.cloudfront.net/powerfull-duck.webp" 
               alt="Sweaty Duck Coaching" 
               class="w-48 sm:w-64 mx-auto rounded-full border-4 border-blue-400 shadow-lg">
        </div>
        <div v-if="user" class="text-gray-400 mt-4 text-lg"> Hello {{  user?.username  }}</div>
        <div v-if="admin" class="text-gray-400 mt-2"> 
          Check on your 
          <NuxtLink to="/admin/adminDashboard" class="text-white py-2 hover:text-blue-400" > 
            Athletes 
          </NuxtLink>
        </div>
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