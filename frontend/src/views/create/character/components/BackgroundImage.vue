<script setup>
import { ref, useTemplateRef } from 'vue'
import Modal from '@/components/photo/Modal.vue'

const fileInputRef = ref(null)
const previewUrl = ref(null)
const selectedFile = ref(null)
const cropModal = useTemplateRef('cropModal')

const handleFileChange = (event) => {
    const file = event.target.files[0]
    event.target.value = ''
    if (!file) return
    const reader = new FileReader()
    reader.onload = (e) => {
        cropModal.value.showModal(e.target.result)
    }
    reader.readAsDataURL(file)
}

const onCrop = (croppedBase64) => {
    previewUrl.value = croppedBase64
    fetch(croppedBase64)
        .then(res => res.blob())
        .then(blob => {
            const file = new File([blob], 'background.png', { type: 'image/png' })
            selectedFile.value = file
        })
}

const triggerFileInput = () => {
    fileInputRef.value?.click()
}

// Expose the method to get the actual file object for the FormData
const getUploadFile = () => {
    return selectedFile.value
}

defineExpose({
    getUploadFile,
    previewUrl
})
</script>

<template>
    <div class="form-control w-full">
        <label class="label mb-2">
            <span class="label-text font-bold">Background Image <span class="text-error">*</span></span>
        </label>

        <div @click="triggerFileInput"
            class="relative w-full max-w-[220px] mx-auto aspect-[9/16] bg-base-200 rounded-2xl overflow-hidden cursor-pointer border-2 border-dashed border-base-300 hover:border-primary transition-colors flex flex-col items-center justify-center group shadow-inner">
            <!-- Hidden file input -->
            <input type="file" ref="fileInputRef" class="hidden" accept="image/*" @change="handleFileChange" />

            <!-- Preview Image -->
            <img v-if="previewUrl" :src="previewUrl" class="absolute inset-0 w-full h-full object-cover" />

            <!-- Overlay for hovering (if image exists) -->
            <div v-if="previewUrl"
                class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                <span class="text-white font-semibold flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mb-1" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                    Change Background
                </span>
            </div>

            <!-- Upload Placeholder (if no image) -->
            <div v-if="!previewUrl"
                class="flex flex-col items-center gap-3 text-base-content/50 group-hover:text-primary transition-colors p-4">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 mb-2" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                <span class="font-semibold text-center text-sm">Upload Background</span>
                <span class="text-xs opacity-75">General Size (9:16)</span>
            </div>
        </div>

        <Modal 
            ref="cropModal" 
            :viewportWidth="180" 
            :viewportHeight="320" 
            viewportType="square" 
            :boundaryWidth="260" 
            :boundaryHeight="400" 
            @crop="onCrop" 
        />
    </div>
</template>

<style scoped></style>