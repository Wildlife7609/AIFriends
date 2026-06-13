<script setup>
import { ref } from 'vue'

const voiceId = ref('')

defineExpose({
    voiceId
})
</script>

<template>
    <div class="form-control w-full">
        <label class="label mb-2">
            <span class="label-text font-bold">Voice ID</span>
            <span class="label-text-alt text-base-content/60">Optional</span>
        </label>
        <input v-model="voiceId" type="text" placeholder="e.g. 21m00Tcm4TlvDq8ikWAM" class="input input-bordered w-full focus:input-primary transition-colors" />
    </div>
</template>

<style scoped></style>
