import { defineStore } from "pinia";

export const useBlocksStore = defineStore('blocks', {
  state: () => ({
    blocks: [
      { id: 101, label: "Block 1" },
      { id: 102, label: "Block 2" },
      { id: 103, label: "Block 1" },
      { id: 104, label: "Block 3" },
      { id: 105, label: "Block 2" },
      { id: 106, label: "Block 3" },
      { id: 107, label: "Block 1" },
      { id: 108, label: "Block 2" }
    ]
  }),
  actions: {
    getBlocksByIds(ids) {
      return this.blocks.filter(block => ids.includes(block.id));
    },
    addBlock(label) {
      const newId = Math.max(...this.blocks.map(block => block.id)) + 1;
      this.blocks.push({ id: newId, label });
    }
  }
});
