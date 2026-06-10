<script setup>
import { ref, watch } from 'vue'

const props = defineProps(['profile'])
const myProfile = ref(props.profile)

watch(() => props.profile, newProfile => {
    myProfile.value = newProfile
})

defineExpose({
    profile: myProfile
})
</script>

<template>
    <div class="flex flex-col w-full">
        <div class="flex justify-between items-end mb-2 px-1">
            <span class="text-sm font-semibold text-base-content/80">Bio</span>
            <span class="text-xs text-base-content/50">
                <span :class="{ 'text-error font-bold': (myProfile?.length || 0) >= 500 }">
                    {{ myProfile?.length || 0 }}
                </span>
                / 500
            </span>
        </div>
        <textarea v-model="myProfile" maxlength="500"
            class="textarea textarea-bordered textarea-primary w-full h-32 bg-base-100/50 focus:bg-base-100 shadow-sm focus:shadow-md transition-shadow leading-relaxed resize-none"></textarea>
    </div>
</template>

<style scoped></style>