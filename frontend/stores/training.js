import { defineStore } from "pinia";

export const useTrainingStore = defineStore('training', {
  state: () => ({
    items: {
      "1": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "2": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "3": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "4": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "5": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "6": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "7": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "8": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "9": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "10": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "11": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ],
      "12": [
        { 
          title: "Monday", 
          content: [
            { name: "Bench Press", label: "Chest", sets: 4, reps: 10, comments: "Great work", rpe: 8 },
            { name: "Pull-ups", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Squats", label: "Squat", sets: 4, reps: 8, comments: "Great work", rpe: 9 }
          ]
        },
        { 
          title: "Wednesday", 
          content: [
            { name: "Deadlift", label: "Deadlift", sets: 4, reps: 6, comments: "Great work", rpe: 9 },
            { name: "Rows", label: "Back", sets: 3, reps: 12, comments: "Great work", rpe: 8 },
            { name: "Leg Press", label: "Quads", sets: 4, reps: 10, comments: "Great work", rpe: 7 }
          ]
        },
        { 
          title: "Friday", 
          content: [
            { name: "Overhead Press", label: "Shoulders", sets: 4, reps: 8, comments: "Great work", rpe: 8 },
            { name: "Lateral Raises", label: "Shoulders", sets: 3, reps: 12, comments: "Great work", rpe: 7 },
            { name: "Tricep Extensions", label: "Triceps", sets: 4, reps: 10, comments: "Great work", rpe: 9 }
          ]
        }
      ]
    }
  }),
  actions: {
    countSetsPerWeek(label, selectedOption1, selectedOption2, allSets, messageOpen) {
      console.log("I am gonna count all " + label + " sets per week");
      console.log("Week is in " + selectedOption1 + " week " + selectedOption2);
      console.log("And here are the details of this week");
      console.log(this.items[selectedOption2]);
      const week = this.items[selectedOption2];
      allSets.value = 0;
      week.forEach((day) => {
        day.content.forEach((exercise) => {
          if (exercise.label === label) {
            allSets.value += exercise.sets;
            messageOpen.value = true;
          }
        });
      });
    },
    addExercise(week, dayIndex, exercise) {
      if (this.items[week] && this.items[week][dayIndex]) {
        this.items[week][dayIndex].content.push(exercise);
      } else {
        console.error("Invalid week or day index");
      }
    },
    deleteExercise(week, dayIndex, exerciseIndex) {
      if (this.items[week] && this.items[week][dayIndex] && this.items[week][dayIndex].content[exerciseIndex]) {
        this.items[week][dayIndex].content.splice(exerciseIndex, 1);
      } else {
        console.error("Invalid week, day index, or exercise index");
      }
    },
    addDay(week, dayTitle) {
      if (!this.items[week]) {
        this.items[week] = [];
      }
      this.items[week].push({ title: dayTitle, content: [] });
    },
  }
});
