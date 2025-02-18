<template>
  <div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <div class="w-full max-w-4xl p-6 rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold text-center mb-4">Athlete {{ username }} Profile</h2>
      <div class="bg-gray-700 p-4 rounded-lg flex space-x-4">
        <!-- First Dropdown -->
        <select v-model="selectedOption1" class="w-1/2 p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
          <option value="" disabled>Select Block</option>
          <option v-for="option in options1" :key="option.id" :value="option.id">
            {{ option.label }}
          </option>
        </select>

        <!-- Second Dropdown -->
        <select v-model="selectedOption2" class="w-1/2 p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
          <option value="" disabled>Select Week</option>
          <option v-for="option in filteredOptions2" :key="option.id" :value="option.id">
            {{ option.label }}
          </option>
        </select>
      </div>
      <!-- Training -->
      <div class="bg-gray-900 text-white p-6 rounded-lg shadow-md">
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
                  <th class="py-2 px-4 text-center">Comments</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(exercise, i) in item.content" :key="i" class="border-b border-gray-700 hover:bg-gray-800">
                  <td class="py-2 px-4">{{ exercise.name }}</td>
                  <td class="py-2 px-4">
                    <button :style="{ backgroundColor: getLabelColor(exercise.label) }" class="text-black px-4 py-2 rounded-full hover:opacity-75 transition">
                      {{ exercise.label }}
                    </button>
                  </td>
                  <td class="py-2 px-4 text-center">{{ exercise.sets }}</td>
                  <td class="py-2 px-4 text-center">{{ exercise.reps }}</td>
                  <td class="py-2 px-4 text-center font-semibold text-yellow-400">{{ exercise.rpe }}</td>
                  <td class="py-2 px-4 text-center font-semibold text-yellow-400">{{ exercise.comments }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { useAthleteStore } from '~/stores/athlete';
import { useTrainingStore } from '~/stores/training';
import { useLabelsStore } from '~/stores/labels';
import { useBlocksStore } from '~/stores/blocks';
import { useWeeksStore } from '~/stores/weeks';

const username = ref("");
const athleteStore = useAthleteStore();
const { athletes } = storeToRefs(athleteStore);
const route = useRoute();
const userId = route.params.id;
const athlete = computed(() => athletes.value.find(a => a.id === parseInt(userId)));
username.value = athlete.value?.username;

const blocksStore = useBlocksStore();
const options1 = ref(blocksStore.getBlocksByIds(athlete.value?.blocks.map(block => block.id) || []));
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
</script>
