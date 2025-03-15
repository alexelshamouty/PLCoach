import { ref } from 'vue'

export function useErrorHandling() {
  const errorMessage = ref("")
  const showError = ref(false)

  function showErrorMessage(message: string) {
    errorMessage.value = message
    showError.value = true
    setTimeout(() => {
      showError.value = false
    }, 3000)
  }

  return {
    errorMessage,
    showError,
    showErrorMessage
  }
}
