<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import Menu from './icons/Menu.vue'
import Home from './icons/Homepage.vue'
import Friends from './icons/Friends.vue'
import Create from './icons/Create.vue'
import UserProfile from './icons/UserProfile.vue'
import UserSpace from './icons/UserSpace.vue'
import UserLogout from './icons/UserLogout.vue'
import Search from './icons/Search.vue'
import UserMenu from './UserMenu.vue'

const user = useUserStore()
const router = useRouter()

// Gorgeous DaisyUI themes
const themes = [
    'light',
    'dark',
    'cupcake',
    'synthwave',
    'valentine',
    'forest',
    'aqua',
    'nord',
    'sunset',
    'dim',
    'dracula',
]

const currentTheme = ref(localStorage.getItem('theme') || 'light')

const changeTheme = (theme) => {
    currentTheme.value = theme
    localStorage.setItem('theme', theme)
    document.documentElement.setAttribute('data-theme', theme)
}

onMounted(() => {
    document.documentElement.setAttribute('data-theme', currentTheme.value)
})
</script>

<template>
    <div class="drawer lg:drawer-open">
        <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
        <div class="drawer-content flex flex-col min-h-screen">
            <!-- Navbar -->
            <nav
                class="navbar sticky top-0 z-45 w-full bg-base-100/80 backdrop-blur-md border-b border-base-300 shadow-sm px-4 transition-all duration-300">
                <div class="navbar-start">
                    <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost">
                        <!-- Sidebar toggle icon -->
                        <Menu />
                    </label>
                    <div
                        class="px-2 font-black text-2xl bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent tracking-tight">
                        AIFriends</div>
                </div>
                <div class="navbar-center w-4/5 max-w-180 flex justify-center">
                    <div class="join w-4/5 flex justify-center items-center">
                        <input
                            class="input input-bordered input-secondary join-item w-full rounded-l-full gap-0 focus:outline-none focus:border-secondary transition-all"
                            placeholder="Search friends or posts..." />
                        <button
                            class="btn btn-secondary join-item rounded-r-full hover:scale-[1.02] active:scale-[0.98] transition-all">
                            <Search />
                            Search
                        </button>
                    </div>
                </div>

                <div class="navbar-end gap-1">
                    <!-- Dynamic Theme Selector -->
                    <div class="dropdown dropdown-end">
                        <div tabindex="0" role="button" class="btn btn-square btn-ghost tooltip tooltip-bottom"
                            data-tip="Change Theme">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.8"
                                stroke="currentColor" class="size-5">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M4.098 19.902a3.75 3.75 0 0 0 5.304 0l6.401-6.402M10.9 10.9l.006-.006a3.75 3.75 0 1 1-5.303-5.303L12 12M15.293 15.293l4.607 4.607a1 1 0 0 0 1.414-1.414l-4.607-4.607m-1.414 1.414a2.25 2.25 0 1 1 3.182-3.182l-3.182 3.182Z" />
                            </svg>
                        </div>
                        <ul tabindex="0"
                            class="dropdown-content menu bg-base-200 rounded-box z-50 w-52 p-2 shadow-2xl max-h-80 overflow-y-auto border border-base-300">
                            <li v-for="t in themes" :key="t">
                                <button :class="{ 'bg-primary text-primary-content': currentTheme === t }"
                                    @click="changeTheme(t)" class="capitalize justify-between">
                                    {{ t }}
                                    <span v-if="currentTheme === t" class="text-xs">✓</span>
                                </button>
                            </li>
                        </ul>
                    </div>

                    <!-- Show skeleton while pulling user info -->
                    <template v-if="!user.hasPulledUserInfo">
                        <div class="flex items-center">
                            <!-- Skeleton for Create button -->
                            <div class="skeleton w-24 h-10 rounded-xl shrink-0 mr-4"></div>
                            <!-- Skeleton for Avatar -->
                            <div class="skeleton w-10 h-10 rounded-full shrink-0 mr-2"></div>
                        </div>
                    </template>

                    <!-- Show Login button when not logged in -->
                    <template v-else-if="!user.isLogin()">
                        <RouterLink :to="{ name: 'login' }"
                            class="btn btn-primary rounded-full px-5 font-semibold hover:scale-[1.03] active:scale-[0.97] transition-all duration-200">
                            Login
                        </RouterLink>
                    </template>

                    <!-- Show user action buttons when logged in -->
                    <template v-else-if="user.isLogin()">
                        <RouterLink :to="{ name: 'create' }"
                            class="btn btn-ghost hover:text-primary transition-colors tooltip tooltip-bottom mr-2"
                            data-tip="Create Post" exact-active-class="btn-active text-primary">
                            <Create />
                            <span class="font-semibold">Create</span>
                        </RouterLink>
                        <UserMenu></UserMenu>
                    </template>
                </div>
            </nav>
            <!-- Page content here -->
            <div class="grow">
                <slot></slot>
            </div>
        </div>

        <div class="drawer-side is-drawer-close:overflow-visible z-50">
            <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
            <div
                class="flex min-h-full flex-col items-start bg-base-200 border-r border-base-300 is-drawer-close:w-14 is-drawer-open:w-64 transition-all duration-300">
                <!-- Sidebar content here -->
                <ul class="menu w-full grow p-2 gap-1">
                    <!-- List item -->
                    <li>
                        <RouterLink :to="{ name: 'homepage' }"
                            class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3 rounded-xl hover:bg-primary hover:text-primary-content transition-all duration-200"
                            active-class="bg-base-300 text-base-content font-bold" data-tip="Homepage">
                            <Home />
                            <span class="is-drawer-close:hidden text-base font-medium whitespace-nowrap">Homepage</span>
                        </RouterLink>
                    </li>

                    <li>
                        <RouterLink :to="{ name: 'friend' }"
                            class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3 rounded-xl hover:bg-primary hover:text-primary-content transition-all duration-200"
                            active-class="bg-base-300 text-base-content font-bold" data-tip="Friends">
                            <Friends />
                            <span class="is-drawer-close:hidden text-base font-medium whitespace-nowrap">Friends</span>
                        </RouterLink>
                    </li>

                    <li>
                        <RouterLink :to="{ name: 'create' }"
                            class="is-drawer-close:tooltip is-drawer-close:tooltip-right py-3 rounded-xl hover:bg-primary hover:text-primary-content transition-all duration-200"
                            active-class="bg-base-300 text-base-content font-bold" data-tip="Create">
                            <Create />
                            <span class="is-drawer-close:hidden text-base font-medium whitespace-nowrap">Create</span>
                        </RouterLink>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
