import { defineStore } from "pinia";

export const useBlocksStore = defineStore('blocks', {
  state: () => ({
    blocks: [
      { value: "Block 1", label: "Block 1" },
      { value: "Block 2", label: "Block 2" },
      { value: "Block 3", label: "Block 3" },
    ]
  })
});
