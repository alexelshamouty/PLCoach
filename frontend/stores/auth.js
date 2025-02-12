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
      } catch (error) {
        this.error = error;
      }
    },
    async logout() {
      try {
        await signOut();
        this.user = null;
      } catch (error) {
        this.error = error;
      }
    },
  },
});
