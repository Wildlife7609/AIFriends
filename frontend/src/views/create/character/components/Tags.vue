<script setup>
const modelValue = defineModel()
</script>

<template>
    <div class="form-control w-full">
        <label class="label mb-2">
            <span class="label-text font-bold">Tags</span>
            <span class="label-text-alt text-base-content/60">Optional</span>
        </label>
        <input v-model="modelValue" type="text" placeholder="e.g. Friendly, Assistant, Helpful" class="input input-bordered w-full focus:input-primary transition-colors" />
    </div>
</template>

<style scoped></style>
