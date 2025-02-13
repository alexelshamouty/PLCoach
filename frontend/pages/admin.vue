<template>
    <div v-if="admin">
        <p> Welcome {{user?.username }} </p>
        <p> You are a coach </p>
    </div>
</template>
<script setup>
  import { useAuthStore } from '~/stores/auth';
  import { storeToRefs } from 'pinia';
  const authStore = useAuthStore();
  const { user, admin } = storeToRefs(authStore);
  watchEffect(() => {
    if (user.value?.admin) {
      console.log(user.value)
      console.log(user.value.profile)
      navigateTo('/');
    }
  });

</script>
