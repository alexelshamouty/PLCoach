import { defineStore } from "pinia";

export const useWeeksStore = defineStore('weeks', {
  state: () => ({
    weeks: {
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
    }
  })
});
