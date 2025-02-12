<script setup lang="ts">
import { NuxtLayout } from '#components';
import { useAuthStore } from './stores/auth';
import { onMounted } from 'vue';

const authStore = useAuthStore();
onMounted(() => {
  authStore.fetchUser();
});
</script>

<template>
    <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>
