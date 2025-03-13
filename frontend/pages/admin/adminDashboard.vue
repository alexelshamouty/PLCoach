<template>
    <div class="bg-gray-900 min-h-screen text-white flex flex-col items-center p-6">
      <h1 class="text-3xl font-bold mb-6">Admin Dashboard</h1>
  
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 w-full max-w-4xl">
        <!-- Add Athlete -->
        <NuxtLink to="/admin/addAthlete" class="dashboard-card">
          <div class="p-6 bg-blue-600 hover:bg-blue-500 rounded-lg shadow-md text-center">
            <h2 class="text-xl font-semibold">Add Athlete</h2>
            <p class="text-sm mt-2">Create a new athlete profile</p>
          </div>
        </NuxtLink>
    
        <!-- List Athletes -->
        <NuxtLink to="/admin/listAtheltes" class="dashboard-card">
          <div class="p-6 bg-green-600 hover:bg-green-500 rounded-lg shadow-md text-center">
            <h2 class="text-xl font-semibold">List Athletes</h2>
            <p class="text-sm mt-2">View all registered athletes</p>
          </div>
        </NuxtLink>
      </div>
    </div>
  </template>

  <script setup>
  definePageMeta({
  middleware: ['auth-admin'],}
);
  </script>
  <style scoped>
  .dashboard-card {
    transition: transform 0.2s ease-in-out;
  }
  .dashboard-card:hover {
    transform: scale(1.05);
  }
  </style>
  