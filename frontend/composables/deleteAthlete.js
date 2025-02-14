export const deleteAthletes= (athletes) => {
    const confirmDelete = async (id) => {
      if (confirm("Are you sure you want to delete this athlete?")) {
        try {
            console.log("Kicked him"); 
          if (athletes?.value) {
            athletes.value = athletes.value.filter(a => a.id !== id); // Remove from list
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
