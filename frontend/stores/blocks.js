import { defineStore } from "pinia";

export const useBlocksStore = defineStore('blocks', {
  state: () => ({
    blocks: [
      { id: 101, value: "Block 1", label: "Block 1" },
      { id: 102, value: "Block 2", label: "Block 2" },
      { id: 103, value: "Block 1", label: "Block 1" },
      { id: 104, value: "Block 3", label: "Block 3" },
      { id: 105, value: "Block 2", label: "Block 2" },
      { id: 106, value: "Block 3", label: "Block 3" },
      { id: 107, value: "Block 1", label: "Block 1" },
      { id: 108, value: "Block 2", label: "Block 2" }
    ]
  }),
  actions: {
    getBlocksByIds(ids) {
      return this.blocks.filter(block => ids.includes(block.id));
    },
    addBlock(value, label) {
      const newId = Math.max(...this.blocks.map(block => block.id)) + 1;
      this.blocks.push({ id: newId, value, label });
    }
  }
});
