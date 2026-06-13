<script setup>
import { ref, watch, useTemplateRef } from 'vue'
import Camera from '@/components/navbar/icons/Camera.vue'
import Modal from './Modal.vue'

const props = defineProps(['photo'])
const emit = defineEmits(['updatePhotoFile'])

const myPhoto = ref(props.photo)
const fileInput = useTemplateRef('fileInput')
const cropModal = useTemplateRef('cropModal')
const uploadFile = ref(null)

watch(() => props.photo, newPhoto => {
    myPhoto.value = newPhoto
})

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
    myPhoto.value = croppedBase64
    fetch(croppedBase64)
        .then(res => res.blob())
        .then(blob => {
            const file = new File([blob], 'avatar.png', { type: 'image/png' })
            uploadFile.value = file
            emit('updatePhotoFile', file)
        })
}

defineExpose({
    getUploadFile: () => uploadFile.value
})
</script>

<template>
    <div class="flex flex-col w-full mb-4">
        <!-- Title left aligned to match the rest of the form -->
        <div class="px-1 mb-6">
            <span class="text-sm font-semibold text-base-content/80">Photo</span>
        </div>

        <!-- Centered Photo and Button -->
        <div class="flex flex-col items-center gap-6">
            <div class="relative group">
                <div class="avatar">
                    <!-- Premium ring, shadow, and hover effect -->
                    <div @click="fileInput.click()"
                        class="w-36 h-36 rounded-full ring-4 ring-primary/20 ring-offset-base-100 ring-offset-4 shadow-xl group-hover:ring-primary/50 transition-shadow transition-transform duration-300 cursor-pointer overflow-hidden bg-base-200 flex items-center justify-center">
                        <img v-if="myPhoto" :src="myPhoto" alt="Avatar" class="w-full h-full object-cover" />
                        <div v-else class="flex flex-col items-center gap-1 text-base-content/50 group-hover:text-primary transition-colors mt-2">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mb-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                            <span class="text-xs font-semibold text-center leading-tight">Upload</span>
                        </div>
                    </div>
                </div>
                <!-- Camera Badge -->
                <div @click="fileInput.click()"
                    class="absolute bottom-1 right-2 bg-primary rounded-full p-2 shadow-lg shadow-primary/40 cursor-pointer hover:scale-110 hover:bg-primary-focus transition-transform transition-shadow z-10 flex items-center justify-center">
                    <Camera class="!w-5 !h-5" />
                </div>
            </div>

            <button @click="fileInput.click()"
                class="btn btn-outline btn-primary rounded-full px-8 shadow-sm hover:shadow-primary/30 hover:shadow-lg hover:scale-[1.02] transition-transform transition-shadow duration-300">
                Upload New
            </button>
            <input ref="fileInput" type="file" class="hidden" accept="image/*" @change="handleFileChange" />

            <Modal ref="cropModal" @crop="onCrop" />
        </div>
    </div>
</template>

<style scoped></style>