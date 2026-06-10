<script setup>
import Username from './components/Username.vue';
import Photo from './components/Photo.vue';
import Profile from './components/Profile.vue';
import { useUserStore } from '@/stores/user'

const user = useUserStore()
</script>

<template>
    <div class="flex justify-center items-start h-full p-6 bg-base-200/30">
        <div
            class="card bg-base-100 shadow-2xl shadow-base-300/50 w-full max-w-4xl border border-base-200/60 mt-8 transition-shadow transition-transform duration-300 hover:shadow-3xl">
            <div class="card-body p-8 sm:p-10">
                <div class="border-b border-base-200 pb-4 mb-8">
                    <h2
                        class="text-3xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">
                        Edit Profile
                    </h2>
                    <p class="text-base-content/60 mt-1">Update your personal information and bio.</p>
                </div>

                <div class="flex flex-col lg:flex-row gap-12">
                    <!-- Left Column: Photo (1/3 width on large screens) -->
                    <div class="flex flex-col items-center lg:w-1/3">
                        <Photo :photo="user.photo"></Photo>
                    </div>

                    <!-- Right Column: Details (2/3 width on large screens) -->
                    <div class="flex flex-col gap-6 lg:w-2/3">
                        <Username :username="user.username"></Username>
                        <Profile :profile="user.profile"></Profile>

                        <div class="card-actions justify-end mt-4 pt-6 border-t border-base-200">
                            <button class="btn btn-ghost hover:bg-base-200 transition-transform">Cancel</button>
                            <button
                                class="btn btn-primary px-8 shadow-lg shadow-primary/30 hover:scale-[1.02] transition-transform">
                                Save Changes
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>