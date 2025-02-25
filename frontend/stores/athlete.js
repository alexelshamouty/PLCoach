import { defineStore } from 'pinia';
import { useApi } from '~/composables/useApi';

export const useAthleteStore = defineStore('athlete', {
  state: () => ({
    athletes: [],
    currentAthlete: null,  // Add this new state property
    loading: false,
    error: null
  }),

  actions: {
    async fetchAthletes() {
      const { authenticatedFetch } = useApi();
      this.loading = true;
      
      try {
        const response = await authenticatedFetch('https://c1yi9fd6kc.execute-api.eu-north-1.amazonaws.com/dev/users');
        if (!response.ok) throw new Error('Failed to fetch athletes');
        
        const responseData = await response.json();
        // Parse the stringified body
        const users = JSON.parse(responseData.body);
        
        this.athletes = users.map(user => ({
          Userid: user.Userid,
          Name: user.Name,
          Email: user.Email,
          Gender: user.Gender,
          Weight: parseInt(user.Weight),
          preferredUsername: user.Preferred_username,
          photoUrl: user.photoUrl || false,
          program: "N/A",
          blocks: []
        }));
      } catch (error) {
        this.error = error.message;
        console.error('Error fetching athletes:', error);
      } finally {
        this.loading = false;
      }
    },

    async fetchAthlete(userId) {
      const { authenticatedFetch } = useApi();
      this.loading = true;
      
      try {
        const response = await authenticatedFetch(`https://6yztzyjul9.execute-api.eu-north-1.amazonaws.com/dev/getUser?userId=${userId}`);
        if (!response.ok) throw new Error('Failed to fetch athlete');
        
        const responseData = await response.json();
        const userData = JSON.parse(responseData.body);
        console.log(userData)
        console.log("sfasfas")
        if (!userData) throw new Error('No user data found');

        // Format the user data
        this.currentAthlete = {
          Userid: userData[0].Userid,
          Name: userData[0].Name,
          Email: userData[0].Email,
          Gender: userData[0].Gender,
          Weight: parseInt(userData[0].Weight),
          preferredUsername: userData[0].Preferred_username,
          photoUrl: userData[0].photoUrl || false,
          program: "N/A",
          blocks: []
        };

        return this.currentAthlete;
      } catch (error) {
        this.error = error.message;
        console.error('Error fetching athlete:', error);
        return null;
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