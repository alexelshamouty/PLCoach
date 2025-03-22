<template>
  <div v-if="show" class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50 p-4">
    <div class="bg-gray-800 rounded-lg p-6 max-w-3xl w-full max-h-[80vh] overflow-y-auto">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-xl font-bold">Video Manager</h2>
        <button @click="$emit('close')" class="text-gray-400 hover:text-white">
          <Icon name="mdi:close" size="24" />
        </button>
      </div>
      
      <div class="mb-4">
        <div class="text-gray-300 mb-2">
          <p><span class="font-semibold">Exercise:</span> {{ exerciseName }}</p>
          <p><span class="font-semibold">Type:</span> {{ exerciseLabel }}</p>
          <p><span class="font-semibold">Block:</span> {{ block }}</p>
          <p><span class="font-semibold">Week:</span> {{ week }}</p>
        </div>
      </div>
      
      <!-- Video Upload Section -->
      <div class="p-4 bg-gray-700 rounded mb-6">
        <h3 class="text-lg font-semibold mb-3">Upload New Video</h3>
        
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
          :disabled="isUploading"
          class="w-full p-2 bg-blue-600 rounded-lg hover:bg-blue-700 disabled:bg-gray-500"
        >
          <div class="flex items-center justify-center">
            <Icon v-if="isUploading" name="mdi:loading" class="animate-spin mr-2" />
            {{ isUploading ? 'Uploading...' : 'Upload Video' }}
          </div>
        </button>
      </div>
      
      <!-- Close button above video listing -->
      <div class="mb-6 flex justify-end">
        <button 
          @click="$emit('close')" 
          class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 flex items-center"
        >
          <Icon name="mdi:close" class="mr-2" />
          Close
        </button>
      </div>
      
      <!-- Video Listing Section -->
      <div>
        <h3 class="text-lg font-semibold mb-3">Exercise Videos</h3>
        
        <div v-if="isLoading" class="text-center p-8">
          <Icon name="mdi:loading" class="animate-spin text-3xl" />
          <p class="mt-2">Loading videos...</p>
        </div>
        
        <div v-else-if="videos.length === 0" class="text-center p-8 bg-gray-700 rounded">
          <Icon name="mdi:video-off" size="48" class="text-gray-400 mx-auto mb-2" />
          <p class="text-gray-300">No videos available for this exercise</p>
        </div>
        
        <div v-else class="space-y-4">
          <div v-for="video in videos" :key="video.id" class="bg-gray-700 rounded-lg p-3">
            <div class="flex items-center">
              <div class="flex-shrink-0 w-32 h-20 bg-gray-900 rounded overflow-hidden">
                <video class="w-full h-full object-cover">
                  <source :src="video.url" type="video/mp4">
                </video>
              </div>
              <div class="ml-4 flex-grow">
                <h4 class="text-white font-semibold">{{ video.title }}</h4>
                <p class="text-gray-300 text-sm truncate">{{ video.description }}</p>
              </div>
              <div class="flex space-x-2">
                <button @click="playVideo(video)" class="p-2 bg-blue-600 rounded hover:bg-blue-700">
                  <Icon name="mdi:play" />
                </button>
                <button @click="deleteVideo(video.id)" class="p-2 bg-red-600 rounded hover:bg-red-700">
                  <Icon name="mdi:trash-can" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue';

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
  }
});

const emit = defineEmits(['close']);

const videos = ref([]);
const isLoading = ref(false);
const isUploading = ref(false);
const selectedFile = ref(null);
const newVideo = ref({
  title: '',
  description: ''
});

// Watch for dialog visibility to load videos when opened
watch(() => props.show, (newValue) => {
  if (newValue) {
    fetchVideos();
  }
});

onMounted(() => {
  if (props.show) {
    fetchVideos();
  }
});

function handleFileChange(event) {
  const file = event.target.files[0];
  if (file) {
    selectedFile.value = file;
  }
}

async function fetchVideos() {
  isLoading.value = true;
  try {
    // Replace with actual API call
    // Example: const response = await fetch(`/api/videos?dayId=${props.dayId}&exerciseName=${props.exerciseName}`);
    // videos.value = await response.json();
    
    // Simulated response for development
    await new Promise(resolve => setTimeout(resolve, 1000));
    videos.value = [
      // Example data - replace with actual API response structure
      {
        id: '1',
        title: 'Proper Form Demo',
        description: 'This video demonstrates the correct form for the exercise',
        url: 'https://example.com/video1.mp4'
      },
      {
        id: '2',
        title: 'Common Mistakes',
        description: 'Common mistakes to avoid during this exercise',
        url: 'https://example.com/video2.mp4'
      }
    ];
  } catch (error) {
    console.error('Error fetching videos:', error);
    // Handle error state
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
    // Create form data for upload
    const formData = new FormData();
    formData.append('file', selectedFile.value);
    formData.append('title', newVideo.value.title);
    formData.append('description', newVideo.value.description);
    formData.append('dayId', props.dayId);
    formData.append('exerciseName', props.exerciseName);
    formData.append('exerciseLabel', props.exerciseLabel);
    formData.append('block', props.block);
    formData.append('week', props.week);
    
    // Replace with actual API call
    // Example: const response = await fetch('/api/videos/upload', {
    //   method: 'POST',
    //   body: formData
    // });
    
    // Simulated upload delay for development
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Reset form
    newVideo.value.title = '';
    newVideo.value.description = '';
    selectedFile.value = null;
    
    // Refresh video list
    await fetchVideos();
    
    // Show success notification
    alert('Video uploaded successfully!');
  } catch (error) {
    console.error('Error uploading video:', error);
    alert('Failed to upload video. Please try again.');
  } finally {
    isUploading.value = false;
  }
}

function playVideo(video) {
  // Open video in modal or new window
  window.open(video.url, '_blank');
}

async function deleteVideo(videoId) {
  if (!confirm('Are you sure you want to delete this video?')) {
    return;
  }
  
  try {
    // Replace with actual API call
    // Example: await fetch(`/api/videos/${videoId}`, {
    //   method: 'DELETE'
    // });
    
    // Simulated deletion for development
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // Remove from local state
    videos.value = videos.value.filter(v => v.id !== videoId);
    
    // Show success notification
    alert('Video deleted successfully!');
  } catch (error) {
    console.error('Error deleting video:', error);
    alert('Failed to delete video. Please try again.');
  }
}
</script>