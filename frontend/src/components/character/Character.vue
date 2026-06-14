<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps({
    character: {
        type: Object,
        required: true
    }
})

// Determine if the character is "New" (created in the last 3 days)
const isNew = computed(() => {
    if (!props.character.create_time) return false;
    const createDate = new Date(props.character.create_time);
    const now = new Date();
    const diffTime = Math.abs(now - createDate);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays <= 3;
});

const goToUserSpace = () => {
    if (props.character.author?.id) {
        router.push(`/space/${props.character.author.id}`);
    }
};

// Helper to get array of tags (max 3)
const tagList = computed(() => {
    if (!props.character.tags) return [];
    // Split by comma or space and remove empty
    return props.character.tags.split(/[, ]+/).filter(t => t.trim().length > 0).slice(0, 3);
})

// Ensures media paths work depending on how your Vite/Django proxy is setup
const getImageUrl = (url) => {
    if (!url) return '';
    if (url.startsWith('http')) return url;
    return url; 
}
</script>

<template>
    <!-- Card Container -->
    <div
        class="card bg-base-300 shadow-xl border border-base-200/20 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 overflow-hidden group aspect-[2/3] w-full relative cursor-pointer">
        
        <!-- Full Background Image -->
        <div class="absolute inset-0 w-full h-full z-0">
            <img v-if="character.background_image" :src="getImageUrl(character.background_image)" alt="Background"
                class="object-cover w-full h-full group-hover:scale-105 transition-transform duration-700" />
            <div v-else class="w-full h-full bg-gradient-to-br from-primary/40 to-secondary/40"></div>
        </div>
        
        <!-- Dark Gradient Overlay for Readability -->
        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-black/10 z-0 pointer-events-none group-hover:from-black/95 transition-colors duration-500"></div>

        <!-- Private Badge (Top Right) -->
        <div v-if="!character.is_public" class="absolute top-4 right-4 z-20 badge bg-black/40 backdrop-blur-md text-white border-white/10 px-3 py-2 text-xs font-bold tracking-wide rounded-full shadow-sm">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-3 h-3 mr-1">
              <path fill-rule="evenodd" d="M8 1a3.5 3.5 0 0 0-3.5 3.5V7A1.5 1.5 0 0 0 3 8.5v5A1.5 1.5 0 0 0 4.5 15h7a1.5 1.5 0 0 0 1.5-1.5v-5A1.5 1.5 0 0 0 11.5 7V4.5A3.5 3.5 0 0 0 8 1Zm2 6V4.5a2 2 0 1 0-4 0V7h4Z" clip-rule="evenodd" />
            </svg>
            Private
        </div>

        <!-- Card Content (Pushed to bottom) -->
        <div class="relative z-10 flex flex-col h-full p-6 justify-end text-white">
            
            <!-- Avatar and Name Row -->
            <div class="flex items-end gap-4 mb-3">
                <!-- Circular Avatar -->
                <div class="avatar shrink-0">
                    <div class="w-16 h-16 rounded-full ring-2 ring-white/50 shadow-2xl bg-base-300">
                        <img v-if="character.photo" :src="getImageUrl(character.photo)" alt="Avatar" class="object-cover" />
                        <span v-else class="text-2xl font-bold text-base-content/50 flex items-center justify-center w-full h-full">
                            {{ character.name?.charAt(0)?.toUpperCase() || '?' }}
                        </span>
                    </div>
                </div>
                
                <!-- Name & New Badge -->
                <div class="flex-1 min-w-0 pb-1">
                    <h2 class="text-2xl font-extrabold text-white truncate drop-shadow-lg tracking-tight">
                        {{ character.name }}
                    </h2>
                    <div v-if="isNew" class="badge badge-error badge-sm mt-1 animate-pulse shadow-sm font-bold border-0 text-white">NEW</div>
                </div>
            </div>

            <!-- Bio / Profile -->
            <p class="text-sm text-white/80 line-clamp-3 mb-4 drop-shadow-md min-h-[3.75rem] leading-relaxed">
                {{ character.profile || 'This character is a mystery...' }}
            </p>

            <!-- Tags -->
            <div class="flex flex-wrap gap-2 mb-4">
                <span v-for="(tag, index) in tagList" :key="index"
                    class="badge badge-sm bg-white/10 text-white/90 border-white/20 backdrop-blur-md shadow-sm">
                    #{{ tag }}
                </span>
            </div>

            <!-- Divider -->
            <div class="w-full h-px bg-white/20 my-1 shrink-0"></div>

            <!-- Footer: Author & Stats -->
            <div class="flex items-center justify-between mt-3 shrink-0">
                <!-- Author Info -->
                <div @click.stop="goToUserSpace" class="flex items-center gap-2 max-w-[60%] cursor-pointer hover:opacity-70 transition-opacity" title="Visit User Space">
                    <div class="avatar">
                        <div class="w-6 h-6 rounded-full ring-1 ring-white/30">
                            <img v-if="character.author?.photo" :src="getImageUrl(character.author.photo)" alt="Author" />
                            <div v-else class="bg-black/50 w-full h-full flex items-center justify-center text-[10px] text-white font-bold">
                                {{ character.author?.username?.charAt(0)?.toUpperCase() || '?' }}
                            </div>
                        </div>
                    </div>
                    <span class="text-xs font-medium text-white/90 truncate drop-shadow-sm">
                        {{ character.author?.username || 'Unknown' }}
                    </span>
                </div>

                <!-- Chat Count -->
                <div class="flex items-center gap-1 text-white/90 bg-white/10 px-2.5 py-1 rounded-full tooltip tooltip-top tooltip-primary before:text-xs font-semibold backdrop-blur-md shadow-sm border border-white/5" :data-tip="`Total Chats: ${character.chat_count || 0}`">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-3.5 h-3.5 drop-shadow-sm">
                        <path fill-rule="evenodd" d="M10 2c-5.523 0-10 3.582-10 8 0 2.651 1.545 5.006 3.905 6.444-1.282 2.193-3.666 3.037-3.766 3.072a.5.5 0 0 0 .319.923c2.721.036 5.215-1.127 6.64-2.585C8.01 17.863 8.98 18 10 18c5.523 0 10-3.582 10-8s-4.477-8-10-8Zm0 14c-1.13 0-2.22-.16-3.238-.456a.5.5 0 0 0-.414.076c-1.135.795-2.614 1.503-4.14 1.765 1.054-1.163 1.944-2.735 2.225-4.32a.5.5 0 0 0-.166-.454C2.395 11.464 1 9.851 1 10c0-3.866 4.03-7 9-7s9 3.134 9 7-4.03 7-9 7Z" clip-rule="evenodd" />
                    </svg>
                    <span class="text-xs">{{ character.chat_count || 0 }}</span>
                </div>
            </div>
            
        </div>
    </div>
</template>

<style scoped>
/* Any custom tweaks go here */
</style>
