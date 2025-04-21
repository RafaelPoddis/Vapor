import Library from './views/Library.vue'
import GamePage from './views/GamePage.vue'
import HomePage from './views/HomePage.vue'
import Layout from './components/Layout.vue'
import UploadGame from './views/UploadGame.vue'
import { createRouter, createWebHistory } from 'vue-router'
import UserReviewCard from './components/UserReviewCard.vue'

const routes = [
  {
    path: '/store',
    name: 'Layout1',
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
        path: 'gamepage/:id',
        name: 'GamePage',
        component: GamePage
      },
      {
        path: 'teste',
        name: 'Teste',
        component: UserReviewCard
      }
    ]
  },
  {
    path: '/library',
    name: 'Layout2',
    component: Layout,
    children: [
      {
        path: '',
        name: 'Library',
        component: Library
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router