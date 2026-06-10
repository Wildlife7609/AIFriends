<script setup>
import Username from './components/Username.vue';
import Photo from './components/Photo.vue';
import Profile from './components/Profile.vue';
import { useUserStore } from '@/stores/user'
import api from '@/js/http/api.js'
import { useTemplateRef } from 'vue';
import { ref } from 'vue';

const user = useUserStore()
const photoRef = useTemplateRef('photoRef')
const usernameRef = useTemplateRef('usernameRef')
const profileRef = useTemplateRef('profileRef')
const errorMessage = ref('')

// Toast Notification State
const showSuccessToast = ref(false)
const showErrorToast = ref(false)
const toastMessage = ref('')

const showToast = (msg, isSuccess = true) => {
    toastMessage.value = msg
    if (isSuccess) {
        showSuccessToast.value = true
        showErrorToast.value = false
        setTimeout(() => showSuccessToast.value = false, 2000)
    } else {
        showErrorToast.value = true
        showSuccessToast.value = false
        setTimeout(() => showErrorToast.value = false, 2000)
    }
}

async function saveChanges() {
    try {
        errorMessage.value = ''

        // Fix: Use the values from the exposed refs
        const currentUsername = usernameRef.value?.username?.trim()
        const currentProfile = profileRef.value?.profile?.trim()

        if (!currentUsername) {
            showToast('Please enter a username', false)
            return
        }
        if (!currentProfile) {
            showToast('Please enter a profile', false)
            return
        }

        const formData = new FormData()
        formData.append('username', currentUsername)
        formData.append('profile', currentProfile)

        // Append the actual file if the user cropped a new photo
        const file = photoRef.value?.getUploadFile()
        if (file) {
            formData.append('photo', file)
        }

        // Use the global Axios interceptor (api.js) so token refresh logic applies
        const res = await api.post('/api/user/profile/update/', formData)
        const data = res.data

        // Django 后端返回的是 result: True (布尔值) 并且数据在 data.data 里
        if (data.result === true) {
            user.setUserInfo(data.data)
            showToast('Profile updated successfully!', true)
        } else {
            showToast(data.msg || 'Update failed', false)
        }
    } catch (error) {
        showToast(error.message, false)
    }
}
</script>

<template>
    <div class="flex justify-center items-start h-full p-6 bg-base-200/30">
        <div
            class="card bg-base-100 shadow-2xl shadow-base-300/50 w-full max-w-4xl border border-base-200/60 mt-8 transition-shadow transition-transform duration-300 hover:shadow-3xl">
            <div class="card-body p-8 sm:p-10">
                <div class="border-b border-base-200 pb-4 mb-8">
                    <h2
                        class="text-3xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">
                        Edit Profile
                    </h2>
                    <p class="text-base-content/60 mt-1">Update your personal information and bio.</p>
                </div>

                <div class="flex flex-col lg:flex-row gap-12">
                    <!-- Left Column: Photo (1/3 width on large screens) -->
                    <div class="flex flex-col items-center lg:w-1/3">
                        <Photo ref="photoRef" :photo="user.photo"></Photo>
                    </div>

                    <!-- Right Column: Details (2/3 width on large screens) -->
                    <div class="flex flex-col gap-6 lg:w-2/3">
                        <Username ref="usernameRef" :username="user.username"></Username>
                        <Profile ref="profileRef" :profile="user.profile"></Profile>

                        <div class="card-actions justify-end mt-4 pt-6 border-t border-base-200">
                            <button class="btn btn-ghost hover:bg-base-200 transition-transform">Cancel</button>
                            <button @click="saveChanges"
                                class="btn btn-primary px-8 shadow-lg shadow-primary/30 hover:scale-[1.02] transition-transform">
                                Save Changes
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Beautiful DaisyUI Toast Notification -->
    <div v-if="showSuccessToast || showErrorToast"
        class="toast toast-top mt-16 z-50 transition-all duration-300 transform left-1/2 -translate-x-1/2"
        :class="[showSuccessToast || showErrorToast ? 'translate-y-0 opacity-100' : '-translate-y-10 opacity-0']">
        <div
            :class="['alert shadow-2xl flex items-center gap-3 px-6 py-4 rounded-full', showSuccessToast ? 'alert-success text-success-content' : 'alert-error text-error-content']">
            <!-- Success Icon -->
            <svg v-if="showSuccessToast" xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6"
                fill="none" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <!-- Error Icon -->
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none"
                viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span class="font-bold text-sm">{{ toastMessage }}</span>
        </div>
    </div>
</template>

<style scoped></style>