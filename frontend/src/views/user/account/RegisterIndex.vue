<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import api from "@/js/http/api.js"

const router = useRouter()
const user = useUserStore()
const username = ref('')
const password = ref('')
const confirmPassword = ref('')
const errorMessage = ref('')

async function handleRegister() {
    // Clear previous errors
    errorMessage.value = ''
    if (!username.value.trim()) {
        errorMessage.value = 'Please fill in your username'
    }
    else if (!password.value.trim()) {
        errorMessage.value = 'Please fill in your password'
    }
    else if (password.value.trim() !== confirmPassword.value.trim()) {
        errorMessage.value = 'Passwords do not match'
    } else {
        try {
            const res = await api.post('/api/user/account/register/', {
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
                    <span class="login-subtitle">Create your account</span>
                </div>
            </div>

            <!-- Form -->
            <form @submit.prevent="handleRegister" class="login-fields">
                <div class="field-group">
                    <div class="field-group-item">
                        <label for="username">Username</label>
                        <input v-model="username" id="username" name="username" type="text"
                            placeholder="Enter your username" required />
                    </div>
                </div>
                <div class="field-group">
                    <label for="password">Password</label>
                    <input v-model="password" id="password" name="password" type="password" placeholder="••••••••"
                        required />
                </div>
                <div class="field-group">
                    <label for="confirmPassword">Confirm Password</label>
                    <input v-model="confirmPassword" id="confirmPassword" name="confirmPassword" type="password"
                        placeholder="••••••••" required />
                </div>

                <!-- Error -->
                <div class="min-h-[1.25rem] text-red-500">
                    <p v-if="errorMessage" class="login-error m-0">{{ errorMessage }}</p>
                </div>

                <button type="submit" class="btn btn-primary w-full">Register</button>
            </form>

            <!-- Footer -->
            <div class="login-footer">
                <span class="login-hint">Already have an account?</span>
                <RouterLink :to="{ name: 'login' }" class="btn btn-outline btn-primary btn-sm">
                    Login
                </RouterLink>
            </div>
        </div>
    </div>
</template>