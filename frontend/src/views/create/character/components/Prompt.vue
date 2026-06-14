<script setup>
const modelValue = defineModel()
</script>

<template>
    <div class="form-control w-full">
        <label class="label mb-2">
            <span class="label-text font-bold">System Prompt</span>
            <span class="label-text-alt text-base-content/60">Optional</span>
        </label>
        <textarea v-model="modelValue" class="textarea textarea-bordered w-full h-32 rounded-xl focus:textarea-primary transition-colors" placeholder="You are a helpful AI assistant that loves to..."></textarea>
    </div>
</template>

<style scoped></style>
