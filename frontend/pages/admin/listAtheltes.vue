<template>
  <div class="bg-gray-900 min-h-screen text-white flex flex-col items-center p-6">
    <LoadingOverlay :show="loading" />
    <ErrorAlert :message="error" @clear="error = null" />
    
    <h1 class="text-3xl font-bold mb-6">Athlete List</h1>

    <!-- Athletes Table -->
    <AthletesTable 
      v-if="!loading"
      :athletes="athletes"
      @delete="confirmDelete"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import LoadingOverlay from '~/components/shared/LoadingOverlay.vue';
import ErrorAlert from '~/components/shared/ErrorAlert.vue';
import { useAthleteManagement } from '~/composables/manageAthletes';
import { deleteAthletes } from '~/composables/deleteAthlete';
import AthletesTable from '~/components/admin/AthletesTable.vue';

const { athletes, error, loading, fetchAthletes } = useAthleteManagement();
const { confirmDelete } = deleteAthletes(athletes);

onMounted(async () => {
  await fetchAthletes();
});

</script>

<style scoped>
table {
  width: 100%;
  text-align: left;
  border-spacing: 0;
}
th, td {
  text-align: left;
}
</style>
