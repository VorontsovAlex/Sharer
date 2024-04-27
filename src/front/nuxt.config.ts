// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      link: [
        {
          rel: 'preconnect',
          href: 'https://fonts.googleapis.com'
        },
        {
          rel: 'preconnect',
          href: 'https://fonts.gstatic.com',
          crossorigin: true,
        },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap',
        }
      ],
    },
  },
  css: [
    '~/assets/css/main.css',
    '~/assets/scss/main.scss',
  ],
  devtools: { enabled: true },
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "~/assets/_colors.scss" as *;'
        }
      }
    }
  },
  runtimeConfig: {
    public: {
      baseURL: process.env.NUXT_APP_BASE_URL || 'http://172.20.208.1:8080/',
    },
  },
})
