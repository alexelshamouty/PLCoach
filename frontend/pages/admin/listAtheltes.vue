<template>
    <div class="bg-gray-900 min-h-screen text-white flex flex-col items-center p-6">
      <!-- Error Alert -->
      <div v-if="error" class="w-full max-w-4xl bg-red-500 text-white px-6 py-4 rounded-lg mb-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-2">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>{{ error }}</span>
          </div>
          <button @click="error = null" class="hover:text-gray-200">&times;</button>
        </div>
      </div>

      <h1 class="text-3xl font-bold mb-6">Athlete List</h1>
  
      <!-- Loading State -->
      <div v-if="loading" class="w-full max-w-4xl bg-gray-800 p-6 rounded-lg shadow-lg flex justify-center">
        <span class="text-blue-400">Loading athletes...</span>
      </div>

      <!-- Athletes Table -->
      <div v-else class="w-full max-w-4xl bg-gray-800 p-6 rounded-lg shadow-lg">
        <div class="overflow-x-auto">
          <table class="w-full border-collapse border border-gray-700">
            <thead class="bg-gray-700">
              <tr>
                <th class="px-4 py-3 border border-gray-600">Preferred Name</th>
                <th class="px-4 py-3 border border-gray-600">Name</th>
                <th class="px-4 py-3 border border-gray-600">Email</th>
                <th class="px-4 py-3 border border-gray-600">Weight</th>
                <th class="px-4 py-3 border border-gray-600">Gender</th>
                <th class="px-4 py-3 border border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="athlete in athletes" :key="athlete.id"
                  class="hover:bg-gray-700 transition">
                <td class="px-4 py-3 border border-gray-600">
                    <NuxtLink :to="`/admin/users/${athlete.Userid}`" class="text-blue-400 hover:text-blue-300 underline">
                    {{ athlete.username }}
                    </NuxtLink>
                </td>
                <td class="px-4 py-3 border border-gray-600">{{ athlete.name }}</td>
                <td class="px-4 py-3 border border-gray-600">{{ athlete.email }}</td>
                <td class="px-4 py-3 border border-gray-600">{{ athlete.weight }} kg</td>
                <td class="px-4 py-3 border border-gray-600">{{ athlete.gender }}</td>
                <td class="px-4 py-3 border border-gray-600 flex space-x-4">
                <!-- Direct Delete Button -->
                <button @click="confirmDelete(athlete.id)" 
                        class="text-red-400 hover:text-red-300 underline">
                  Delete Now
                </button>
              </td>        
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useAthleteManagement } from '~/composables/manageAthletes';
  import { deleteAthletes } from '~/composables/deleteAthlete';

  const { athletes, error, loading, fetchAthletes } = useAthleteManagement();
  const { confirmDelete } = deleteAthletes(athletes);

  onMounted(async () => {
    await fetchAthletes();
  });

  </script>
  
  <style scoped>
  table {
    width: 100%;
    text-align: left;
    border-spacing: 0;
  }
  th, td {
    text-align: left;
  }
  </style>
