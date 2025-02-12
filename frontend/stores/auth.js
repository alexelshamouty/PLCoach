import { defineStore } from "pinia";
import { getCurrentUser, signOut } from "@aws-amplify/auth";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: null,
    error: null,
    loading: true,
  }),
  actions: {
    async fetchUser() {
      try {
        const user = await getCurrentUser();
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
