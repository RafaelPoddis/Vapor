import Library from './views/Library.vue'
import HomePage from './views/HomePage.vue'
import UploadGame from './views/UploadGame.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Layout from './components/Layout.vue'
import GamePage from './views/GamePage.vue'
import UserReviewCard from './components/UserReviewCard.vue'

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
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router