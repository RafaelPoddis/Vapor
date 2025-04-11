import Library from './views/Library.vue'
import HomePage from './views/HomePage.vue'
import UploadGame from './views/UploadGame.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Layout from './components/Layout.vue'
import GamePage from './views/GamePage.vue'

const routes = [
  {
    path: '/',
    name: 'Layout',
    component: Layout,
    children: [
      {
        path: '',
        name: 'HomePage',
        component: HomePage,
      },
      {
        path: 'uploadGame',
        name: 'UploadGame',
        component: UploadGame
      },
      {
        path: 'library',
        name: 'Library',
        component: Library
      },
      {
        path: 'gamepage',
        name: 'GamePage',
        component: GamePage
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router