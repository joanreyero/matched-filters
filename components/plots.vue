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
    <div class="w-11/12 mx-auto max-w-3xl pt-8 text-center">
      <!-- <img :src="src" class="rounded-lg mx-auto shadow-lg border-gray-300 border w-full"/> -->
      <pt/>
      <p v-if="loading" class="loading mx-auto"> Loading </p>
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
    },
    loading: {
      required: false,
      type: Boolean,
      default: false
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

.loading {
  @apply opacity-75 w-1/2 px-10 pt-6 mt-6 bg-gray-600 text-gray-100 rounded-lg shadow-md h-20;
}

.active {
  @apply bg-gray-500 text-gray-100 pointer-events-none;
}

</style>