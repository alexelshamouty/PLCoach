export const deleteAthletes= () => {
  const athleteStore = useAthleteStore();
  const {athletes} = storeToRefs(athleteStore);
    const confirmDelete = async (id) => {
      if (confirm("Are you sure you want to delete this athlete?")) {
        try {
            console.log("Kicked him"); 
          if (athletes?.value) {
            athleteStore.deleteAthlete(id)
          }
  
          alert("Athlete deleted successfully!");
        } catch (error) {
          console.error("Error deleting athlete:", error);
          alert("Failed to delete athlete.");
        }
      }
    };
  
    return { confirmDelete };
  };
