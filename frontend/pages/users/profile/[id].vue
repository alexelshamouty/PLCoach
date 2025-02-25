<template>
  <div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <div class="w-full max-w-4xl p-6 rounded-lg shadow-md">
      <!-- New User Info Card -->
      <div class="bg-gray-800 rounded-xl p-6 mb-6 shadow-lg">
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-3xl font-bold text-blue-400">{{ athlete?.Name }}</h1>
            <div class="mt-2 space-y-1">
                <p class="text-gray-300">
                  <span class="font-semibold text-blue-400">Gender:</span> 
                  <span class="ml-2 capitalize text-yellow-400">{{ athlete?.Gender }}</span>
                </p>
                <p class="text-gray-300">
                  <span class="font-semibold text-blue-400">Weight:</span> 
                  <span class="ml-2 text-yellow-400">{{ athlete?.Weight }} kg</span>
                </p>
                <p class="text-gray-300">
                  <span class="font-semibold text-blue-400">Email:</span> 
                  <span class="ml-2 text-yellow-400">{{ athlete?.Email }}</span>
                </p>
            </div>
          </div>
          <!-- Add a placeholder avatar or icon -->
          <div class="bg-gray-700 rounded-full p-4">
            <svg class="w-16 h-16 text-gray-400" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
            </svg>
          </div>
        </div>
      </div>

      <h2 class="text-2xl font-semibold text-center mb-4">Athlete {{ username }} Profile</h2>
      <div class="bg-gray-700 p-4 rounded-lg flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
        <!-- First Dropdown -->
        <select v-model="selectedOption1" class="w-full md:w-1/2 p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
          <option value="" disabled>Select Block</option>
          <option v-for="option in options1" :key="option.id" :value="option.id">
            {{ option.label }}
          </option>
        </select>

        <!-- Second Dropdown -->
        <select v-model="selectedOption2" class="w-full md:w-1/2 p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
          <option value="" disabled>Select Week</option>
          <option v-for="option in filteredOptions2" :key="option.id" :value="option.id">
            {{ option.label }}
          </option>
        </select>
      </div>
      <!-- Training -->
      <div class="bg-gray-900 text-white p-6 rounded-lg shadow-md mt-4">
        <div v-for="(item, index) in filteredOptions3" :key="index" class="border-b border-gray-600">
          <button @click="toggle(index)" class="w-full flex justify-between items-center p-4 focus:outline-none">
            <span class="font-semibold">{{ item.title }}</span>
            <span :class="{'rotate-180': activeIndex === index}" class="transition-transform duration-300">
              ⬇️
            </span>
          </button>
          <div v-if="activeIndex === index" class="p-4 text-gray-300">
            <table class="w-full border-collapse text-sm">
              <thead>
                <tr class="bg-gray-800 text-gray-300">
                  <th class="py-2 px-4 text-left">Exercise</th>
                  <th class="py-2 px-4 text-left">Label</th>
                  <th class="py-2 px-4 text-center">Sets</th>
                  <th class="py-2 px-4 text-center">Reps</th>
                  <th class="py-2 px-4 text-center">RPE</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(exercise, i) in item.content" :key="i" class="border-b border-gray-700 hover:bg-gray-800">
                  <td class="py-2 px-4 cursor-pointer" @click="openDialog(exercise)">{{ exercise.name }}</td>
                  <td class="py-2 px-4">
                    <button :style="{ backgroundColor: getLabelColor(exercise.label) }" class="text-black px-4 py-2 rounded-full hover:opacity-75 transition">
                      {{ exercise.label }}
                    </button>
                  </td>
                  <td class="py-2 px-4 text-center">{{ exercise.sets }}</td>
                  <td class="py-2 px-4 text-center">{{ exercise.reps }}</td>
                  <td class="py-2 px-4 text-center font-semibold text-yellow-400">{{ exercise.rpe }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <!-- Dialog -->
    <div v-if="dialogOpen" class="fixed inset-0 bg-black bg-opacity-70 flex items-center justify-center z-50">
      <div class="bg-gray-800 bg-opacity-90 p-6 rounded-2xl shadow-lg w-full max-w-2xl">
        <div class="flex justify-center mb-4">
          <h3 class="text-m font-semibold text-center px-4 py-2" :style="{ backgroundColor: getLabelColor(selectedExercise.label), color: 'white', borderRadius: '0.375rem' }">{{ selectedExercise.name }}</h3>
        </div>
        <p class="mb-4 text-gray-300 text-center">{{ selectedExercise.comments }}</p>
        <p class="mb-4 text-gray-300 text-center">Protocol: {{ selectedExercise.sets }} sets of {{ selectedExercise.reps }} reps at RPE {{ selectedExercise.rpe }}</p>
        <form @submit.prevent="submitDialog">
          <table class="w-full border-collapse text-sm">
            <thead>
              <tr class="bg-gray-700 text-gray-300">
                <th class="py-2 px-4 text-left">Set</th>
                <th class="py-2 px-4 text-center">Reps</th>
                <th class="py-2 px-4 text-center">RPE</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="set in selectedExercise.sets" :key="set" class="border-b border-gray-600">
                <td class="py-2 px-4 text-left">
                  Set {{ set }}
                </td>
                <td class="py-2 px-4 text-center">
                  <input type="text" v-model="selectedExercise.reps" class="w-full px-2 py-1 bg-gray-700 text-white rounded-md" />
                </td>
                <td class="py-2 px-4 text-center">
                  <input type="text" v-model="selectedExercise.rpe" class="w-full px-2 py-1 bg-gray-700 text-white rounded-md" />
                </td>
              </tr>
            </tbody>
          </table>
          <div class="mt-4">
            <textarea v-model="selectedExercise.comments" placeholder="Comments on this exercise" class="w-full px-2 py-1 bg-gray-700 text-white rounded-md"></textarea>
          </div>
          <div class="mt-4 flex justify-end space-x-2">
            <button @click="closeDialog" type="button" class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition">
              Close
            </button>
            <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600 transition">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { useAthleteStore } from '~/stores/athlete';
import { useTrainingStore } from '~/stores/training';
import { useLabelsStore } from '~/stores/labels';
import { useBlocksStore } from '~/stores/blocks';
import { useWeeksStore } from '~/stores/weeks';

const athleteStore = useAthleteStore();
const { athletes, currentAthlete } = storeToRefs(athleteStore);
const route = useRoute();
const userId = route.params.id;

// Update the athlete computed property to use currentAthlete
const athlete = computed(() => currentAthlete.value);

// Update the onMounted hook to fetch single athlete
onMounted(async () => {
  await athleteStore.fetchAthlete(userId);
});

const blocksStore = useBlocksStore();
const options1 = ref(blocksStore.getBlocksByIds(athlete.value?.blocks?.map(block => block.id) || []));
const selectedOption1 = ref(options1.value.length ? options1.value[options1.value.length - 1].id : "");

const weeksStore = useWeeksStore();
const options2 = computed(() => weeksStore.getWeeksByBlockId(selectedOption1.value));

const filteredOptions2 = ref(options2.value || []);
watch(() => options2.value, (newVal) => {
  filteredOptions2.value = newVal || [];
});

const selectedOption2 = ref(
  filteredOptions2.value.length ? filteredOptions2.value[filteredOptions2.value.length - 1].id : ""
);

const trainingStore = useTrainingStore();
const items = computed(() => trainingStore.items);

const labelsStore = useLabelsStore();
const labels = computed(() => labelsStore.labels);

function getLabelColor(label) {
  return labelsStore.getColorByLabel(label);
}

const filteredOptions3 = ref(items.value[selectedOption2.value] || []);
watch(() => trainingStore.items[selectedOption2.value], (newItems) => {
  filteredOptions3.value = newItems || [];
}, { deep: true });

watch(() => selectedOption2.value, (newVal) => {
  filteredOptions3.value = items.value[newVal] || [];
});

const activeIndex = ref(null);

const toggle = (index) => {
  activeIndex.value = activeIndex.value === index ? null : index;
};

const dialogOpen = ref(false);
const selectedExercise = ref({});

function openDialog(exercise) {
  selectedExercise.value = exercise;
  dialogOpen.value = true;
}

function closeDialog() {
  dialogOpen.value = false;
}

function submitDialog() {
  // Log the changes
  console.log("Submitted changes:", selectedExercise.value);
  closeDialog();
}
</script>
