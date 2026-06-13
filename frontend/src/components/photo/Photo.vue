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
                        class="w-36 rounded-full ring-4 ring-primary/20 ring-offset-base-100 ring-offset-4 shadow-xl group-hover:ring-primary/50 transition-shadow transition-transform duration-300 cursor-pointer overflow-hidden">
                        <img :src="myPhoto" alt="Avatar" class="w-full h-full object-cover" />
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