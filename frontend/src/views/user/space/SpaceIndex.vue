<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/js/http/api.js'
import UserInfoField from './components/UserInfoField.vue'
import Character from '@/components/character/Character.vue'

const route = useRoute()
const router = useRouter()

const userId = route.params.user_id
const userInfo = ref({})
const characterList = ref([])

// UI State
const isLoadingInfo = ref(true)
const isLoadingCharacters = ref(true)
const errorMessage = ref('')

// Pagination
const itemsCount = ref(0)
const hasMore = ref(true)

// Timeouts
const activeTimeouts = []
const safeSetTimeout = (fn, delay) => {
    const id = setTimeout(fn, delay)
    activeTimeouts.push(id)
    return id
}

onBeforeUnmount(() => {
    activeTimeouts.forEach(clearTimeout)
})

const fetchUserInfo = async () => {
    try {
        isLoadingInfo.value = true
        const res = await api.get('/api/user/account/get_user_info/', {
            params: { user_id: userId }
        })
        if (res.data.result === true) {
            userInfo.value = res.data.data
        } else {
            errorMessage.value = res.data.msg || 'Failed to load user info.'
        }
    } catch (err) {
        errorMessage.value = 'Network error fetching user info.'
    } finally {
        isLoadingInfo.value = false
    }
}

const fetchCharacters = async (isLoadMore = false) => {
    if (!isLoadMore) {
        itemsCount.value = 0
        characterList.value = []
        isLoadingCharacters.value = true
    }
    
    try {
        const res = await api.get('/api/create/character/get_list/', {
            params: {
                user_id: userId,
                items_count: itemsCount.value
            }
        })
        
        if (res.data.result === true) {
            const fetched = res.data.data
            if (fetched.length < 20) {
                hasMore.value = false
            } else {
                hasMore.value = true
            }
            characterList.value.push(...fetched)
            itemsCount.value += fetched.length
        }
    } catch (err) {
        console.error("Failed to load characters", err)
    } finally {
        isLoadingCharacters.value = false
    }
}

onMounted(() => {
    if (!userId) {
        router.push('/404')
        return
    }
    fetchUserInfo()
    fetchCharacters()
})
</script>

<template>
    <div class="min-h-screen bg-base-200/30 py-8 px-4 sm:px-6 lg:px-8">
        <div class="max-w-7xl mx-auto space-y-8">
            
            <!-- Error State -->
            <div v-if="errorMessage" class="alert alert-error shadow-lg rounded-2xl">
                <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                <span>{{ errorMessage }}</span>
            </div>

            <!-- User Info Header -->
            <div v-if="isLoadingInfo" class="skeleton h-64 w-full rounded-3xl"></div>
            <UserInfoField v-else-if="userInfo.user_id" :userInfo="userInfo" />

            <!-- Character List Section -->
            <div class="space-y-6">
                <div class="flex items-center justify-between px-2">
                    <h2 class="text-2xl font-bold text-base-content tracking-tight">Characters</h2>
                    <span v-if="!isLoadingCharacters" class="badge badge-primary badge-outline font-bold">{{ characterList.length }}</span>
                </div>

                <!-- Skeletons while loading initially -->
                <div v-if="isLoadingCharacters && characterList.length === 0" class="grid grid-cols-[repeat(auto-fill,minmax(240px,1fr))] gap-9 mt-12 justify-items-center w-full px-9">
                    <div v-for="i in 4" :key="i" class="skeleton aspect-[2/3] w-full rounded-2xl"></div>
                </div>

                <!-- Characters Grid -->
                <div v-else-if="characterList.length > 0" class="grid grid-cols-[repeat(auto-fill,minmax(240px,1fr))] gap-9 mt-12 justify-items-center w-full px-9">
                    <Character 
                        v-for="char in characterList" 
                        :key="char.id" 
                        :character="char" 
                    />
                </div>

                <!-- Empty State -->
                <div v-else class="text-center py-24 bg-base-100 rounded-3xl border border-base-200/60 shadow-sm flex flex-col items-center justify-center">
                    <div class="text-7xl mb-6 opacity-80">🏜️</div>
                    <h3 class="text-2xl font-bold text-base-content">No Characters Found</h3>
                    <p class="text-base-content/60 mt-3 max-w-sm mx-auto">This space is looking a little empty. Check back later!</p>
                </div>

                <!-- Load More Button -->
                <div v-if="hasMore && characterList.length > 0" class="flex justify-center pt-8 pb-12">
                    <button @click="fetchCharacters(true)" class="btn btn-outline btn-wide rounded-full font-bold">
                        Load More
                    </button>
                </div>
            </div>

        </div>
    </div>
</template>

<style scoped>
</style>