<script setup>
import { ref } from 'vue'

const greeting = ref('')

defineExpose({
    greeting
})
</script>

<template>
    <div class="form-control w-full">
        <label class="label mb-2">
            <span class="label-text font-bold">Greeting Message</span>
            <span class="label-text-alt text-base-content/60">Optional</span>
        </label>
        <input v-model="greeting" type="text" placeholder="Hello! I'm Alice, how can I help you today?" class="input input-bordered w-full focus:input-primary transition-colors" />
    </div>
</template>

<style scoped></style>
