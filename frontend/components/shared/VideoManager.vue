<template>
  <div v-if="show" class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50 p-2">
    <div class="bg-gray-800 rounded-lg p-4 sm:p-6 w-full max-w-3xl max-h-[90vh] sm:max-h-[80vh] overflow-y-auto hide-scrollbar">
      <div class="flex justify-between items-center mb-4 sm:mb-6">
        <h2 class="text-lg sm:text-xl font-bold truncate pr-2">Video Manager</h2>
        <button @click="$emit('close')" class="text-gray-400 hover:text-white flex-shrink-0">
          <Icon name="mdi:close" size="24" />
        </button>
      </div>
      
      <div class="mb-4">
        <div class="text-gray-300 mb-2 text-sm sm:text-base">
          <p class="truncate"><span class="font-semibold">Exercise:</span> {{ exerciseName }}</p>
          <p class="truncate"><span class="font-semibold">Type:</span> {{ exerciseLabel }}</p>
          <p class="truncate"><span class="font-semibold">Block:</span> {{ block }}</p>
          <p class="truncate"><span class="font-semibold">Week:</span> {{ week }}</p>
        </div>
      </div>
      
      <!-- Video Upload Section -->
      <div class="p-3 sm:p-4 bg-gray-700 rounded mb-4 sm:mb-6">
        <h3 class="text-base sm:text-lg font-semibold mb-2 sm:mb-3">Upload New Video</h3>
        
        <div class="mb-4">
          <label class="block text-sm text-gray-300 mb-1">Video Title</label>
          <input 
            v-model="newVideo.title" 
            placeholder="Enter video title" 
            class="w-full p-2 bg-gray-600 text-white rounded outline-none"
          />
        </div>
        
        <div class="mb-4">
          <label class="block text-sm text-gray-300 mb-1">Video Description</label>
          <textarea
            v-model="newVideo.description"
            placeholder="Enter video description"
            rows="3"
            class="w-full p-2 bg-gray-600 text-white rounded outline-none resize-none"
          ></textarea>
        </div>
        
        <div class="mb-4">
          <label class="block text-sm text-gray-300 mb-1">Video Type</label>
          <select 
            v-model="newVideo.type" 
            class="w-full p-2 bg-gray-600 text-white rounded outline-none"
          >
            <option value="coach">Coach Video</option>
            <option value="athlete">Athlete Video</option>
          </select>
        </div>
        
        <div class="mb-4">
          <label class="block text-sm text-gray-300 mb-1">Video File</label>
          <div class="relative border-2 border-dashed border-gray-500 rounded-lg p-6 text-center">
            <input
              type="file"
              accept="video/*"
              @change="handleFileChange"
              class="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            />
            <div v-if="!selectedFile">
              <Icon name="mdi:upload" size="36" class="text-gray-400 mx-auto mb-2" />
              <p class="text-gray-300">Click or drag video file here to upload</p>
            </div>
            <div v-else class="text-left">
              <p class="text-green-400 flex items-center">
                <Icon name="mdi:check-circle" class="mr-2" />
                {{ selectedFile.name }}
              </p>
            </div>
          </div>
        </div>
        
        <button 
          @click="uploadVideo"
          :disabled="isUploading || videoManagementLoading"
          class="w-full p-2 bg-blue-600 rounded-lg hover:bg-blue-700 disabled:bg-gray-500"
        >
          <div class="flex items-center justify-center">
            <Icon v-if="isUploading || videoManagementLoading" name="mdi:loading" class="animate-spin mr-2" />
            {{ isUploading || videoManagementLoading ? 'Uploading...' : 'Upload Video' }}
          </div>
        </button>
      </div>
      
      <!-- Close button above video listing -->
      <div class="mb-4 sm:mb-6 flex justify-end">
        <button 
          @click="$emit('close')" 
          class="px-3 py-1 sm:px-4 sm:py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 flex items-center text-sm sm:text-base"
        >
          <Icon name="mdi:close" class="mr-2" />
          Close
        </button>
      </div>
      
      <!-- Video Listing Section -->
      <div>
        <h3 class="text-base sm:text-lg font-semibold mb-2 sm:mb-3">Exercise Videos</h3>
        
        <div v-if="isLoading || videoManagementLoading" class="text-center p-8">
          <Icon name="mdi:loading" class="animate-spin text-3xl" />
          <p class="mt-2">Loading videos...</p>
        </div>
        
        <div v-else-if="videos.length === 0" class="text-center p-8 bg-gray-700 rounded">
          <Icon name="mdi:video-off" size="48" class="text-gray-400 mx-auto mb-2" />
          <p class="text-gray-300">No videos available for this exercise</p>
        </div>
        
        <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <!-- Coach Videos Column -->
          <div class="space-y-3 sm:space-y-4">
            <h4 class="text-sm sm:text-md font-semibold pb-2 border-b border-gray-600">Coach Videos</h4>
            <div v-if="coachVideos.length === 0" class="text-center p-3 sm:p-4 bg-gray-700 rounded">
              <p class="text-gray-300 text-sm">No coach videos available</p>
            </div>
            <div v-else v-for="video in coachVideos" :key="video.id" class="bg-gray-700 rounded-lg p-2 sm:p-3">
              <div class="flex items-center">
                <div class="flex-shrink-0 w-20 sm:w-32 h-16 sm:h-20 bg-gray-900 rounded overflow-hidden">
                  <video class="w-full h-full object-cover">
                    <source :src="video.url" type="video/mp4">
                  </video>
                </div>
                <div class="ml-2 sm:ml-4 flex-grow min-w-0">
                  <h4 class="text-white font-semibold text-sm sm:text-base truncate">{{ video.title }}</h4>
                  <p class="text-gray-300 text-xs sm:text-sm truncate">{{ video.description }}</p>
                </div>
                <div class="flex space-x-1 sm:space-x-2 flex-shrink-0 ml-1">
                  <button @click="playVideo(video)" class="p-1 sm:p-2 bg-blue-600 rounded hover:bg-blue-700">
                    <Icon name="mdi:play" size="20" />
                  </button>
                  <button @click="deleteVideo(video.id, 'coach')" class="p-1 sm:p-2 bg-red-600 rounded hover:bg-red-700">
                    <Icon name="mdi:trash-can" size="20" />
                  </button>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Athlete Videos Column -->
          <div class="space-y-3 sm:space-y-4 mt-4 lg:mt-0">
            <h4 class="text-sm sm:text-md font-semibold pb-2 border-b border-gray-600">Athlete Videos</h4>
            <div v-if="athleteVideos.length === 0" class="text-center p-3 sm:p-4 bg-gray-700 rounded">
              <p class="text-gray-300 text-sm">No athlete videos available</p>
            </div>
            <div v-else v-for="video in athleteVideos" :key="video.id" class="bg-gray-700 rounded-lg p-2 sm:p-3">
              <div class="flex items-center">
                <div class="flex-shrink-0 w-20 sm:w-32 h-16 sm:h-20 bg-gray-900 rounded overflow-hidden">
                  <video class="w-full h-full object-cover">
                    <source :src="video.url" type="video/mp4">
                  </video>
                </div>
                <div class="ml-2 sm:ml-4 flex-grow min-w-0">
                  <h4 class="text-white font-semibold text-sm sm:text-base truncate">{{ video.title }}</h4>
                  <p class="text-gray-300 text-xs sm:text-sm truncate">{{ video.description }}</p>
                </div>
                <div class="flex space-x-1 sm:space-x-2 flex-shrink-0 ml-1">
                  <button @click="playVideo(video)" class="p-1 sm:p-2 bg-blue-600 rounded hover:bg-blue-700">
                    <Icon name="mdi:play" size="20" />
                  </button>
                  <button @click="deleteVideo(video.id, 'athlete')" class="p-1 sm:p-2 bg-red-600 rounded hover:bg-red-700">
                    <Icon name="mdi:trash-can" size="20" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch, onBeforeUnmount } from 'vue';
