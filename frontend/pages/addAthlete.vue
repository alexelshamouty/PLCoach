<template>
<div v-if="admin">
    <UForm :validate="validate" class="space-y-4" @submit="onSubmit">
    <UFormGroup label="Email" name="email">
      <UInput v-model="email" />
    </UFormGroup>

    <UFormGroup label="Name" name="name">
      <UInput v-model="password"/>
    </UFormGroup>

    <UButton type="submit">
      Submit
    </UButton>
  </UForm>
</div>
</template>

<script setup>
import { ref } from "vue"
import { useAuthStore } from '~/stores/auth';

const authStore = useAuthStore();
const {user, groups, admin, loading} = storeToRefs(authStore);

const email = ref("");
const message = ref("");
const signingUp = ref(false);

async function inviteUser(){
    signingUp.value = true;
    message.value = "";
    try{
        console.log("Am gonna call the API now")
    }catch(error){
        console.error("Error invting user:",error)
        message.value = "Error inviting user"
    }finally{
        signingUp.value = false
    }
}
</script>