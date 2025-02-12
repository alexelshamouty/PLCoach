<template>
<div v-if="authStore.user">
      <NuxtLink to="/logout" class="block text-white py-2">Login</NuxtLink>
</div>
</template>
