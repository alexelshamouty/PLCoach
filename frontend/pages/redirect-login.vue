<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-900">
    <div class="w-16 h-16 border-4 border-gray-300 border-t-yellow-400 rounded-full animate-spin"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '~/stores/auth';

const router = useRouter();
const authStore = useAuthStore();

onMounted(async () => {
  try {
    await authStore.fetchUser();
    if (authStore.user) {
      if (authStore.admin) {
        router.push('/admin/adminDashboard');
      } else {
        router.push(`/users/profile/${authStore.user.userId}`);
      }
    } else {
      router.push('/login');
    }
  } catch (error) {
    console.error('Error during redirect login:', error);
    router.push('/login');
  }
});
</script>
