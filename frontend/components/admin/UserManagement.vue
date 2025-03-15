<template>
  <div class="mt-4 bg-gray-800 p-4 rounded-lg">
    <button @click="toggleManage" class="w-full flex justify-between items-center p-4 focus:outline-none">
      <h3 class="text-lg font-semibold">Manage Athlete</h3>
      <span :class="{'rotate-180': manageOpen}" class="transition-transform duration-300">
        ⬇️
      </span>
    </button>
    <div v-if="manageOpen" class="p-4">
      <!-- Add block -->
      <div class="mt-4 bg-gray-800 p-4 rounded-lg">
        <h3 class="text-lg font-semibold">Add Block</h3>
        <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
          <input v-model="newBlockLabel" placeholder="Block Label" class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
          <button @click="handleAddBlock" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-purple-600 rounded-lg hover:bg-purple-700">
            Add Block
          </button>
        </div>
      </div>
      <!-- Add week -->
      <div class="mt-4 bg-gray-800 p-4 rounded-lg">
        <h3 class="text-lg font-semibold">Add a New Week</h3>
        <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
          <input v-model="newWeekTitle" placeholder="Enter week number (e.g., Week 4)" class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
          <button @click="handleAddWeek" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-purple-600 rounded-lg hover:bg-purple-700">
            Add Week
          </button>
        </div>
      </div>
      <!-- Add day -->
      <div class="mt-4 bg-gray-800 p-4 rounded-lg">
        <h3 class="text-lg font-semibold">Add a New Day</h3>
        <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
          <input v-model="newDayTitle" placeholder="Enter day (e.g., Wednesday)" class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
          <button @click="handleAddDay" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-blue-600 rounded-lg hover:bg-blue-700">
            Add Day
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const manageOpen = ref(false);
const newBlockLabel = ref('');
const newWeekTitle = ref('');
const newDayTitle = ref('');

const emit = defineEmits(['add-block', 'add-week', 'add-day']);

function toggleManage() {
  manageOpen.value = !manageOpen.value;
}

function handleAddBlock() {
  emit('add-block', newBlockLabel.value);
  newBlockLabel.value = '';
}

function handleAddWeek() {
  emit('add-week', newWeekTitle.value);
  newWeekTitle.value = '';
}

function handleAddDay() {
  emit('add-day', newDayTitle.value);
  newDayTitle.value = '';
}
</script>
