import { defineStore } from "pinia";
import { getCurrentUser, fetchAuthSession, signOut } from "@aws-amplify/auth";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    admin: null,
    gender: null,
    groups: [],
    error: null,
    loading: true,
  }),
  actions: {
    async fetchUser() {
      try {
        const user = await getCurrentUser();
        const session = await fetchAuthSession();
        console.log(user)
        if (session.tokens?.idToken) {
          const payload = JSON.parse(atob(session.tokens.idToken.toString().split('.')[1]));
          this.groups = payload["cognito:groups"] || [];
          this.admin = this.groups.includes('coaches');
          this.gender = payload.gender || 'other';
          console.log(payload)
          // Enhance user object with additional info from token
          this.user = {
            ...user,
            userId: payload.sub,
            email: payload.email,
            username: payload.name || payload.email
          };
        } else {
          this.user = user;
        }
        
        this.loading = false;
        return this.user;
      } catch (error) {
        this.error = error;
        this.user = null;
        this.admin = false;
        this.groups = [];
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
    setUser(userData) {
      this.user = userData;
      this.loading = false;
    }
  },
});
