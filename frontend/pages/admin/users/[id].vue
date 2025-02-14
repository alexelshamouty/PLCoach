<template>
<div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <div class="w-full max-w-lg p-6 rounded-lg shadow-md">        
        <h2 class="text-2xl font-semibold text-center mb-4">Athlete {{ username }} Program Managment</h2>
        <div class="bg-gray-700 p-4 rounded-lg flex space-x-4">
            <!-- First Dropdown -->
            <select v-model="selectedOption1" class="w-1/2 p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
            <option value="" disabled>Select Block</option>
            <option v-for="option in options1" :key="option.value" :value="option.value">
                {{ option.label }}
            </option>
            </select>

            <!-- Second Dropdown -->
            <select v-model="selectedOption2" class="w-1/2 p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
            <option value="" disabled>Select Week</option>
            <option v-for="option in filteredOptions2" :key="option.value" :value="option.value">
                {{ option.label }}
            </option>
            </select>
        </div>
        <!-- Add week -->
        <div class="mt-4 bg-gray-800 p-4 rounded-lg">
        <h3 class="text-lg font-semibold">Add a New Week</h3>
        <input v-model="newWeekTitle" placeholder="Enter week number (e.g., Week 4)" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
        <button @click="addWeek" class="w-full mt-2 p-2 bg-purple-600 rounded-lg hover:bg-purple-700">
          Add Week
        </button>
      </div>
        <!-- Add day -->
        <div class="mt-4 bg-gray-800 p-4 rounded-lg">
        <h3 class="text-lg font-semibold">Add a New Day</h3>
        <input v-model="newDayTitle" placeholder="Enter day (e.g., Wednesday)" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
        <button @click="addDay" class="w-full mt-2 p-2 bg-blue-600 rounded-lg hover:bg-blue-700">
          Add Day
        </button>
        </div>
    <div class="bg-gray-900 text-white p-6 w-full max-w-md rounded-lg shadow-md">
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
              <th class="py-2 px-4 text-center">Sets</th>
              <th class="py-2 px-4 text-center">Reps</th>
              <th class="py-2 px-4 text-center">RPE</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(exercise, i) in item.content" :key="i" class="border-b border-gray-700 hover:bg-gray-800">
              <td class="py-2 px-4">{{ exercise.name }}</td>
              <td class="py-2 px-4 text-center">{{ exercise.sets }}</td>
              <td class="py-2 px-4 text-center">{{ exercise.reps }}</td>
              <td class="py-2 px-4 text-center font-semibold text-yellow-400">{{ exercise.rpe }}</td>
            </tr>
          </tbody>
        </table>
        <!-- Add training -->
        <div class="mt-4 bg-gray-800 p-4 rounded-lg">
              <h3 class="text-lg font-semibold">Add Exercise</h3>
              <input v-model="newExerciseName" placeholder="Exercise Name" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none" />
              <input v-model.number="newExerciseSets" placeholder="Sets" type="number" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none" />
              <input v-model.number="newExerciseReps" placeholder="Reps" type="number" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none" />
              <input v-model.number="newExerciseRpe" placeholder="RPE (6-10)" type="number" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none" />
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
  import { ref } from "vue";
  import { useRoute } from "vue-router";
  import { useAthleteStore } from '~/stores/athlete'
  const username = ref("")
  const athleteStore = useAthleteStore();
  const {athletes} = storeToRefs(athleteStore);
  const route = useRoute();
  const userId = route.params.id;
  username.value = athletes.value[userId-1]?.username
  definePageMeta({middleware: ['auth-admin'],});
  const options1 = ref([
    { value: "Block 1", label: "Block 1" },
    { value: "Block 2", label: "Block 2" },
    { value: "Block 3", label: "Block 3" },
]);
const options2 = ref({
    "Block 1": [
        { value: "1", label: "Week1" },
        { value: "2", label: "Week2" },
        { value: "3", label: "Week3" },
    ],
    "Block 2": [
        { value: "4", label: "Week1" },
        { value: "5", label: "Week2" },
        { value: "6", label: "Week3" },
    ],
    "Block 3": [
        { value: "7", label: "Week1" },
        { value: "8", label: "Week2" },
        { value: "9", label: "Week3" },
    ],
});
const selectedOption1 = ref(
    options1.value[options1.value.length - 1].value
);

const filteredOptions2 = computed(() => {
  return options2.value[selectedOption1.value] || [];
});
const selectedOption2 = ref(
  filteredOptions2.value.length ? filteredOptions2.value[filteredOptions2.value.length - 1].value : ""
);

