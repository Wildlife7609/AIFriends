<script setup>
import { computed } from 'vue';

const props = defineProps({
    userInfo: {
        type: Object,
        required: true,
        default: () => ({})
    }
})

const getImageUrl = (url) => {
    if (!url) return '';
    if (url.startsWith('http')) return url;
    return url; 
}
</script>

<template>
    <div class="relative bg-base-100 rounded-3xl shadow-xl border border-base-200/60 overflow-hidden mb-10">
        <!-- Abstract Header Background -->
        <div class="h-32 md:h-48 w-full bg-gradient-to-br from-primary/20 via-secondary/20 to-accent/20 relative flex items-center justify-center overflow-hidden">
            <div class="absolute inset-0 bg-base-100/30 backdrop-blur-[2px]"></div>
            
            <!-- Large Faint Username Watermark -->
            <div class="absolute text-[5rem] md:text-[8rem] font-black text-base-content/[0.03] tracking-widest uppercase whitespace-nowrap select-none pointer-events-none">
                {{ userInfo?.username || 'AIFRIENDS' }}
            </div>
            
            <!-- Welcoming Subtitle -->
            <div class="relative z-10 text-base-content/40 font-bold tracking-[0.3em] uppercase text-xs md:text-sm mb-4 md:mb-8">
                Creator Space
            </div>
        </div>

        <div class="px-6 md:px-10 pb-8 relative flex flex-col md:flex-row items-center md:items-start gap-6">
            <!-- Avatar (Shifted up to overlap the background) -->
            <div class="-mt-16 md:-mt-20 relative z-10 shrink-0">
                <div class="avatar">
                    <div class="w-32 h-32 md:w-40 md:h-40 rounded-full ring-4 ring-base-100 ring-offset-base-100 shadow-2xl bg-base-200">
                        <img v-if="userInfo?.photo" :src="getImageUrl(userInfo.photo)" alt="User Avatar" class="object-cover" />
                        <span v-else class="text-5xl md:text-6xl font-bold text-base-content/20 flex items-center justify-center w-full h-full">
                            {{ userInfo?.username?.charAt(0)?.toUpperCase() || '?' }}
                        </span>
                    </div>
                </div>
            </div>

            <!-- User Info Text -->
            <div class="flex-1 text-center md:text-left mt-2 md:mt-4 w-full">
                <h1 class="text-3xl md:text-4xl font-extrabold text-base-content tracking-tight">
                    {{ userInfo?.username || 'Loading...' }}
                </h1>
                
                <!-- Bio / Profile -->
                <div class="mt-4 bg-base-200/50 rounded-2xl p-4 border border-base-300/30 w-full">
                    <h3 class="text-xs font-semibold text-base-content/50 uppercase tracking-wider mb-2">About</h3>
                    <p class="text-sm md:text-base text-base-content/80 leading-relaxed whitespace-pre-wrap">
                        {{ userInfo?.profile || 'This user is a mystery...' }}
                    </p>
                </div>
            </div>

            <!-- Optional: Action Buttons (Like "Share" or "Follow" in the future) -->
            <!-- 
            <div class="mt-4 md:mt-6 shrink-0">
                <button class="btn btn-primary rounded-full px-8 shadow-lg shadow-primary/30">
                    Follow
                </button>
            </div>
            -->
        </div>
    </div>
</template>

<style scoped>
/* Optional custom animations or styles */
</style>
