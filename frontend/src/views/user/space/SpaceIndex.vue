<script setup>
import { useRouter, useRoute } from 'vue-router'
const router = useRouter() //use navigate between pages
const route = useRoute() //use current page message

</script>

<template>
    space: {{ $route.params.user_id }}
</template>

<style scoped></style>