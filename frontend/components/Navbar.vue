<template>
  <div v-if=loading> 
  </div>
  <div v-else>
    <nav class="bg-gray-800 px-6 py-4 flex items-center justify-between relative z-40">
      <!-- Mobile Menu Button -->
      <button @click="toggleMenu" class="text-white text-2xl">
        ☰
      </button>  
      <!-- Logo -->
      <NuxtLink to="/" class="flex items-center">
        <img src="https://d2cu7vju76n2na.cloudfront.net/powerfull-duck.webp" alt="Logo" class="w-12 h-12 mr-2">
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
  
    <!-- Backdrop overlay -->
    <div v-if="menuOpen" 
         class="fixed inset-0 bg-black/30 backdrop-blur-sm z-40 transition-opacity duration-300"
         @click="toggleMenu">
    </div>

    <!-- Mobile Menu (Dropdown) -->
    <div v-if="menuOpen" 
         class="fixed left-0 top-0 w-64 h-full bg-gray-800 p-4 shadow-lg z-50 transition-transform duration-300 ease-in-out">
      <!-- Added profile image -->
      <div class="flex justify-center mb-4">
        <img 
          src="https://d2cu7vju76n2na.cloudfront.net/powerfull-duck.webp" 
          alt="Profile" 
          class="w-24 h-24 rounded-full border-2 border-yellow-400"
        >
      </div>
      
      <NuxtLink 
        v-if="user" 
        :to="`/users/profile/${user.userId}`" 
        class="block text-white py-2 hover:bg-gray-700 rounded px-2"
        @click="toggleMenu"
      >
        Profile
      </NuxtLink>
      <NuxtLink 
        to="/contact" 
        class="block text-white py-2 hover:bg-gray-700 rounded px-2"
        @click="toggleMenu"
      >
        Contact
      </NuxtLink>

      <!-- Admin section -->
      <NuxtLink 
        v-if="admin" 
        to="/admin/adminDashboard" 
        class="block text-white py-2 hover:bg-gray-700 rounded px-2"
        @click="toggleMenu"
      >
        Admin
      </NuxtLink>

      <!-- User stuff -->
      <NuxtLink 
        v-if="user?.username" 
        class="block text-white py-2 hover:bg-gray-700 rounded px-2" 
        to="/logout"
        @click="toggleMenu"
      >
        Logout
      </NuxtLink>
      <NuxtLink 
        v-if="!user?.username" 
        class="block text-white py-2 hover:bg-gray-700 rounded px-2" 
        to="/login"
        @click="toggleMenu"
      >
        Login
      </NuxtLink>
      <NuxtLink 
        v-if="!user?.username" 
        class="block text-white py-2 hover:bg-gray-700 rounded px-2" 
        to="/signup"
        @click="toggleMenu"
      >
        Signup
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onUnmounted } from 'vue';
import { useAuthStore } from '~/stores/auth';
import { storeToRefs } from 'pinia';

const authStore = useAuthStore();
const {user, groups, admin, loading} = storeToRefs(authStore);

const menuOpen = ref(false);
const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
  // Prevent body scroll when menu is open
  if (menuOpen.value) {
    document.body.style.overflow = 'hidden';
  } else {
    document.body.style.overflow = 'auto';
  }
};

// Cleanup on component unmount
onUnmounted(() => {
  document.body.style.overflow = 'auto';
});
</script>

<style scoped>
.backdrop-blur-sm {
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}
</style>