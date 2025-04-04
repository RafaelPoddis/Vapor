import Library from './views/Library.vue'
import HomePage from './views/HomePage.vue'
import UploadGame from './views/UploadGame.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/library',
    name: 'Library',
    component: Library
  },
  {
    path: '/uploadGame',
    name: 'UplaodGame',
    component: UploadGame
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router