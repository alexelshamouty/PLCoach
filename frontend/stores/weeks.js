import { defineStore } from "pinia";

export const useWeeksStore = defineStore('weeks', {
  state: () => ({
    weeks: [
      { id: 1, block_id: 101, label: "Week 1" },
      { id: 2, block_id: 101, label: "Week 2" },
      { id: 3, block_id: 101, label: "Week 3" },
      { id: 4, block_id: 102, label: "Week 1" },
      { id: 5, block_id: 102, label: "Week 2" },
      { id: 6, block_id: 102, label: "Week 3" },
      { id: 7, block_id: 103, label: "Week 1" },
      { id: 8, block_id: 103, label: "Week 2" },
      { id: 9, block_id: 103, label: "Week 3" },
      { id: 10, block_id: 104, label: "Week 1" },
      { id: 11, block_id: 104, label: "Week 2" },
      { id: 12, block_id: 104, label: "Week 3" },
      { id: 13, block_id: 105, label: "Week 1" },
      { id: 14, block_id: 105, label: "Week 2" },
      { id: 15, block_id: 105, label: "Week 3" },
      { id: 16, block_id: 106, label: "Week 1" },
      { id: 17, block_id: 106, label: "Week 2" },
      { id: 18, block_id: 106, label: "Week 3" },
      { id: 19, block_id: 107, label: "Week 1" },
      { id: 20, block_id: 107, label: "Week 2" },
      { id: 21, block_id: 107, label: "Week 3" },
      { id: 22, block_id: 108, label: "Week 1" },
      { id: 23, block_id: 108, label: "Week 2" },
      { id: 24, block_id: 108, label: "Week 3" }
    ]
  }),
  actions: {
    addWeek(block_id, label) {
      const newId = Math.max(...this.weeks.map(week => week.id)) + 1;
      this.weeks.push({ id: newId, block_id, label });
    },
    getWeeksByBlockId(block_id) {
      console.log("getWeeksByBlockId", block_id);
      console.log(this.weeks.filter(week => week.block_id === block_id));
      return this.weeks.filter(week => week.block_id === block_id);
    }
  }
});
