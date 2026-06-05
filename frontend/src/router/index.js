import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'homepage', component: () => import('@/views/homepage/HomepageIndex.vue') },
    { path: '/friend', name: 'friend', component: () => import('@/views/friend/FriendIndex.vue') },
    { path: '/create', name: 'create', component: () => import('@/views/create/CreateIndex.vue') },
    { path: '/profile', name: 'profile', component: () => import('@/views/profile/ProfileIndex.vue') },
    { path: '/login', name: 'login', component: () => import('@/views/user/account/LoginIndex.vue') },
    { path: '/register', name: 'register', component: () => import('@/views/user/account/RegisterIndex.vue') },
    { path: '/space/:user_id', name: 'user-space', component: () => import('@/views/user/space/SpaceIndex.vue') },
    { path: '/404', name: '404', component: () => import('@/views/error/NotFoundIndex.vue') },
    { path: '/:pathMatch(.*)*', redirect: '/404' },
  ],
})

export default router
