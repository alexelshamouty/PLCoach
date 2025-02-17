<template>
    <div class="bear-container relative flex justify-center">
      <svg
        class="w-32 h-32"
        viewBox="0 0 200 200"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <!-- Bear Head -->
        <circle cx="100" cy="100" r="80" fill="#6B4226" />
  
        <!-- Ears -->
        <circle cx="40" cy="50" r="25" fill="#6B4226" />
        <circle cx="160" cy="50" r="25" fill="#6B4226" />
  
        <!-- Eyes (Open) - Move dynamically -->
        <circle
          v-if="!isTypingPassword"
          :cx="75 + eyeOffsetX"
          :cy="90 + eyeOffsetY"
          r="8"
          fill="black"
        />
        <circle
          v-if="!isTypingPassword"
          :cx="125 + eyeOffsetX"
          :cy="90 + eyeOffsetY"
          r="8"
          fill="black"
        />
  
        <!-- Eyes (Closed) -->
        <line
          v-if="isTypingPassword"
          :x1="65 + eyeOffsetX"
          :y1="90 + eyeOffsetY"
          :x2="85 + eyeOffsetX"
          :y2="90 + eyeOffsetY"
          stroke="black"
          stroke-width="4"
          stroke-linecap="round"
        />
        <line
          v-if="isTypingPassword"
          :x1="115 + eyeOffsetX"
          :y1="90 + eyeOffsetY"
          :x2="135 + eyeOffsetX"
          :y2="90 + eyeOffsetY"
          stroke="black"
          stroke-width="4"
          stroke-linecap="round"
        />
  
        <!-- Nose -->
        <ellipse cx="100" cy="120" rx="15" ry="10" fill="black" />
      </svg>
    </div>
  </template>
  
  <script setup>
  import { ref, watch } from "vue";
  
  const props = defineProps(["email", "isTypingPassword"]);
  
  const eyeOffsetX = ref(-10); // Start eyes looking left
  const eyeOffsetY = ref(5);  // Start eyes looking down
  
  watch(
    () => props.email,
    (newVal) => {
      const length = newVal.length;
  
      // Eyes gradually move right (max at 10)
      eyeOffsetX.value = Math.min(-10 + length * 2, 10);
  
      // Eyes gradually move up (max at 0)
      eyeOffsetY.value = Math.max(5 - length * 0.5, 0);
    }
  );
  </script>
  
  <style scoped>
  .bear-container {
    position: relative;
  }
  </style>
  