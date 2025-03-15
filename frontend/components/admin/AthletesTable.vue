<template>
  <div class="w-full max-w-4xl bg-gray-800 p-6 rounded-lg shadow-lg">
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
                <NuxtLink :to="`/admin/users/${athlete.id}`" class="text-blue-400 hover:text-blue-300 underline">
                {{ athlete.username }}
                </NuxtLink>
            </td>
            <td class="px-4 py-3 border border-gray-600">{{ athlete.name }}</td>
            <td class="px-4 py-3 border border-gray-600">{{ athlete.email }}</td>
            <td class="px-4 py-3 border border-gray-600">{{ athlete.weight }} kg</td>
            <td class="px-4 py-3 border border-gray-600">{{ athlete.gender }}</td>
            <td class="px-4 py-3 border border-gray-600 flex space-x-4">
              <button @click="$emit('delete', athlete.id)" 
                      class="text-red-400 hover:text-red-300 underline">
                Delete Now
              </button>
            </td>        
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
defineProps({
  athletes: {
    type: Array,
    required: true
  }
});

defineEmits(['delete']);
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
