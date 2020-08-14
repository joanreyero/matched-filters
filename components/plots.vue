<template>
  <div>
    <div class="border-2 bg-gray-200 rounded-lg w-5/6 h-16 shadow-md flex
                mx-auto"> 
      <div class="w-1/2 pt-0 rounded-lg h-16 text-center hover:bg-gray-300"
           :class="{active: active == 'pos'}">
        <button class="w-full pt-0 h-16 cursor-pointer focus:outline-none"
                @click="changeActive('pos')"> 
          <h2> Positions </h2> 
        </button>
      </div>
      <div class="w-1/2 pt-0 rounded-lg h-16 text-center hover:bg-gray-300"
           :class="{active: active == 'plot'}">
        <button class="w-full pt-0 h-16 cursor-pointer focus:outline-none"
                @click="changeActive('plot')"> 
          <h2> Filter </h2> 
        </button>
      </div>
    </div>
    <div class="w-11/12 mx-auto max-w-3xl pt-8">
      <img :src="src" class="rounded-lg mx-auto shadow-lg border-gray-300 border w-full"/>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    src: {
      required: true
    },
    active: {
      required: true
    }
  },

  methods: {
    changeActive(n) {
      if (n != this.active) {
        this.$emit('changeActive', n)
      }
    }
  }
}
</script>

<style>

.active {
  @apply bg-gray-500 text-gray-100 pointer-events-none;
}

</style>