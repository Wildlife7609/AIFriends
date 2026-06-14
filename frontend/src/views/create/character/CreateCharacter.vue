<script setup>
import { ref, onBeforeUnmount, useTemplateRef } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/js/http/api.js'

import Photo from '@/components/photo/Photo.vue'
import BackgroundImage from './components/BackgroundImage.vue'
import Name from './components/Name.vue'
import Profile from './components/Profile.vue'
import Prompt from './components/Prompt.vue'
import Greeting from './components/Greeting.vue'
import Tags from './components/Tags.vue'
import VoiceId from './components/VoiceId.vue'
import IsPublic from './components/IsPublic.vue'

const router = useRouter()

// Track active timeouts to prevent memory leaks
const activeTimeouts = []
const safeSetTimeout = (fn, delay) => {
    const id = setTimeout(fn, delay)
    activeTimeouts.push(id)
    return id
}

onBeforeUnmount(() => {
    activeTimeouts.forEach(clearTimeout)
})

// Refs to grab data from child components (File uploads only)
const photoRef = useTemplateRef('photoRef')
const bgRef = useTemplateRef('bgRef')

// Data-driven state for textual fields
const character = ref({
    is_public: true
})

// Loading & Toast State
const isSubmitting = ref(false)
const showSuccessToast = ref(false)
const showErrorToast = ref(false)
const toastMessage = ref('')

const showToast = (msg, isSuccess = true) => {
    toastMessage.value = msg
    if (isSuccess) {
        showSuccessToast.value = true
        showErrorToast.value = false
        safeSetTimeout(() => showSuccessToast.value = false, 2000)
    } else {
        showErrorToast.value = true
        showSuccessToast.value = false
        safeSetTimeout(() => showErrorToast.value = false, 3000)
    }
}

const submitCharacter = async () => {
    try {
        isSubmitting.value = true

        const { name, profile, prompt, greeting, tags, voice_id: voiceId, is_public: isPublic } = character.value

        const photoFile = photoRef.value?.getUploadFile()
        const bgFile = bgRef.value?.getUploadFile()

        // Validation
        if (!name) {
            showToast('Character Name is required', false)
            return
        }
        if (!profile) {
            showToast('Profile Description is required', false)
            return
        }
        if (!photoFile) {
            showToast('Avatar Photo is required', false)
            return
        }
        if (!bgFile) {
            showToast('Background Image is required', false)
            return
        }

        const formData = new FormData()
        formData.append('name', name)
        formData.append('profile', profile)
        formData.append('photo', photoFile)
        formData.append('background_image', bgFile)
        
        if (prompt) formData.append('prompt', prompt)
        if (greeting) formData.append('greeting', greeting)
        if (tags) formData.append('tags', tags)
        if (voiceId) formData.append('voice_id', voiceId)
        formData.append('is_public', isPublic ? 'true' : 'false')

        const res = await api.post('/api/create/character/create/', formData)
        const data = res.data

        if (data.result === true) {
            showToast('Character created successfully!', true)
            // Redirect after success (e.g., to dashboard)
            safeSetTimeout(() => {
                router.push('/')
            }, 1000)
        } else {
            showToast(data.msg || 'Creation failed', false)
        }
    } catch (error) {
        showToast(error.message || 'An error occurred', false)
    } finally {
        isSubmitting.value = false
    }
}
</script>

<template>
    <div class="flex justify-center items-start min-h-screen p-4 sm:p-6 bg-base-200/30 pb-24">
        <div class="card bg-base-100 shadow-2xl shadow-base-300/50 w-full max-w-5xl border border-base-200/60 mt-4 sm:mt-8 transition-shadow">
            
            <div class="card-body p-6 sm:p-10">
                <div class="border-b border-base-200 pb-4 mb-8">
                    <h2 class="text-3xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">
                        Create AI Character
                    </h2>
                    <p class="text-base-content/60 mt-1">Design a new AI companion with a unique personality and appearance.</p>
                </div>

                <div class="flex flex-col lg:flex-row gap-10">
                    
                    <!-- Left Column: Visuals -->
                    <div class="flex flex-col gap-6 lg:w-1/3">
                        <div class="text-center font-bold text-lg border-b border-base-200 pb-2">Appearance</div>
                        <div class="flex flex-col items-center">
                            <label class="label w-full"><span class="label-text font-bold">Avatar Photo <span class="text-error">*</span></span></label>
                            <Photo ref="photoRef"></Photo>
                        </div>
                        <BackgroundImage ref="bgRef"></BackgroundImage>
                        <IsPublic v-model="character.is_public"></IsPublic>
                    </div>

                    <!-- Right Column: Details -->
                    <div class="flex flex-col gap-6 lg:w-2/3">
                        <div class="text-center font-bold text-lg border-b border-base-200 pb-2">Identity & Personality</div>
                        
                        <Name v-model="character.name"></Name>
                        <Profile v-model="character.profile"></Profile>
                        
                        <!-- Advanced Settings (Unfolded & Beautiful) -->
                        <div class="mt-4 pt-6 border-t border-base-200">
                            <h3 class="text-lg font-bold mb-4 flex items-center gap-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd" />
                                </svg>
                                Advanced Configuration
                            </h3>
                            <div class="bg-base-200/40 rounded-2xl p-6 flex flex-col gap-5 border border-base-200 shadow-sm">
                                <Prompt v-model="character.prompt"></Prompt>
                                <Greeting v-model="character.greeting"></Greeting>
                                <div class="flex flex-col sm:flex-row gap-5">
                                    <Tags v-model="character.tags" class="flex-1"></Tags>
                                    <VoiceId v-model="character.voice_id" class="flex-1"></VoiceId>
                                </div>
                            </div>
                        </div>

                        <div class="card-actions justify-end mt-6 pt-6 border-t border-base-200">
                            <button @click="$router.push('/')" class="btn btn-ghost hover:bg-base-200 transition-transform">Cancel</button>
                            <button 
                                @click="submitCharacter" 
                                :disabled="isSubmitting"
                                class="btn btn-primary px-8 shadow-lg shadow-primary/30 hover:scale-[1.02] transition-transform"
                            >
                                <span v-if="isSubmitting" class="loading loading-spinner loading-sm"></span>
                                Create Character
                            </button>
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
    </div>
</template>

<style scoped></style>
