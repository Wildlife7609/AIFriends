<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const user = useUserStore()

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
                    <input id="username" name="username" type="text" placeholder="Enter your username" required />
                </div>
                <div class="field-group">
                    <label for="password">Password</label>
                    <input id="password" name="password" type="password" placeholder="Enter your password" required />
                </div>

                <!-- Error from backend -->
                <p v-if="errorMsg" class="login-error">{{ errorMsg }}</p>

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
