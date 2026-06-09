<script setup>
import { onMounted } from 'vue';
import NavBar from './components/navbar/NavBar.vue'
import { useUserStore } from '@/stores/user';
import api from "@/js/http/api.js"
import { useRoute, useRouter } from 'vue-router';

const user = useUserStore()
const route = useRoute()
const router = useRouter()

onMounted(async () => {
    try {
        const res = await api.get('/api/user/account/get_user_info/')
        const data = res.data
        if (data.result === true) {
            user.setUserInfo(data.data)
        }
    } catch (error) {
        console.log(error)
    } finally {
        user.setHasPulledUserInfo(true)
        if (route.meta.requiresAuth && !user.isLogin()) {
            router.replace({ name: 'login' })
        }
    }
})

</script>

<template>
    <NavBar>
        <router-view />
    </NavBar>
</template>

<style scoped></style>
