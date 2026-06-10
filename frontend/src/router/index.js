import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'homepage', component: () => import('@/views/homepage/HomepageIndex.vue'), meta: { requiresAuth: false } },
    { path: '/friend', name: 'friend', component: () => import('@/views/friend/FriendIndex.vue'), meta: { requiresAuth: true } },
    { path: '/create', name: 'create', component: () => import('@/views/create/CreateIndex.vue'), meta: { requiresAuth: true } },
    { path: '/profile', name: 'profile', component: () => import('@/views/user/profile/ProfileIndex.vue'), meta: { requiresAuth: true } },
    { path: '/login', name: 'login', component: () => import('@/views/user/account/LoginIndex.vue'), meta: { requiresAuth: false } },
    { path: '/register', name: 'register', component: () => import('@/views/user/account/RegisterIndex.vue'), meta: { requiresAuth: false } },
    { path: '/space/:user_id', name: 'user-space', component: () => import('@/views/user/space/SpaceIndex.vue'), meta: { requiresAuth: true } },
    { path: '/404', name: '404', component: () => import('@/views/error/NotFoundIndex.vue'), meta: { requiresAuth: false } },
    { path: '/:pathMatch(.*)*', redirect: '/404', meta: { requiresAuth: false } },
  ],
})

import { useUserStore } from '@/stores/user'

router.beforeEach((to, from, next) => {
  const user = useUserStore()
  if (to.meta.requiresAuth && user.hasPulledUserInfo && !user.isLogin()) {
    next({ name: 'login' })
  } else {
    next()
  }
});

export default router;