import { useVideoManagement } from '~/composables/videoManagement';
import { useState } from '#app';

const props = defineProps({
  show: {
    type: Boolean,
    default: false
  },
  block: {
    type: String,
    required: true
  },
  week: {
    type: String,
    required: true
  },
  dayId: {
    type: String,
    required: true
  },
  exerciseName: {
    type: String,
    required: true
  },
  exerciseLabel: {
    type: String,
    required: true
  },
  coach: {
    type: Boolean,
    default: false
  }
});

const emit = defineEmits(['close', 'video-uploaded', 'video-deleted']);

const videos = ref([]);
const isLoading = ref(false);
const isUploading = ref(false);
const selectedFile = ref(null);
const newVideo = ref({
  title: '',
  description: '',
  type: 'coach' // Default to coach video
});

// Initialize the video management composable with shared state
const videoManagement = useVideoManagement();
// Get the shared loading state
const videoManagementLoading = useState('videoManagement.loading');
const videoManagementError = useState('videoManagement.error');

// Make sure loading is reset when the component mounts
onMounted(() => {
  // Reset loading state initially
  videoManagement.resetLoadingState();
  
  if (props.show) {
    fetchVideos();
  }
});

// Also ensure loading state is reset when the component is unmounted
onBeforeUnmount(() => {
  videoManagement.resetLoadingState();
});

