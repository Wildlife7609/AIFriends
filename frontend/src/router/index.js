import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'homepage', component: () => import('@/views/homepage/HomepageIndex.vue'), meta: { requiresAuth: false } },
    { path: '/friend', name: 'friend', component: () => import('@/views/friend/FriendIndex.vue'), meta: { requiresAuth: true } },
    { path: '/create', name: 'create', component: () => import('@/views/create/character/CreateCharacter.vue'), meta: { requiresAuth: true } },
    { 
      path: '/update/:character_id', 
      name: 'update-character', 
      component: () => import('@/views/create/character/UpdateCharacter.vue'), 
      meta: { requiresAuth: true },
      beforeEnter: async (to, from, next) => {
        try {
          const api = (await import('@/js/http/api.js')).default;
          const res = await api.get(`/api/create/character/get_single/?character_id=${to.params.character_id}`);
          if (res.data && res.data.result === true) {
            next();
          } else {
            next('/404');
          }
        } catch(e) {
          next('/404');
        }
      }
    },
    { path: '/profile', name: 'profile', component: () => import('@/views/user/profile/ProfileIndex.vue'), meta: { requiresAuth: true } },
    { path: '/login', name: 'login', component: () => import('@/views/user/account/LoginIndex.vue'), meta: { requiresAuth: false } },
    { path: '/register', name: 'register', component: () => import('@/views/user/account/RegisterIndex.vue'), meta: { requiresAuth: false } },
    { path: '/space/:user_id', name: 'user-space', component: () => import('@/views/user/space/SpaceIndex.vue'), meta: { requiresAuth: true } },
    { path: '/404', name: '404', component: () => import('@/views/error/NotFoundIndex.vue'), meta: { requiresAuth: false } },
    { path: '/:pathMatch(.*)*', redirect: '/404', meta: { requiresAuth: false } },
  ],
})

import { useUserStore } from '@/stores/user'

router.beforeEach((to, from) => {
  const user = useUserStore()
  if (to.meta.requiresAuth && user.hasPulledUserInfo && !user.isLogin()) {
    return { name: 'login' }
  }
});

export default router;
