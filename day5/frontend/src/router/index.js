import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import chaloTestKrteHain from '../views/test.vue'
import testView from '@/views/test.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/testKrLiyeHain/:indiaWantsToKnow',
      // component: chaloTestKrteHain,
      // component: () => import('../views/test.vue'),
      name: 'test',
      component: testView,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login.vue'),
    },
    {
      path: '/add-person',
      name: 'add-person',
      component: () => import('../views/add_person.vue'),
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/adminDash.vue'),
    }
  ],
})

export default router
