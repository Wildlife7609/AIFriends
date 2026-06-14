<script setup>
const modelValue = defineModel()
</script>

<template>
    <div class="form-control w-full">
        <label class="label mb-2">
            <span class="label-text font-bold">Public Profile / Description <span class="text-error">*</span></span>
        </label>
        <textarea v-model="modelValue" class="textarea textarea-bordered w-full h-32 rounded-xl focus:textarea-primary transition-colors" placeholder="Describe the character's public persona..."></textarea>
    </div>
</template>

<style scoped></style>