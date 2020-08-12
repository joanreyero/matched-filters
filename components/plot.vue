<template>
  <div class="w-11/12 mx-auto max-w-3xl">
    <img :src="src" class="rounded-lg mx-auto shadow-lg w-full"/>
  </div>
</template>

<script>
export default {
  props: {
    src: {
      required: true
    }
  },
}
</script>

<style>

</style>