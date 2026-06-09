<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user.js'
import api from "@/js/http/api.js"


const router = useRouter()
const user = useUserStore()
const username = ref('')
const password = ref('')
const errorMessage = ref('')

async function handleLogin() {
    // Clear previous errors
    errorMessage.value = ''
    if (!username.value.trim()) {
        errorMessage.value = 'Please fill in your username'
    }
    else if (!password.value.trim()) {
        errorMessage.value = 'Please fill in your password'
    } else {
        try {
            const res = await api.post('/api/user/account/login/', {
                username: username.value,
                password: password.value
            })
            const data = res.data
            if (data.result === true) {
                user.setAccessToken(data.data.access_token)
                user.setUserInfo(data.data)
                await router.push({ name: 'homepage' })

            } else {
                errorMessage.value = data.msg
            }
        } catch (error) {
            errorMessage.value = error.message
        }
    }
}

</script>

<template>
    <div class="login-wrapper">
        <div class="login-card">

            <!-- Header -->
            <div class="login-header">
                <div class="login-logo bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">
                    AI<span>Friends</span>
                </div>
                <div class="login-divider">
                    <span class="login-subtitle">Sign in to continue</span>
                </div>
            </div>

            <!-- Form -->
            <form class="login-fields" @submit.prevent="handleLogin">
                <div class="field-group">
                    <label for="username">Username</label>
                    <input v-model="username" name="username" type="text" class="input-primary"
                        placeholder="Enter your username" required />
                </div>
                <div class="field-group">
                    <label for="password">Password</label>
                    <input v-model="password" name="password" type="password" class="input-primary"
                        placeholder="Enter your password" required />
                </div>

                <!-- Error from backend -->
                <div class="min-h-[1.25rem] text-red-500">
                    <p v-if="errorMessage" class="login-error m-0">{{ errorMessage }}</p>
                </div>

                <button type="submit" class="btn btn-primary w-full">Login</button>
            </form>

            <!-- Footer -->
            <div class="login-footer">
                <span class="login-hint">New here?</span>
                <RouterLink :to="{ name: 'register' }" class="btn btn-outline btn-primary btn-sm">
                    Register
                </RouterLink>
            </div>
        </div>
    </div>
</template>
