<template>
    <div>
        <div v-if="user?.username"> Bye ...! </div>
        <div v-else> You have been logged out. </div>
    </div>
</template>

<script setup>
import { useAuthStore } from '~/stores/auth';

const router = useRouter();
const authStore = useAuthStore();
import { storeToRefs } from 'pinia';
const { user,loading } = storeToRefs(authStore);

onMounted(async () => {
  await authStore.logout();
  authStore.loading = false;
  await navigateTo('/');
});
</script>