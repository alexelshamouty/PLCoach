<template>
    <div class="bg-gray-900 min-h-screen text-white flex items-center justify-center">
      <div class="w-full max-w-md p-6 rounded-lg shadow-md">
          <h2 class="text-2xl font-semibold text-center mb-4">Delete Athlete</h2>
          <Form @submit="delSubmit" :validation-schema="schema" class="space-y-4">
  
          <div>
              <label for="name" class="block text-sm font-medium mb-1">Username:</label>
            <Field id="email" name="email" v-model="formData.email"
                   class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
            <ErrorMessage name="email" class="text-red-400 text-sm mt-1" />
          </div>

          <button class="bg-red-400 text-black px-4 py-2 rounded" type="submit">
              Delete Athelete
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
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { useAuthStore } from '~/stores/auth';
  import { Field, Form, ErrorMessage } from 'vee-validate';
  import *  as yup from 'yup';
  
  definePageMeta({
    middleware: ['auth-admin'],}
  );
  
  const authStore = useAuthStore();
  const {user, groups, admin, loading} = storeToRefs(authStore);
  const formData = ref({email:""});
  const error = ref(false)
  const success = ref(false)
  const message = ref("")
  const messageOpen = ref(false)

  import {deleteAthletes} from '~/composables/deleteAthlete';

  const schema = computed(() => yup.object({
      email: yup.string().email("Invalid Email Format").required("Email is required"),
  }));
  
  function toggleMessage(){
    messageOpen.value = !messageOpen.value
  }

  async function delSubmit(values){
    message.value="";
    try{
        console.log("Am gonna call the API now")
        console.log("Deleting user " + values?.email)
        message.value = "User " + values?.email + " has been deleted!";
        success.value=true
        messageOpen.value = true
    }catch(error){
        error.value = true
        message.value=error
        console.log("Something happened")
    }
  }
  </script>