import type {NuxtPage} from 'nuxt/schema'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  generate: {
    dir: 'dist'  // This is the default
  },
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt'
  ],
  css: [
    '@/assets/css/tailwind.css',
  ],
  plugins: [
    { src: '~/plugins/amplify.js', mode: 'client' }
  ],
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true }
})
