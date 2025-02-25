import { defineStore } from 'pinia';
import { useApi } from '~/composables/useApi';

export const useAthleteStore = defineStore('athlete', {
  state: () => ({
    athletes: [],
    loading: false,
    error: null
  }),

  actions: {
    async fetchAthletes() {
      const { authenticatedFetch } = useApi();
      this.loading = true;
      
      try {
        const response = await authenticatedFetch('/users');
        if (!response.ok) throw new Error('Failed to fetch athletes');
        
        const data = await response.json();
        this.athletes = data;
      } catch (error) {
        this.error = error.message;
        console.error('Error fetching athletes:', error);
      } finally {
        this.loading = false;
      }
    },
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