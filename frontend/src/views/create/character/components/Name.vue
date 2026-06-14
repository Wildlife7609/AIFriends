<script setup>
const modelValue = defineModel()
</script>

<template>
    <div class="form-control w-full">
        <label class="label mb-2">
            <span class="label-text font-bold">Character Name <span class="text-error">*</span></span>
        </label>
        <input v-model="modelValue" type="text" placeholder="e.g. Alice" class="input input-bordered w-full focus:input-primary transition-colors" />
    </div>
</template>

<style scoped></style>