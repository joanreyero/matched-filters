<template>
<button class="bg-blue-500 text-base font-medium border-2 border-gray-100 text-gray-100 rounded-md w-40 h-12
               hover:border-blue-500 hover:font-bold"
        :class="{primary: primary}"
        @click="clicked()">
  <slot/> 
</button>
</template>

<script>
export default {
  props: {
    primary: {
      required: false,
      default: false
    }
  },
  methods: {
    clicked() {
      this.$emit('click');
    }
  }
}
</script>

<style>
  .primary {
    @apply w-48 h-16
  }
  
</style>
