<template>
  <div v-if="show" class="fixed top-0 w-screen h-screen left-0 rounded-lg bg-gray-100 z-50">
    <div class="fixed bottom-0 w-screen h-20 text-center">
      <button class="bg-blue-500 text-base font-medium border-2 border-gray-100 
                         text-gray-100 rounded-md w-48 h-16 mt-2
                         hover:border-blue-500 hover:font-bold hover:shadow-md"
                  @click="hideMatrix()">
        Done
      </button>
    </div>
    <div class="matrix-container">
      Three dimensional matrix with 2 slices. 
      Slices are marked by: <span class="font-mono"> Slice {0 or 1} </span>. <br/>
      Can be imported into <span class="font-mono"> numpy </span> with 
      <a href="https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html"> the 
      <span class="font-mono"> loadtxt </span> function</a>.  <i> (not tested) </i>. <br/> 
      Otherwise use <a href="https://github.com/joanreyero/matched-filters/blob/master/matched-filters/matchedFilters.py"> this script </a> to generate the matrix. 
      <div class="font-mono w-full bg-gray-600 text-gray-100 mt-5">
        {{filter}}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    filter: {
      required: true,
      type: String
    },
    show: {
      required: true,
      type: Boolean
    }
  },

  methods: {
    hideMatrix() {
      this.$emit('hideMatrix')
    }
  }

}
</script>

<style>

.matrix-container {
  @apply text-center px-5 py-2;
  height: calc(100vh - 5rem);
  overflow-x: hidden;
  overflow-y: scroll;
}

</style>