// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
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
