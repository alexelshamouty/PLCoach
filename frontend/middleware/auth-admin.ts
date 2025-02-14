export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore();
    const { admin } = storeToRefs(authStore);
    if(!admin){
      console.log("Access to admin page detected but the user is not an admin");
      navigateTo('/');
    }
  });  