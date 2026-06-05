<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import NavBar from './components/navbar/NavBar.vue'

const route = useRoute()
const isPlainLayout = computed(() => route.meta.layout === 'plain')
</script>

<template>
  <!-- Login / Register: no navbar, full-screen -->
  <router-view v-if="isPlainLayout" />

  <!-- All other pages: wrapped in NavBar layout -->
  <NavBar v-else>
    <router-view />
  </NavBar>
</template>

<style scoped></style>
