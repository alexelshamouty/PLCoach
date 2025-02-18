import { defineStore } from "pinia";

export const useLabelsStore = defineStore('labels', {
  state: () => ({
    labels: {
      "Calves": "#FF5733",
      "Quads": "#33FF57",
      "Hamstrings": "#3357FF",
      "Glutes": "#FF33A1",
      "Abs": "#FF8C33",
      "Biceps": "#8C33FF",
      "Triceps": "#33FFF5",
      "Shoulders": "#FF33D1",
      "Back": "#33FF8C",
      "Chest": "#FF3333",
      "Squat": "#33D1FF",
      "Bench": "#D1FF33",
      "Deadlift": "#FF5733",
      "Other": "#8CFF33"
    }
  }),
  getters: {
    getColorByLabel: (state) => (label) => {
      const lowerCaseLabel = label.toLowerCase();
      for (const key in state.labels) {
        if (key.toLowerCase() === lowerCaseLabel) {
          return state.labels[key];
        }
      }
      return null; // Return null if no matching label is found
    }
  }
});
