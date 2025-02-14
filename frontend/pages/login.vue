<template>
  <div v-if="loading" class="flex items-center justify-center min-h-screen bg-gray-900">
    <div class="w-16 h-16 border-4 border-gray-300 border-t-yellow-400 rounded-full animate-spin"></div>
  </div>
  <div v-else-if="!user?.username && !newUser">
    <div class="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h2 class="text-2xl font-bold mb-4">Login</h2>
      
      <input v-model="email" type="email" placeholder="Email" class="p-2 mb-2 text-black rounded">
      <input v-model="password" type="password" placeholder="Password" class="p-2 mb-2 text-black rounded">
      
      <button @click="login" class="bg-yellow-400 px-4 py-2 rounded">Login</button>
  
      <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
    </div>
  </div>
  <div v-if="newUser">
    <div class="bg-gray-900 min-h-screen text-white flex items-center justify-center">
      <div class="w-full max-w-md p-6 rounded-lg shadow-md">
          <h2 class="text-2xl font-semibold text-center mb-4">Create your new profile</h2>
          <Form @submit="confirmNewUser" :validation-schema="schema" class="space-y-4">

            <div>
              <label for="newpassword" class="block text-sm font-medium mb-1">New Password:</label>
              <Field id="newpassword" name="newpassword" type="password" v-model="formData.newpassword"
                    class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500" />
              <ErrorMessage name="newpassword" class="text-red-400 text-sm mt-1" />
            </div>

            <!-- Confirm Password Field -->
            <div>
              <label for="confirmPassword" class="block text-sm font-medium mb-1">Confirm Password:</label>
              <Field id="confirmPassword" name="confirmPassword" type="password" v-model="formData.confirmPassword"
                    class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500" />
              <ErrorMessage name="confirmPassword" class="text-red-400 text-sm mt-1" />
            </div>
          <div>
              <label for="weight" class="block text-sm font-medium mb-1">Weight:</label>
            <Field id="weight" name="weight" v-model="formData.weight"
                   class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
            <ErrorMessage name="weight" class="text-red-400 text-sm mt-1" />
          </div>

          <button class="bg-red-400 text-black px-4 py-2 rounded" type="submit">
              Confirm Profile
          </button>
          <div v-if="messageOpen">
            <div @click="toggleMessage()" v-if="success" class="mt-6 p-4 bg-yellow-500 text-black text-center rounded-lg shadow-lg animate-bounce">
              <p class="text-lg font-semibold">{{ message }}</p>
            </div>
          </div>
        <div v-if="messageOpen" @click="toggleMessage()">
            <div v-if="success" class="mt-4 text-center">
            <NuxtLink to="/" class="bg-yellow-400 text-black px-6 py-2 rounded-md font-semibold shadow-md hover:bg-yellow-300 transition">
                Go Home
            </NuxtLink>
            </div>
        </div>
        <div v-if="error" class="mt-6 p-4 bg-red-500 text-black text-center rounded-lg shadow-lg">
              <p class="text-lg font-semibold">{{ error }}</p>
          </div>
      </Form>
      </div>
    </div>
  </div>
  </template>
  
  <script setup>
  import { watchEffect, ref } from 'vue';
  import { useRouter } from 'vue-router';
  import {  signIn  } from 'aws-amplify/auth';
  import { useAuthStore } from './stores/auth';
  import { useAthleteStore } from '~/stores/athlete';
  import { onMounted } from 'vue';
  import { storeToRefs } from 'pinia';
  import { Field, Form, ErrorMessage } from 'vee-validate';
  import *  as yup from 'yup';

  const authStore = useAuthStore();
  
  const { user,loading } = storeToRefs(authStore);
  const email = ref('');
  const password = ref('');
  const error = ref('');
  const newUser = ref(false);
  const formData = ref({newpassword: "", confirmPassword: "", weight:""});
  const messageOpen = ref(false)
  const success = ref(false)
  const message = ref("")
  let userSession = null;
  const schema = computed(() => yup.object({
    name: yup.string().required("Name is required"),
    email: yup.string().email("Invalid Email Format").required("Email is required"),
    gender: yup.string().required("Gender is required"),
    weight: yup.number().required("Weight is required"),
    newpassword: yup.string().required("New Password is required"),
    confirmPassword: yup
    .string()
    .oneOf([yup.ref("newpassword"), null], "Passwords must match")
    .required("Confirm Password is required"),
}));

  const login = async () => {
    try {
     const userLogIn = await signIn({
        username: email.value, 
        password: password.value,
    })
    if(userLogIn?.nextStep?.signInStep == "CONFIRM_SIGN_IN_WITH_NEW_PASSWORD_REQUIRED"){
      newUser.value = true;
      userSession = userLogIn;
    }else{
      navigateTo("/")
    }
    } catch (err) {
      error.value = err.message || "Login failed.";
      console.log(error)
    }
  };

  async function confirmNewUser(values){
    if(!userSession){
      alert("No user session found. Please try to login again");
      return
    }
    try{
      const updatedUser = await confirmSignIn(userSession, values.newpassword);
      console.log("Ok I got everything now")
      console.log(updatedUser)
    }catch(error){
      message.value=error;
      error.value=true;
    }
    
  }  
  function toggleMessage(){
    messageOpen.value = !messageOpen.value
  }


  onMounted(() => {
    authStore.fetchUser();
  });

  watchEffect(() => {
    if (user.value?.username) {
      console.log(user.value)
      console.log(user.value.profile)
      navigateTo('/');
    }
  });
  </script>  