import { defineStore } from "pinia";

export const useAthleteStore = defineStore("athletes", {
  state: () => ({
    athletes:[
        { 
          id: 1, 
          username: "johndoe", 
          email: "john@example.com", 
          weight: 75, 
          gender: "Male", 
          program: "Strength Training",
          blocks: [
            { id: 101, label: "Block 1" },
            { id: 102, label: "Block 2" }
          ]
        },
        { 
          id: 2, 
          username: "janedoe", 
          email: "jane@example.com", 
          weight: 60, 
          gender: "Female", 
          program: "Cardio",
          blocks: [
            { id: 103, label: "Block 1" },
            { id: 104, label: "Block 3" }
          ]
        },
        { 
          id: 3, 
          username: "mike99", 
          email: "mike@example.com", 
          weight: 85, 
          gender: "Male", 
          program: "CrossFit",
          blocks: [
            { id: 105, label: "Block 2" },
            { id: 106, label: "Block 3" }
          ]
        },
        { 
          id: 4, 
          username: "sara_k", 
          email: "sara@example.com", 
          weight: 65, 
          gender: "Female", 
          program: "Yoga",
          blocks: [
            { id: 107, label: "Block 1" },
            { id: 108, label: "Block 2" }
          ]
        }    
    ]
  }),
  actions: {
    deleteAthlete(id){
        this.athletes = this.athletes.filter(athlete => athlete.id !== id);
    },
    addAthlete(name,email,gender){
      const randomId = Math.floor(Math.random() * 10000);
      const weight = Math.floor(Math.random() * (150 - 50 + 1)) + 50;
      this.athletes.push({
        id: randomId,
        username: name,
        email: email,
        gender: gender,
        weight: weight,
        program: "N/A",
        blocks: []
      }) 
    },
    addBlockToAthlete(athleteId, block) {
      const athlete = this.athletes.find(a => a.id === athleteId);
      if (athlete) {
        athlete.blocks.push(block);
      } else {
        console.error("Athlete not found");
      }
    }
  }
});