<script setup>
const modelValue = defineModel()
</script>

<template>
    <div class="form-control w-max mt-2">
        <label class="label cursor-pointer flex gap-4">
            <span class="label-text font-bold">Public Character</span>
            <input v-model="modelValue" type="checkbox" class="toggle toggle-primary" />
        </label>
        <label class="label py-0">
             <span class="label-text-alt text-base-content/60">Allow others to chat with this character</span>
        </label>
    </div>
</template>

<style scoped></style>
