<template>
  <div class="bg-gray-900 min-h-screen text-white flex items-center justify-center">
    <div class="w-full max-w-md p-6 rounded-lg shadow-md">
        <h2 class="text-2xl font-semibold text-center mb-4">Add Athlete</h2>
        <Form @submit="inviteUser" :validation-schema="schema" class="space-y-4">

        <div>
            <label for="name" class="block text-sm font-medium mb-1">Name:</label>
          <Field id="name" name="name" v-model="formData.name"
                 class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
          <ErrorMessage name="name" class="text-red-400 text-sm mt-1" />
        </div>

        <div>
          <label for="email" class="block text-sm font-medium mb-1">Email:</label>
          <Field id="email" name="email" v-model="formData.email"
                 class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
          <ErrorMessage name="email" class="text-red-400 text-sm mt-1" />
        </div>
        <div>
            <label for="gender" class="block text-sm font-medium mb-1">Gender:</label>
            <Field as="select" id="gender" name="gender" v-model="formData.gender"
                 class="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
            <option value="" disabled>Select Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Female">Other</option>
            </Field>
            <ErrorMessage name="gender" class="text-red-400 text-sm mt-1" />
        </div>
        <button class="bg-yellow-400 text-black px-4 py-2 rounded" type="submit">
            Add Athelete
        </button>
        <div v-if="success" class="mt-6 p-4 bg-green-500 text-black text-center rounded-lg shadow-lg animate-bounce">
            <p class="text-lg font-semibold">{{ message }}</p>
        </div>
      <div v-if="success" class="mt-4 text-center">
        <NuxtLink to="/" class="bg-yellow-400 text-black px-6 py-2 rounded-md font-semibold shadow-md hover:bg-yellow-300 transition">
          Go Home
        </NuxtLink>
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
const formData = ref({name: "", email:""});
const message = ref("");
const success = ref(false);
const error = ref(false);

const schema = computed(() => yup.object({
    name: yup.string().required("Name is required"),
    email: yup.string().email("Invalid Email Format").required("Email is required"),
    gender: yup.string().required("Gender is required"),
}));

async function inviteUser(values){
    message.value = "";
    try{
      console.log("NOTHING")
    }catch(error){
        console.error("Error invting user:",error)
        message.value = "Error inviting user"
        error.value = true;
    }
}
</script>