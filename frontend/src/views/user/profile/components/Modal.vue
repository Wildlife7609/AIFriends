<script setup>
import { ref, useTemplateRef } from 'vue'
import Croppie from 'croppie'
import 'croppie/croppie.css'

const emit = defineEmits(['crop'])

const dialog = useTemplateRef('dialog')
const croppieElement = useTemplateRef('croppieElement')
let croppieInstance = null

const showModal = (url) => {
    dialog.value.showModal()
    
    setTimeout(() => {
        if (!croppieInstance) {
            croppieInstance = new Croppie(croppieElement.value, {
                viewport: { width: 250, height: 250, type: 'circle' },
                boundary: { width: 300, height: 300 },
                showZoomer: true,
                enableOrientation: true
            })
        }
        croppieInstance.bind({ url })
    }, 50)
}

const closeModal = () => {
    dialog.value.close()
    if (croppieInstance) {
        croppieInstance.destroy()
        croppieInstance = null
    }
}

const handleCrop = () => {
    if (croppieInstance) {
        croppieInstance.result({ type: 'base64', size: 'viewport', format: 'png', circle: false }).then((result) => {
            emit('crop', result)
            closeModal()
        })
    }
}

defineExpose({ showModal, closeModal })
</script>

<template>
    <dialog ref="dialog" class="modal modal-bottom sm:modal-middle backdrop-blur-sm transition-all duration-300" @close="closeModal">
        <div class="modal-box flex flex-col items-center max-w-md bg-base-100 shadow-2xl shadow-primary/10 border border-base-200">
            <!-- Header -->
            <div class="w-full pb-4 mb-2 border-b border-base-200">
                <h3 class="font-extrabold text-2xl bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary text-left">
                    Adjust Photo
                </h3>
                <p class="text-sm text-base-content/60 mt-1 text-left">Drag and zoom to frame your perfect avatar</p>
            </div>
            
            <!-- Cropper Container -->
            <div class="w-full flex justify-center py-6 bg-gradient-to-b from-base-200/50 to-base-200/20 rounded-2xl ring-1 ring-base-content/5 shadow-inner mt-4">
                <div ref="croppieElement"></div>
            </div>
            
            <!-- Actions -->
            <div class="modal-action w-full flex justify-end gap-3 mt-8">
                <button type="button" class="btn btn-ghost hover:bg-base-200/60 rounded-full transition-colors" @click="closeModal">
                    Cancel
                </button>
                <button type="button" class="btn btn-primary px-8 rounded-full shadow-lg shadow-primary/30 hover:scale-[1.02] hover:shadow-xl transition-all duration-300" @click="handleCrop">
                    Apply Changes
                </button>
            </div>
        </div>
        <form method="dialog" class="modal-backdrop bg-base-300/40">
            <button>close</button>
        </form>
    </dialog>
</template>

<style scoped>
:deep(.croppie-container) {
    width: 100%;
    max-height: 440px;
    padding-bottom: 1rem;
}

:deep(.cr-boundary) {
    border-radius: 1rem;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.05);
}

/* Slider Wrapper */
:deep(.cr-slider-wrap) {
    display: flex !important;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    width: 80%;
    max-width: 300px;
    margin: 1.5rem auto 0 !important;
}

/* Zoom out icon */
:deep(.cr-slider-wrap::before) {
    content: "−";
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--fallback-bc, oklch(var(--bc) / 0.4));
    line-height: 1;
}

/* Zoom in icon */
:deep(.cr-slider-wrap::after) {
    content: "+";
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--fallback-bc, oklch(var(--bc) / 0.4));
    line-height: 1;
}

/* Track */
:deep(.cr-slider) {
    -webkit-appearance: auto !important;
    appearance: auto !important;
    flex-grow: 1;
    margin: 0 !important;
    cursor: pointer;
    /* This modern CSS property naturally colors the left filled part of the track and thumb */
    accent-color: var(--fallback-p, oklch(var(--p) / 1));
}
</style>
