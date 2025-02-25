<template>
  <div v-if="loading" class="flex items-center justify-center min-h-screen bg-gray-900">
    <div class="w-16 h-16 border-4 border-gray-300 border-t-yellow-400 rounded-full animate-spin"></div>
  </div>
  <div v-else class="flex flex-col items-center min-h-screen bg-gray-900 text-white p-4">
    <h2 class="text-2xl font-bold mb-8">Login</h2>
    
    <!-- Direct Login Form -->
    <form @submit.prevent="handleDirectLogin" class="w-full max-w-md space-y-4 mb-8">
      <div>
        <input 
          v-model="email" 
          type="email" 
          placeholder="Email" 
          class="w-full p-3 mb-3 text-black rounded-md text-lg"
          required
        />
      </div>
      <div>
        <input 
          v-model="password" 
          type="password" 
          placeholder="Password" 
          class="w-full p-3 mb-3 text-black rounded-md text-lg"
          required
        />
      </div>
      <button 
        type="submit" 
        class="w-full bg-yellow-400 text-black px-4 py-2 rounded hover:bg-yellow-500 transition"
      >
        Login
      </button>
    </form>

    <!-- Divider -->
    <div class="w-full max-w-md flex items-center justify-center mb-8">
      <div class="border-t border-gray-600 flex-grow"></div>
      <span class="px-4 text-gray-400">or</span>
      <div class="border-t border-gray-600 flex-grow"></div>
    </div>

    <!-- Cognito Hosted UI Button -->
    <button 
      @click="handleCognitoLogin" 
      class="w-full max-w-md bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
    >
      Continue with Cognito
    </button>

    <p v-if="error" class="mt-4 text-red-500">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { signIn } from 'aws-amplify/auth';
import { useAuthStore } from '~/stores/auth';

const router = useRouter();
const authStore = useAuthStore();
const email = ref('');
const password = ref('');
const error = ref('');
const loading = ref(false);

onMounted(async () => {
  // Check if user is already authenticated
  try {
    await authStore.fetchUser();
    if (authStore.user) {
      handleSuccessfulLogin();
    }
  } catch (err) {
    console.error('Auth check error:', err);
  }
});

async function handleDirectLogin() {
  loading.value = true;
  error.value = '';
  
  try {
    await signIn({
      username: email.value,
      password: password.value,
    });
    await authStore.fetchUser();
    handleSuccessfulLogin();
  } catch (err) {
    error.value = err.message || 'Login failed';
    loading.value = false;
  }
}

function handleCognitoLogin() {
  // Redirect to Cognito hosted UI
  window.location.href = process.env.NUXT_PUBLIC_COGNITO_HOSTED_UI_URL;
}

function handleSuccessfulLogin() {
  if (authStore.admin) {
    router.push('/admin/adminDashboard');
  } else if (authStore.user) {
    router.push(`/users/profile/${authStore.user.userId}`);
  }
}
</script>