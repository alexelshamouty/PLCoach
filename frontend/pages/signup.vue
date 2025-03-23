<template>
  <div v-if="loading" class="flex items-center justify-center min-h-screen bg-gray-900">
    <div class="w-16 h-16 border-4 border-gray-300 border-t-yellow-400 rounded-full animate-spin"></div>
  </div>
  <div v-else class="flex flex-col items-center min-h-screen bg-gray-900 text-white p-4">
    <h2 class="text-2xl font-bold mb-8">{{ showVerification ? 'Verify Email' : 'Sign Up' }}</h2>
    
    <!-- Signup Form -->
    <form v-if="!showVerification" @submit.prevent="handleSignup" class="w-full max-w-md space-y-4">
      <div class="space-y-4">
        <input 
          v-model="form.name" 
          type="text" 
          placeholder="Full Name" 
          class="w-full p-3 text-black rounded-md text-lg"
          required
        />
        
        <input 
          v-model="form.preferredName" 
          type="text" 
          placeholder="Preferred Name" 
          class="w-full p-3 text-black rounded-md text-lg"
          required
        />
        
        <select 
          v-model="form.gender" 
          class="w-full p-3 text-black rounded-md text-lg"
          required
        >
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
        
        <input 
          v-model="form.weight" 
          type="number" 
          placeholder="Weight (kg)" 
          class="w-full p-3 text-black rounded-md text-lg"
          required
        />
        
        <input 
          v-model="form.email" 
          type="email" 
          placeholder="Email" 
          class="w-full p-3 text-black rounded-md text-lg"
          required
        />
        
        <div class="space-y-2">
          <input 
            v-model="form.password" 
            type="password" 
            placeholder="Password" 
            class="w-full p-3 text-black rounded-md text-lg"
            @input="validatePasswords"
            required
          />
          
          <input 
            v-model="form.confirmPassword" 
            type="password" 
            placeholder="Confirm Password" 
            class="w-full p-3 text-black rounded-md text-lg"
            @input="validatePasswords"
            required
          />
          
          <p v-if="passwordError" class="text-red-500 text-sm mt-1">
            {{ passwordError }}
          </p>
        </div>
      </div>

      <button 
        type="submit" 
        class="w-full bg-yellow-400 text-black px-4 py-2 rounded hover:bg-yellow-500 transition"
      >
        Sign Up
      </button>

      <div class="text-center mt-4">
        <NuxtLink to="/login" class="text-yellow-400 hover:text-yellow-300">
          Already have an account? Login
        </NuxtLink>
      </div>
    </form>

    <!-- Verification Form -->
    <form v-else @submit.prevent="handleVerification" class="w-full max-w-md space-y-4">
      <p class="text-center text-gray-400 mb-4">
        Please check your email for the verification code
      </p>
      
      <input 
        v-model="verificationCode" 
        type="text" 
        placeholder="Verification Code" 
        class="w-full p-3 text-black rounded-md text-lg"
        required
      />

      <button 
        type="submit" 
        class="w-full bg-yellow-400 text-black px-4 py-2 rounded hover:bg-yellow-500 transition"
      >
        Verify Email
      </button>
    </form>

    <p v-if="error" class="mt-4 text-red-500">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { signUp, confirmSignUp, signIn } from 'aws-amplify/auth';
import { useAuthStore } from '~/stores/auth';

const router = useRouter();
const authStore = useAuthStore();
const loading = ref(false);
const error = ref('');
const showVerification = ref(false);
const verificationCode = ref('');
const passwordError = ref('');

const form = reactive({
  name: '',
  preferredName: '',
  gender: '',
  weight: '',
  email: '',
  password: '',
  confirmPassword: ''
});

onMounted(async () => {
  // Redirect to index page if user is already authenticated
  try {
    await authStore.fetchUser();
    if (authStore.user) {
      router.push('/');
    }
  } catch (err) {
    console.error('Auth check error:', err);
  }
});

function validatePasswords() {
  if (form.password && form.confirmPassword) {
    if (form.password !== form.confirmPassword) {
      passwordError.value = 'Passwords do not match';
    } else {
      passwordError.value = '';
    }
  } else {
    passwordError.value = '';
  }
}

async function handleSignup() {
  loading.value = true;
  error.value = '';

  if (form.password !== form.confirmPassword) {
    error.value = 'Passwords do not match';
    passwordError.value = 'Passwords do not match';
    loading.value = false;
    return;
  }

  try {
    await signUp({
      username: form.email,
      password: form.password,
      options: {
        userAttributes: {
          name: form.name,
          preferred_username: form.preferredName,
          gender: form.gender,
          'custom:weight': form.weight.toString()
        }
      }
    });
    showVerification.value = true;
  } catch (err) {
    error.value = err.message || 'Signup failed';
  } finally {
    loading.value = false;
  }
}

async function handleVerification() {
  loading.value = true;
  error.value = '';

  try {
    await confirmSignUp({
      username: form.email,
      confirmationCode: verificationCode.value
    });
    
    // Sign in the user after verification
    await signIn({
      username: form.email,
      password: form.password,
    });
    
    // Fetch user data into store
    await authStore.fetchUser();
    
    // Redirect based on user type
    if (authStore.admin) {
      router.push('/admin/adminDashboard');
    } else if (authStore.user) {
      router.push(`/users/profile/${authStore.user.userId}`);
    } else {
      router.push('/login');
    }
  } catch (err) {
    error.value = err.message || 'Verification failed';
  } finally {
    loading.value = false;
  }
}
</script>
