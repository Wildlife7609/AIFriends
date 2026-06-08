<script setup>
import { useUserStore } from '@/stores/user'
import UserSpaceIcon from './icons/UserSpace.vue'
import UserProfileIcon from './icons/UserProfile.vue'
import UserLogoutIcon from './icons/UserLogout.vue'
const user = useUserStore()

const closeMenu = () => {
    const element = document.activeElement
    if (element && element instanceof HTMLElement) element.blur()
}


</script>



<template>
    <div class="dropdown dropdown-end">
        <div tabindex="0" role="button"
            class="avatar btn btn-circle btn-ghost hover:bg-base-200 transition-colors mr-2 w-10 h-10">
            <div class="w-10 rounded-full ring ring-base-300 ring-offset-base-100 ring-offset-1">
                <img :src="user.photo" />
            </div>
        </div>
        <ul tabindex="-1"
            class="dropdown-content menu bg-base-100/95 backdrop-blur-xl rounded-2xl z-1 w-64 p-2 shadow-2xl mt-4 border border-base-200/50">
            <li class="mb-2">
                <RouterLink @click="closeMenu" :to="{ name: 'user-space', params: { user_id: user.id } }"
                    class="flex items-center gap-3 py-3 px-3 hover:bg-base-200/50 rounded-xl transition-all">
                    <div class="avatar">
                        <div class="w-12 h-12 rounded-full ring-2 ring-primary/40 ring-offset-base-100 ring-offset-2">
                            <img :src="user.photo" alt="" />
                        </div>
                    </div>
                    <div class="flex flex-col justify-center">
                        <span class="text-lg font-bold line-clamp-1 leading-tight">{{ user.username }}</span>
                        <span class="text-xs text-primary font-medium mt-1">{{ user.id }}</span>
                    </div>
                </RouterLink>
            </li>
            <div class="divider my-0 px-2 opacity-50"></div>
            <li class="mt-1">
                <RouterLink @click="closeMenu" :to="{ name: 'user-space', params: { user_id: user.id } }"
                    class="group text-base font-medium py-3 px-3 flex items-center gap-4 hover:bg-primary/10 hover:text-primary rounded-xl transition-colors">
                    <UserSpaceIcon class="w-[22px] h-[22px] opacity-70 group-hover:opacity-100 transition-opacity" />
                    User Space
                </RouterLink>
            </li>
            <li>
                <RouterLink @click="closeMenu" :to="{ name: 'profile' }"
                    class="group text-base font-medium py-3 px-3 flex items-center gap-4 hover:bg-primary/10 hover:text-primary rounded-xl transition-colors">
                    <UserProfileIcon class="w-[22px] h-[22px] opacity-70 group-hover:opacity-100 transition-opacity" />
                    Profile
                </RouterLink>
            </li>
            <div class="divider my-1 px-2 opacity-50"></div>
            <li class="mb-1">
                <a @click="user.logout(); closeMenu()"
                    class="group text-base font-medium py-3 px-3 flex items-center gap-4 text-error hover:bg-error/10 hover:text-error rounded-xl transition-colors">
                    <UserLogoutIcon class="w-[22px] h-[22px] opacity-80 group-hover:opacity-100 transition-opacity" />
                    Logout
                </a>
            </li>
        </ul>
    </div>
</template>

<style scoped></style>