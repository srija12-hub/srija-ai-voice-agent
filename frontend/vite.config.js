import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [react()],
  server: {
    allowedHosts: [
      'poncho-sheath-chihuahua.ngrok-free.dev'
    ],
    proxy: {
      '/ask': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
    },
  },
})