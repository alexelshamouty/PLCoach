import { ref } from 'vue'

export const useTabs = () => {
  const tabs = [
    { id: 'programs', name: 'Programs' },
    { id: 'activity', name: 'Activity' }
  ]
  
  const activeTab = ref('programs')
  
  const setActiveTab = (tabId: string) => {
    activeTab.value = tabId
  }

  return {
    tabs,
    activeTab,
    setActiveTab
  }
}
