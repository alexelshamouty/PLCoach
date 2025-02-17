<template>
<div class="bg-gray-900 min-h-screen text-white flex justify-center">
    <div class="w-full max-w-lg p-6 rounded-lg shadow-md">        
        <h2 class="text-2xl font-semibold text-center mb-4">Athlete {{ username }} Program Managment</h2>
        <div class="bg-gray-700 p-4 max-w-lg rounded-lg flex space-x-4">
            <!-- First Dropdown -->
            <select v-model="selectedOption1" class="w-1/2  p-2 bg-gray-600 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500">
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
        <div class="mt-4 bg-gray-800 p-4 w-full max-w-md rounded-lg">
        <h3 class="text-lg font-semibold">Add a New Week</h3>
        <input v-model="newWeekTitle" placeholder="Enter week number (e.g., Week 4)" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
        <button @click="addWeek" class="w-full mt-2 p-2 bg-purple-600 rounded-lg hover:bg-purple-700">
          Add Week
        </button>
      </div>
        <!-- Add day -->
        <div class="mt-4 bg-gray-800 p-4 w-full max-w-md rounded-lg">
        <h3 class="text-lg font-semibold">Add a New Day</h3>
        <input v-model="newDayTitle" placeholder="Enter day (e.g., Wednesday)" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none focus:ring-2 focus:ring-blue-500" />
        <button @click="addDay" class="w-full mt-2 p-2 bg-blue-600 rounded-lg hover:bg-blue-700">
          Add Day
        </button>
        </div>
    <div class="bg-gray-900 text-white max-w-lg p-6 w-full max-w-md rounded-lg shadow-md">
        <div v-for="(item, index) in filteredOptions3" :key="index" class="border-b border-gray-600">
        <button @click="toggle(index)" class="w-full flex justify-between items-center p-4 focus:outline-none">
            <span class="font-semibold">{{ item.title }}</span>
            <span :class="{'rotate-180': activeIndex === index}" class="transition-transform duration-300">
            ⬇️
            </span>
        </button>
        <div v-if="messageOpen">
            <div @click="toggleMessage()" v-if="allSets" class="mt-6 p-4 bg-yellow-500 text-black text-center rounded-lg shadow-lg animate-bounce">
              <p class="text-lg font-semibold">{{ allSets }}</p>
            </div>
          </div>
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
                <button @click="countSetsPerWeek(exercise.label)" class="bg-red-400 text-black px-4 py-2 rounded-full hover:bg-red-500 transition">
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
        <!-- Add training -->
        <div class="mt-4 bg-gray-800 p-4 rounded-lg">
              <h3 class="text-lg font-semibold">Add Exercise</h3>
              <input v-model="newExerciseName" placeholder="Exercise Name" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none" />
              <input v-model="newExerciseLabel" placeholder="Exercise Label" class="w-full p-2 mt-2 bg-gray-700 text-white rounded-lg outline-none" />
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
  const messageOpen = ref(false);
  const allSets = ref(0);
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
        { name: "Bench Press", label:"chest", sets: 4, reps: 10, comments: " Great work", rpe: 8 },
        { name: "Pull-ups", label:"pull-ups", sets: 3, reps: 12, comments: " Great work", rpe: 7 },
        { name: "Squats", label:"squats", sets: 4, reps: 8, comments: " Great work", rpe: 9 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Squat", label:"squats", sets: 5, reps: 10, comments: " Great work", rpe: 8 },
        { name: "Lunges", label:"lunges", sets: 3, reps: 15, comments: " Great work", rpe: 7 },
        { name: "Leg Press", label:"legs", sets: 4, reps: 12, comments: " Great work", rpe: 9 }
      ]
    }
  ],
  "2": [
    { 
      title: "Monday", 
      content: [
        { name: "Deadlift", label:"deadlift", sets: 4, reps: 6, comments: " Great work", rpe: 9 },
        { name: "Good Mornings", label:"hamstrings", sets: 3, reps: 12, comments: " Great work", rpe: 8 },
        { name: "Hamstring Curls", label:"hamstrings", sets: 4, reps: 15, comments: " Great work", rpe: 7 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Squat", label:"chest", sets: 5, reps: 8, comments: " Great work", rpe: 9 },
        { name: "Leg Extensions", label:"legs", sets: 3, reps: 12, comments: " Great work", rpe: 7 }
      ]
    }
  ],
  "3": [
    { 
      title: "Monday", 
      content: [
        { name: "Bench Press", label:"chest",  sets: 4, reps: 10, comments: " Great work", rpe: 8 },
        { name: "Dips", label:"chest", sets: 3, reps: 12, comments: " Great work", rpe: 7 },
        { name: "Push-ups", label:"back", sets: 4, reps: 15, comments: " Great work", rpe: 6 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Squat", label:"legs", sets: 4, reps: 8, comments: " Great work", rpe: 9 },
        { name: "Step-ups", label:"legs",  sets: 3, reps: 10, comments: " Great work", rpe: 7 }
      ]
    },
    { 
      title: "Wednesday", 
      content: [
        { name: "Deadlift", label:"deadlift", sets: 4, reps: 6, comments: " Great work", rpe: 10 },
        { name: "Pull-ups", label:"back", sets: 3, reps: 12, comments: " Great work", rpe: 7 }
      ]
    }
  ],
  "4": [
    { 
      title: "Monday", 
      content: [
        { name: "Dumbbell Press", label:"chest", sets: 3, reps: 12, comments: " Great work", rpe: 8 },
        { name: "Incline Press", label:"chest", sets: 3, reps: 10, comments: " Great work", rpe: 7 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Goblet Squats", label:"legs", sets: 4, reps: 12, comments: " Great work", rpe: 8 },
        { name: "Lunges", label:"legs", sets: 3, reps: 15, comments: " Great work", rpe: 7 }
      ]
    }
  ],
  "5": [
    { 
      title: "Monday", 
      content: [
        { name: "Bench Press", label:"chest", sets: 4, reps: 8, comments: " Great work", rpe: 9 },
        { name: "Triceps Dips", label:"chest", sets: 3, reps: 12, comments: " Great work", rpe: 7 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Squat",  label:"legs", sets: 4, reps: 10, comments: " Great work", rpe: 8 },
        { name: "Lunges", label:"legs",  sets: 3, reps: 15, comments: " Great work", rpe: 6 }
      ]
    }
  ],
  "6": [
    { 
      title: "Monday", 
      content: [
        { name: "Dips", label:"chest", sets: 3, reps: 12, comments: " Great work", rpe: 8 },
        { name: "Close-grip Bench Press", label:"chest",  sets: 4, reps: 10, comments: " Great work", rpe: 9 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Front Squats",label:"legs",  sets: 4, reps: 8, comments: " Great work", rpe: 8 },
        { name: "Step-ups",  label:"legs", sets: 3, reps: 12, comments: " Great work", rpe: 7 }
      ]
    },
    { 
      title: "Friday", 
      content: [
        { name: "Front Squats", label:"legs", sets: 4, reps: 8, comments: " Great work", rpe: 8 },
        { name: "Step-ups", label:"legs", sets: 3, reps: 12, comments: " Great work", rpe: 7 }
      ]
    }
  ],
  "7": [
    { 
      title: "Monday", 
      content: [
        { name: "Flat Bench Press",  label:"chest", sets: 3, reps: 10, comments: " Great work", rpe: 7 },
        { name: "Incline Bench Press", label:"chest",  sets: 4, reps: 8, comments: " Great work", rpe: 9 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Leg Press", label:"legs", sets: 4, reps: 12, comments: " Great work", rpe: 8 },
        { name: "Bulgarian Split Squat", label:"legs",  sets: 3, reps: 10, comments: " Great work", rpe: 7 }
      ]
    }
  ],
  "8": [
    { 
      title: "Monday", 
      content: [
        { name: "Barbell Bench Press", label:"chest",  sets: 4, reps: 8, comments: " Great work", rpe: 9 },
        { name: "Dips", sets: 3,  label:"chest", reps: 12, comments: " Great work", rpe: 7 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Box Jumps", label:"legs",  sets: 3, reps: 10, comments: " Great work", rpe: 6 },
        { name: "Lunges", label:"legs", sets: 4, reps: 12, comments: " Great work", rpe: 7 }
      ]
    },
    { 
      title: "Friday", 
      content: [
        { name: "Box Jumps", label:"legs", sets: 3, reps: 10, comments: " Great work", rpe: 6 },
        { name: "Lunges", label:"legs", sets: 4, reps: 12, comments: " Great work", rpe: 7 }
      ]
    }
  ],
  "9": [
    { 
      title: "Monday", 
      content: [
        { name: "Chest Press", label:"chest",  sets: 3, reps: 12, comments: " Great work", rpe: 7 },
        { name: "Triceps Pushdowns", label:"chest",  sets: 4, reps: 10, comments: " Great work", rpe: 8 }
      ]
    },
    { 
      title: "Tuesday", 
      content: [
        { name: "Hack Squats", label:"legs",  sets: 4, reps: 10, comments: " Great work", rpe: 8 },
        { name: "Jump Squats", label:"legs",  sets: 3, reps: 12, comments: " Great work", rpe: 7 }
      ]
    },
    { 
      title: "Friday", 
      content: [
        { name: "Hack Squats", label:"legs",  sets: 4, reps: 10, comments: " Great work", rpe: 8 },
        { name: "Jump Squats", label:"legs", sets: 3, reps: 12, comments: " Great work", rpe: 7 }
      ]
    }
  ]
});

function countSetsPerWeek(label){
  console.log("I am gonna count all " + label + " sets per week")
  console.log("Week is in " + selectedOption1.value + " week " + selectedOption2.value)
  console.log("And here are the details of this week")
  console.log(items.value[selectedOption2.value])
  const week = items.value[selectedOption2.value]
  allSets.value = 0;
  week.forEach((day) => {
    day.content.forEach((exercise) => {
      if(exercise.label === label){
        allSets.value += exercise.sets
        messageOpen.value = true;
      }
    })
  })
}

function toggleMessage(){
  messageOpen.value = !messageOpen.value;
}
const filteredOptions3 = computed(() => {
  return items.value[selectedOption2.value] || [];
});
const activeIndex = ref(null);

const toggle = (index) => {
  activeIndex.value = activeIndex.value === index ? null : index;
  messageOpen.value = false;
};


  </script>
  