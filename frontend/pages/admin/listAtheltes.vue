<template>
    <div class="bg-gray-900 min-h-screen text-white flex flex-col items-center p-6">
      <h1 class="text-3xl font-bold mb-6">Athlete List</h1>
  
      <div class="w-full max-w-4xl bg-gray-800 p-6 rounded-lg shadow-lg">
        <div class="overflow-x-auto">
          <table class="w-full border-collapse border border-gray-700">
            <thead class="bg-gray-700">
              <tr>
                <th class="px-4 py-3 border border-gray-600">Username</th>
                <th class="px-4 py-3 border border-gray-600">Email</th>
                <th class="px-4 py-3 border border-gray-600">Weight</th>
                <th class="px-4 py-3 border border-gray-600">Gender</th>
                <th class="px-4 py-3 border border-gray-600">Program</th>
                <th class="px-4 py-3 border border-gray-600">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="athlete in athletes" :key="athlete.id"
                  class="hover:bg-gray-700 transition">
                <td class="px-4 py-3 border border-gray-600">
                    <NuxtLink :to="`/users/athlete/${athlete.id}`" class="text-blue-400 hover:text-blue-300 underline">
                    {{ athlete.username }}
                    </NuxtLink>
                </td>
                <td class="px-4 py-3 border border-gray-600">{{ athlete.email }}</td>
                <td class="px-4 py-3 border border-gray-600">{{ athlete.weight }} kg</td>
                <td class="px-4 py-3 border border-gray-600">{{ athlete.gender }}</td>
                <td class="px-4 py-3 border border-gray-600">
                    <NuxtLink :to="`/users/athlete/${athlete.id}`" class="text-blue-400 hover:text-blue-300 underline">
                    {{ athlete.program }}
                    </NuxtLink>
                </td>
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
  import { ref } from 'vue';
  import {deleteAthletes} from '~/composables/deleteAthlete';
  // Sample athlete data (replace with API call if needed)
  const athletes = ref([
    { id: 1, username: "johndoe", email: "john@example.com", weight: 75, gender: "Male", program: "Strength Training" },
    { id: 2, username: "janedoe", email: "jane@example.com", weight: 60, gender: "Female", program: "Cardio" },
    { id: 3, username: "mike99", email: "mike@example.com", weight: 85, gender: "Male", program: "CrossFit" },
    { id: 4, username: "sara_k", email: "sara@example.com", weight: 65, gender: "Female", program: "Yoga" }
  ]);

  const { confirmDelete } = deleteAthletes(athletes);

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
  