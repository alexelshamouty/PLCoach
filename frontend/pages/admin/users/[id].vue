<template>
  <div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <div class="w-full max-w-4xl p-6 rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold text-center mb-4">Athlete {{ username }} Program Management</h2>
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
      <!-- Management Section -->
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
              <button @click="addBlock" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-purple-600 rounded-lg hover:bg-purple-700">
                Add Block
              </button>
            </div>
          </div>
          <!-- Add week -->
          <div class="mt-4 bg-gray-800 p-4 rounded-lg">
            <h3 class="text-lg font-semibold">Add a New Week</h3>
            <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
              <input v-model="newWeekTitle" placeholder="Enter week number (e.g., Week 4)" class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
              <button @click="addWeek" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-purple-600 rounded-lg hover:bg-purple-700">
                Add Week
              </button>
            </div>
          </div>
          <!-- Add day -->
          <div class="mt-4 bg-gray-800 p-4 rounded-lg">
            <h3 class="text-lg font-semibold">Add a New Day</h3>
            <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
              <input v-model="newDayTitle" placeholder="Enter day (e.g., Wednesday)" class="w-full p-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
              <button @click="addDay" class="w-full md:w-auto mt-2 md:mt-0 p-2 bg-blue-600 rounded-lg hover:bg-blue-700">
                Add Day
              </button>
            </div>
          </div>
        </div>
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
                  <th class="py-2 px-4 text-center">Comments</th>
                  <th class="py-2 px-4 text-center">Actions</th>
                </tr>
              </thead>
              <div v-if="messageOpen">
                <div @click="toggleMessage()" v-if="allSets" class="mt-6 p-4 bg-yellow-500 text-black text-center rounded-lg shadow-lg animate-bounce">
                  <p class="text-lg font-semibold" :style="{ color: labelColor }">{{ allSets }}</p>
                </div>
              </div>
              <tbody>
                <tr v-for="(exercise, i) in item.content" :key="i" class="border-b border-gray-700 hover:bg-gray-800">
                  <td class="py-2 px-4">{{ exercise.name }}</td>
                  <td class="py-2 px-4">
                    <button @click="countSetsPerWeek(exercise.label)" :style="{ backgroundColor: getLabelColor(exercise.label) }" class="text-black px-4 py-2 rounded-full hover:opacity-75 transition">
                      {{ exercise.label }}
                    </button>
                  </td>
                  <td class="py-2 px-4 text-center">{{ exercise.sets }}</td>
                  <td class="py-2 px-4 text-center">{{ exercise.reps }}</td>
                  <td class="py-2 px-4 text-center font-semibold text-yellow-400">{{ exercise.rpe }}</td>
                  <td class="py-2 px-4 text-center font-semibold text-yellow-400">{{ exercise.comments }}</td>
                  <td class="py-2 px-4 text-center">
                    <button @click="deleteExercise(index, i)" class="text-red-600 hover:text-red-800 transition">
                      ✖️
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
            <!-- Add training -->
            <div class="mt-4 bg-gray-800 p-4 rounded-lg">
              <h3 class="text-lg font-semibold">Add Exercise</h3>
              <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4 mb-2">
                <input v-model="newExerciseName" placeholder="Exercise Name" class="w-full md:w-1/6 p-2 bg-gray-700 text-white rounded-lg outline-none" />
                <select v-model="newExerciseLabel" class="w-full md:w-1/6 p-2 bg-gray-700 text-white rounded-lg outline-none">
                  <option value="" disabled>Select Label</option>
                  <option v-for="(color, label) in labels" :key="label" :value="label">
                    {{ label }}
                  </option>
                </select>
                <input v-model.number="newExerciseSets" placeholder="Sets" type="number" class="w-full md:w-1/6 p-2 bg-gray-700 text-white rounded-lg outline-none" />
                <input v-model.number="newExerciseReps" placeholder="Reps" type="number" class="w-full md:w-1/6 p-2 bg-gray-700 text-white rounded-lg outline-none" />
                <input v-model.number="newExerciseRpe" placeholder="RPE (6-10)" type="number" class="w-full md:w-1/6 p-2 bg-gray-700 text-white rounded-lg outline-none" />
                <input v-model="newExerciseComments" placeholder="Comments" class="w-full md:w-1/6 p-2 bg-gray-700 text-white rounded-lg outline-none" />
              </div>
              <button @click="addExercise(index)" class="w-full mt-2 p-2 bg-green-600 rounded-lg hover:bg-green-700">
                Add Exercise
              </button>
            </div>
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
definePageMeta({ middleware: ['auth-admin'] });

const messageOpen = ref(false);
const allSets = ref(0);
const labelColor = ref("");

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

function countSetsPerWeek(label) {
  trainingStore.countSetsPerWeek(label, selectedOption1.value, selectedOption2.value, allSets, messageOpen);
  labelColor.value = labelsStore.getColorByLabel(label);
}

function getLabelColor(label) {
  return labelsStore.getColorByLabel(label);
}

function toggleMessage() {
  messageOpen.value = !messageOpen.value;
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
  messageOpen.value = false;
};

const newExerciseName = ref("");
const newExerciseLabel = ref("");
const newExerciseSets = ref(0);
const newExerciseReps = ref(0);
const newExerciseRpe = ref(0);
const newExerciseComments = ref("");

function addExercise(dayIndex) {
  const exercise = {
    name: newExerciseName.value,
    label: newExerciseLabel.value,
    sets: newExerciseSets.value,
    reps: newExerciseReps.value,
    rpe: newExerciseRpe.value,
    comments: newExerciseComments.value
  };
  trainingStore.addExercise(selectedOption2.value, dayIndex, exercise);
  newExerciseName.value = "";
  newExerciseLabel.value = "";
  newExerciseSets.value = 0;
  newExerciseReps.value = 0;
  newExerciseRpe.value = 0;
  newExerciseComments.value = "";
}

function deleteExercise(dayIndex, exerciseIndex) {
  trainingStore.deleteExercise(selectedOption2.value, dayIndex, exerciseIndex);
}

const newBlockLabel = ref("");

function addBlock() {
  blocksStore.addBlock(newBlockLabel.value);
  const newBlock = blocksStore.blocks[blocksStore.blocks.length - 1];
  athleteStore.addBlockToAthlete(athlete.value.id, newBlock);
  options1.value = blocksStore.getBlocksByIds(athlete.value?.blocks.map(block => block.id) || []);
  newBlockLabel.value = "";
}

const newWeekTitle = ref("");

function addWeek() {
  weeksStore.addWeek(selectedOption1.value, newWeekTitle.value);
  newWeekTitle.value = "";
}

const newDayTitle = ref("");

function addDay() {
  trainingStore.addDay(selectedOption2.value, newDayTitle.value);
  newDayTitle.value = "";
}

const manageOpen = ref(false);

function toggleManage() {
  manageOpen.value = !manageOpen.value;
}

watch(() => athlete.value.blocks, (newBlocks) => {
  options1.value = blocksStore.getBlocksByIds(newBlocks.map(block => block.id));
}, { deep: true });

watch(() => selectedOption1.value, (newVal) => {
  filteredOptions2.value = weeksStore.getWeeksByBlockId(newVal) || [];
});
</script>
