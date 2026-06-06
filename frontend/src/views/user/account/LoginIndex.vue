<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')
const error = ref('')

function handleLogin() {
    if (!email.value || !password.value) {
        error.value = 'Please enter your email and password.'
        return
    }
    // TODO: replace with real API call
    authStore.login({ email: email.value })
    router.push({ name: 'homepage' })
}
</script>

<template>
    <div class="login-wrapper">
        <div class="login-card">

            <!-- Header -->
            <div class="login-header">
                <div class="login-logo bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">AI<span>Friends</span></div>
                <div class="login-divider">
                    <span class="login-subtitle">Sign in to continue</span>
                </div>
            </div>

            <!-- Fields -->
            <div class="login-fields">
                <div class="field-group">
                    <label>Email</label>
                    <input
                        v-model="email"
                        type="email"
                        placeholder="you@example.com"
                        @keyup.enter="handleLogin"
                    />
                </div>
                <div class="field-group">
                    <label>Password</label>
                    <input
                        v-model="password"
                        type="password"
                        placeholder="••••••••"
                        @keyup.enter="handleLogin"
                    />
                </div>
            </div>

            <!-- Error -->
            <p v-if="error" class="login-error">{{ error }}</p>

            <!-- Actions -->
            <div class="login-actions">
                <button class="btn btn-primary w-full" @click="handleLogin">Login</button>
            </div>

            <!-- Divider hint -->
            <div class="login-footer">
                <span class="login-hint">New here?</span>
                <RouterLink :to="{ name: 'register' }" class="btn btn-outline btn-primary btn-sm">
                    Register
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* ── Wrapper ── */
.login-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
    padding-bottom: 25vh;
}

/* ── Card ── */
.login-card {
    width: min(24rem, 92vw);
    background: oklch(var(--b2));
    border: 2px solid oklch(var(--bc) / 0.2);
    border-radius: 1.5rem;
    padding: 2.25rem 2rem 2rem;
    box-shadow:
        0 2px 8px oklch(0 0 0 / 0.08),
        0 16px 48px oklch(0 0 0 / 0.22);
    animation: pop-in 0.35s cubic-bezier(0.34, 1.56, 0.64, 1) both;
}

@keyframes pop-in {
    from { opacity: 0; transform: translateY(18px) scale(0.95); }
    to   { opacity: 1; transform: translateY(0)    scale(1);    }
}

/* ── Header ── */
.login-header {
    text-align: center;
    margin-bottom: 1.75rem;
}

.login-logo {
    font-size: 2rem;
    font-weight: 900;
    letter-spacing: -0.04em;
}

.login-logo span { font-weight: 400; }

.login-divider {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-top: 0.85rem;
}

.login-divider::before,
.login-divider::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, #d1d5db, transparent);
}

.login-subtitle {
    font-size: 0.8rem;
    font-weight: 600;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    white-space: nowrap;
}

/* ── Fields ── */
.login-fields {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.field-group {
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
}

.field-group label {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: oklch(var(--bc) / 0.6);
}

.field-group input {
    width: 100%;
    padding: 0.7rem 1rem;
    border-radius: 0.75rem;
    border: 2px solid #d1d5db;
    background: #ffffff;
    color: #111827;
    font-size: 0.95rem;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06) inset;
}

.field-group input::placeholder { color: #9ca3af; }

.field-group input:focus {
    border-color: oklch(var(--p));
    box-shadow: 0 0 0 3px oklch(var(--p) / 0.18);
}

/* ── Error ── */
.login-error {
    margin-top: 0.75rem;
    font-size: 0.82rem;
    text-align: center;
    color: oklch(var(--er));
}

/* ── Actions ── */
.login-actions {
    margin-top: 1.25rem;
}

/* ── Bottom footer row ── */
.login-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 1.1rem;
}

/* ── Bottom hint ── */
.login-hint {
    font-size: 0.8rem;
    color: oklch(var(--bc) / 0.4);
}
</style>