const items = ref({
  "1": [
    { 
      title: "Monday", 
      content: [
        { name: "Bench Press", sets: 4, reps: 10, rpe: 8 },
        { name: "Pull-ups", sets: 3, reps: 12, rpe: 7 },
        { name: "Squats", sets: 4, reps: 8, rpe: 9 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Squat", sets: 5, reps: 10, rpe: 8 },
        { name: "Lunges", sets: 3, reps: 15, rpe: 7 },
        { name: "Leg Press", sets: 4, reps: 12, rpe: 9 }
      ]
    }
  ],
  "2": [
    { 
      title: "Monday", 
      content: [
        { name: "Deadlift", sets: 4, reps: 6, rpe: 9 },
        { name: "Good Mornings", sets: 3, reps: 12, rpe: 8 },
        { name: "Hamstring Curls", sets: 4, reps: 15, rpe: 7 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Squat", sets: 5, reps: 8, rpe: 9 },
        { name: "Leg Extensions", sets: 3, reps: 12, rpe: 7 }
      ]
    }
  ],
  "3": [
    { 
      title: "Monday", 
      content: [
        { name: "Bench Press", sets: 4, reps: 10, rpe: 8 },
        { name: "Dips", sets: 3, reps: 12, rpe: 7 },
        { name: "Push-ups", sets: 4, reps: 15, rpe: 6 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Squat", sets: 4, reps: 8, rpe: 9 },
        { name: "Step-ups", sets: 3, reps: 10, rpe: 7 }
      ]
    },
    { 
      title: "Wednesday", 
      content: [
        { name: "Deadlift", sets: 4, reps: 6, rpe: 10 },
        { name: "Pull-ups", sets: 3, reps: 12, rpe: 7 }
      ]
    }
  ],
  "4": [
    { 
      title: "Monday", 
      content: [
        { name: "Dumbbell Press", sets: 3, reps: 12, rpe: 8 },
        { name: "Incline Press", sets: 3, reps: 10, rpe: 7 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Goblet Squats", sets: 4, reps: 12, rpe: 8 },
        { name: "Lunges", sets: 3, reps: 15, rpe: 7 }
      ]
    }
  ],
  "5": [
    { 
      title: "Monday", 
      content: [
        { name: "Bench Press", sets: 4, reps: 8, rpe: 9 },
        { name: "Triceps Dips", sets: 3, reps: 12, rpe: 7 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Squat", sets: 4, reps: 10, rpe: 8 },
        { name: "Lunges", sets: 3, reps: 15, rpe: 6 }
      ]
    }
  ],
  "6": [
    { 
      title: "Monday", 
      content: [
        { name: "Dips", sets: 3, reps: 12, rpe: 8 },
        { name: "Close-grip Bench Press", sets: 4, reps: 10, rpe: 9 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Front Squats", sets: 4, reps: 8, rpe: 8 },
        { name: "Step-ups", sets: 3, reps: 12, rpe: 7 }
      ]
    },
    { 
      title: "Friday", 
      content: [
        { name: "Front Squats", sets: 4, reps: 8, rpe: 8 },
        { name: "Step-ups", sets: 3, reps: 12, rpe: 7 }
      ]
    }
  ],
  "7": [
    { 
      title: "Monday", 
      content: [
        { name: "Flat Bench Press", sets: 3, reps: 10, rpe: 7 },
        { name: "Incline Bench Press", sets: 4, reps: 8, rpe: 9 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Leg Press", sets: 4, reps: 12, rpe: 8 },
        { name: "Bulgarian Split Squat", sets: 3, reps: 10, rpe: 7 }
      ]
    }
  ],
  "8": [
    { 
      title: "Monday", 
      content: [
        { name: "Barbell Bench Press", sets: 4, reps: 8, rpe: 9 },
        { name: "Dips", sets: 3, reps: 12, rpe: 7 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Box Jumps", sets: 3, reps: 10, rpe: 6 },
        { name: "Lunges", sets: 4, reps: 12, rpe: 7 }
      ]
    },
    { 
      title: "Friday", 
      content: [
        { name: "Box Jumps", sets: 3, reps: 10, rpe: 6 },
        { name: "Lunges", sets: 4, reps: 12, rpe: 7 }
      ]
    }
  ],
  "9": [
    { 
      title: "Monday", 
      content: [
        { name: "Chest Press", sets: 3, reps: 12, rpe: 7 },
        { name: "Triceps Pushdowns", sets: 4, reps: 10, rpe: 8 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Hack Squats", sets: 4, reps: 10, rpe: 8 },
        { name: "Jump Squats", sets: 3, reps: 12, rpe: 7 }
      ]
    },
    { 
      title: "Friday", 
      content: [
        { name: "Hack Squats", sets: 4, reps: 10, rpe: 8 },
        { name: "Jump Squats", sets: 3, reps: 12, rpe: 7 }
      ]
    }
  ]
});

const filteredOptions3 = computed(() => {
  return items.value[selectedOption2.value] || [];
});
const activeIndex = ref(null);

const toggle = (index) => {
  activeIndex.value = activeIndex.value === index ? null : index;
};


  </script>
  