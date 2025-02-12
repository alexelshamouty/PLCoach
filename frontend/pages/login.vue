<template>
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h2 class="text-2xl font-bold mb-4">Login</h2>
      
      <input v-model="email" type="email" placeholder="Email" class="p-2 mb-2 text-black rounded">
      <input v-model="password" type="password" placeholder="Password" class="p-2 mb-2 text-black rounded">
      
      <button @click="login" class="bg-yellow-400 px-4 py-2 rounded">Login</button>
  
      <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import {  signIn  } from 'aws-amplify/auth'; 
  
  const email = ref('');
  const password = ref('');
  const error = ref('');
  const router = useRouter();
  
  const login = async () => {
    try {
      await signIn({
        username: email.value, 
        password: password.value,
    });
      router.push('/'); // Redirect after login
    } catch (err) {
      error.value = err.message || "Login failed.";
      console.log(error)
    }
  };
  </script>  