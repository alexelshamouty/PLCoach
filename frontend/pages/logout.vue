<template>
    <div>
        <div v-if="authStore.loading"> Bye ...! </div>
        <div v-else> You have been logged out. </div>
    </div>
</template>

<script setup>
import { useAuthStore } from '~/stores/auth';

const router = useRouter();
const authStore = useAuthStore();

onMounted(async () => {
  await authStore.logout();
  authStore.loading = false;
  await router.navigateTo('/login');
});
</script>