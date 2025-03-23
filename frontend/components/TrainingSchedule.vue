<template>
  <div class="bg-gray-900 text-white p-6 rounded-lg shadow-md mt-4">
    <div v-for="(item, index) in sortedItems" :key="index" class="border-b border-gray-600">
      <div class="w-full flex justify-between items-center p-4">
        <button @click="toggle(index)" class="flex-1 flex justify-between items-center focus:outline-none">
          <span class="font-semibold">{{ item.title }}</span>
          <span :class="{'rotate-180': activeIndex === index}" class="transition-transform duration-300">
            ⬇️
          </span>
        </button>
        <button 
          @click="handleDayFinish(index, item.title)"
          class="ml-4 bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded-full transition-colors duration-200 text-xs font-medium">
          Finish Day
        </button>
      </div>
      <div v-if="activeIndex === index" class="p-4 text-gray-300">
        <div class="overflow-x-auto">
          <table class="table-auto w-full border-collapse text-sm">
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
                <td class="py-2 px-4">
                  <button 
                    @click="$emit('exercise-click', exercise, index)"
                    class="text-left hover:text-blue-400 transition-colors duration-200 cursor-pointer w-full flex items-center gap-2">
                    <span>{{ exercise.name }}</span>
                    <span class="text-blue-400 text-sm">📝</span>
                  </button>
                </td>
                <td class="py-2 px-4">
                  <div class="flex items-center gap-2">
                    <button :style="{ backgroundColor: getLabelColor(exercise.label) }" 
                            class="text-black px-4 py-2 rounded-full hover:opacity-75 transition">
                      {{ exercise.label }}
                    </button>
                    <VideoUploadButton @click="openVideoManager(item.title, exercise.name, exercise.label)" />
                  </div>
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

    <!-- Video Manager Dialog -->
    <VideoManager 
      v-if="showVideoManager"
      :show="showVideoManager"
      :block="currentBlock"
      :week="currentWeek"
      :day-id="selectedDayId"
      :exercise-name="selectedExerciseName"
      :exercise-label="selectedExerciseLabel"
      @close="showVideoManager = false"
      @video-uploaded="handleVideoUploaded"
      @video-deleted="handleVideoDeleted"
    />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useLabelsStore } from '~/stores/labels';
import VideoManager from '~/components/shared/VideoManager.vue';
import VideoUploadButton from '~/components/shared/VideoUploadButton.vue';

const props = defineProps({
  days: {
    type: Array,
    required: true
  },
  block: {
    type: String,
    required: true
  },
  week: {
    type: String,
    required: true
  }
});

const emit = defineEmits(['exercise-click', 'day-finished']);

const activeIndex = ref(null);
const labelsStore = useLabelsStore();

const showVideoManager = ref(false);
const selectedDayId = ref('');
const selectedExerciseName = ref('');
const selectedExerciseLabel = ref('');
const currentBlock = ref('');
const currentWeek = ref('');

// Local reactive copy of days
const localDays = ref([]);

// Watch for changes in block and week props
watch(() => props.block, (newBlock) => {
  currentBlock.value = newBlock;
}, { immediate: true });

watch(() => props.week, (newWeek) => {
  currentWeek.value = newWeek;
}, { immediate: true });

// Update localDays whenever props.days changes
watch(() => props.days, (newDays) => {
  if (newDays && newDays.length) {
    localDays.value = [...newDays];
  } else {
    localDays.value = [];
  }
}, { immediate: true, deep: true });

// Sort days based on index
const sortedItems = computed(() => {
  const daysWithIndices = localDays.value.map(day => ({
    ...day,
    index: day.index !== undefined ? parseInt(day.index, 10) : 999
  }));
  console.log('Sorted days:', daysWithIndices);
  return daysWithIndices.sort((a, b) => a.index - b.index);
});

function handleDayFinish(index, dayId) {
  emit('day-finished', { index, dayId });
}

function toggle(index) {
  activeIndex.value = activeIndex.value === index ? null : index;
}

function getLabelColor(label) {
  return labelsStore.getColorByLabel(label);
}

function openVideoManager(dayId, exerciseName, exerciseLabel) {
  selectedDayId.value = dayId;
  selectedExerciseName.value = exerciseName;
  selectedExerciseLabel.value = exerciseLabel;
  showVideoManager.value = true;
}

function handleVideoUploaded(data) {
  console.log('Video uploaded successfully:', data);
}

function handleVideoDeleted(data) {
  console.log('Video deleted successfully:', data);
}
</script>