// Watch for dialog visibility to load videos when opened
watch(() => props.show, (newValue) => {
  if (newValue) {
    // Reset loading state when dialog is opened
    videoManagement.resetLoadingState();
    fetchVideos();
  }
});

// Computed properties to filter videos by type
const coachVideos = computed(() => {
  return videos.value.filter(video => video.type === 'coach');
});

const athleteVideos = computed(() => {
  return videos.value.filter(video => video.type === 'athlete');
});

function handleFileChange(event) {
  const file = event.target.files[0];
  if (file) {
    selectedFile.value = file;
  }
}

async function fetchVideos() {
  isLoading.value = true;
  videoManagement.resetLoadingState(); 
  
  try {
    // Simplified - return empty arrays
    videos.value = [];
  } catch (error) {
    console.error('Error fetching videos:', error);
  } finally {
    isLoading.value = false;
  }
}

async function uploadVideo() {
  if (!selectedFile.value || !newVideo.value.title) {
    alert('Please add a title and select a video file');
    return;
  }
  
  isUploading.value = true;
  try {
    // Simplified mock response
    const result = { id: 'mock-video-id' };
    
    // Reset form
    newVideo.value.title = '';
    newVideo.value.description = '';
    selectedFile.value = null;
    
    // Emit event with simplified data
    emit('video-uploaded', { 
      videoId: result.id, 
      type: newVideo.value.type,
      isCoach: props.coach
    });
    
  } catch (error) {
    console.error('Error uploading video:', error);
    alert('Failed to upload video. Please try again.');
  } finally {
    isUploading.value = false;
  }
}

function playVideo(video) {
  // Simplified - just log instead of opening
  console.log('Playing video:', video.url);
}

async function deleteVideo(videoId, type) {
  if (!confirm('Are you sure you want to delete this video?')) {
    return;
  }
  
  try {
    // Simplified - just remove from local state
    videos.value = videos.value.filter(v => v.id !== videoId);
    
    // Emit simplified event
    emit('video-deleted', { 
      videoId, 
      type,
      isCoach: props.coach
    });
    
  } catch (error) {
    console.error('Error deleting video:', error);
    alert('Failed to delete video. Please try again.');
  }
}
</script>

<style scoped>
.hide-scrollbar {
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE and Edge */
}
.hide-scrollbar::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera */
}
</style>