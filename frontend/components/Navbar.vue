<template>
  <div v-if=loading> 
  </div>
  <div v-else>
    <nav class="bg-gray-800 px-6 py-4 flex items-center justify-between">
      <!-- Mobile Menu Button -->
      <button @click="toggleMenu" class="text-white text-2xl">
        ☰
      </button>  
      <!-- Logo -->
      <NuxtLink to="/" class="flex items-center">
        <img src="/logo_bg_gray_900.png" alt="Logo" class="w-12 h-12 mr-2">
        <span class="text-white text-lg font-bold">Sweaty Duck Coaching </span>
      </NuxtLink>
  
      <!-- Login & Signup Buttons -->
      <div class="hidden md:flex space-x-2">
        <div v-if="authStore.loading" class="text-gray-400">Loading...</div>

        <div v-else-if="authStore.user" class="flex space-x-4 items-center">
          <span class="text-white">Hello, {{ authStore.user.username }}</span>
          <NuxtLink to="/logout" class="bg-red-500 text-white px-4 py-2 rounded">Logout</NuxtLink>
        </div>
        <div v-else class="flex space-x-2">
          <NuxtLink to="/signup" class="bg-yellow-400 text-black px-4 py-2 rounded">Sign-up</NuxtLink>
          <NuxtLink to="/login" class="bg-yellow-400 text-black px-4 py-2 rounded">Login</NuxtLink>
        </div>
      </div>
    </nav>
  
    <!-- Mobile Menu (Dropdown) -->
    <div v-if="menuOpen" class="absolute left-0 w-64 h-full bg-gray-800 p-4 shadow-lg transition-transform duration-300 ease-in-out">
      <NuxtLink to="/dashboard" class="block text-white py-2">Dashboard</NuxtLink>
      <NuxtLink to="/profile" class="block text-white py-2">Profile</NuxtLink>
      <NuxtLink to="/contact" class="block text-white py-2">Contact</NuxtLink>

      <!-- Admin section -->
      <NuxtLink v-if="admin" to="/atheletes" class="block text-white py-2"> Atheletes </NuxtLink>
      <NuxtLink v-if="admin" to="/admin" class="block text-white py-2">Admin</NuxtLink>

      <!-- User stuff -->
      <NuxtLink v-if="user?.username" class="block text-white py-2" to="/logout"> Logout </NuxtLink>
      <NuxtLink v-if="!user?.username" class="block text-white py-2" to="/login"> Login </NuxtLink>
      <NuxtLink v-if="!user?.username" class="block text-white py-2" to="/signup"> Signup </NuxtLink>
    </div>
  </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useAuthStore } from '~/stores/auth';
  import { storeToRefs } from 'pinia';

  const authStore = useAuthStore();
  const {user, groups, admin, loading} = storeToRefs(authStore);

  const menuOpen = ref(false);
  const toggleMenu = () => {
    menuOpen.value = !menuOpen.value;
  };

  watch(() => authStore.user, (newUser) => {
  });
  </script>  