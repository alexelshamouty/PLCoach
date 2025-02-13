import { defineStore } from "pinia";
import { getCurrentUser, fetchAuthSession, signOut } from "@aws-amplify/auth";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    admin: null,
    groups: [],
    error: null,
    loading: true,
  }),
  actions: {
    async fetchUser() {
      try {
        const user = await getCurrentUser();
        try{
          const session = await fetchAuthSession();
          const idToken = session.tokens?.idToken?.toString();
          if(idToken){
            const payload = JSON.parse(atob(idToken.split('.')[1]));
            this.groups = payload["cognito:groups"] || [];
            if(this.groups.includes('coaches')){
              this.admin = true;
            }
          }  
        }catch(error){
          console.log(error)
        }
        this.user = user;
        this.loading = false;
      } catch (error) {
        this.error = error;
        this.loading = true;
      } finally {
        this.loading = false;
      }
    },
    async logout() {
      try {
        await signOut();
        this.user = null;
        this.error = null;
        this.loading = true;
        localStorage.clear()
        sessionStorage.clear()
      } catch (error) {
        this.error = error;
      }
    },
  },
});
