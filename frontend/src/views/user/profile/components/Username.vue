<script setup>
import { ref, watch } from 'vue'

const props = defineProps(['username'])
const myUsername = ref(props.username)

watch(() => props.username, newUsername => {
    myUsername.value = newUsername
})

</script>

<template>
    <div class="form-control w-full">
        <label class="label">
            <span class="label-text font-semibold text-base-content/80">Username</span>
        </label>
        <input v-model="myUsername" type="text" placeholder="Enter your username"
            class="input input-bordered input-primary w-full bg-base-100/50 focus:bg-base-100 transition-colors shadow-sm focus:shadow-md" />
    </div>
</template>

<style scoped></style>