import { defineStore } from "pinia";

export const useAthleteStore = defineStore("athletes", {
  state: () => ({
    athletes:[
        { id: 1, username: "johndoe", email: "john@example.com", weight: 75, gender: "Male", program: "Strength Training" },
        { id: 2, username: "janedoe", email: "jane@example.com", weight: 60, gender: "Female", program: "Cardio" },
        { id: 3, username: "mike99", email: "mike@example.com", weight: 85, gender: "Male", program: "CrossFit" },
        { id: 4, username: "sara_k", email: "sara@example.com", weight: 65, gender: "Female", program: "Yoga" }    
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
        program: "N/A"
      }) 
    }
  }
});
