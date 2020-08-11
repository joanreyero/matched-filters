<template>
  <div class="w-screen h-screen bg-gray-300 p-10">
    <div class="main block lg:hidden text-center py-24">
      <p class="text-lg"> Currently the application is only supported on computer screens. </p>
    </div>
    <div class="main hidden lg:flex text-center flex-wrap">
      <h1 class="w-full pt-10"> Matched Filter Generator </h1>
      <div class="panel overflow-scroll">
        <editor/>
      </div>
      <div class="panel">
        <plot/>
        <div class="w-full pt-10 text-center">
          <button class="bg-blue-500 text-base font-medium border-2 border-gray-100 
                         text-gray-100 rounded-md w-48 h-16
                         hover:border-blue-500 hover:font-bold hover:shadow-md">
            Get matrix
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

  .panel::-webkit-scrollbar {
    display: none;
  }
  .panel {
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
  }

  .main{
    @apply bg-gray-100 rounded-lg shadow-xl w-full h-full;
  }

  .panel {
    @apply w-1/2 h-full pt-16;
  }

  h1 {
    @apply font-semibold text-4xl font-serif;
  }

  h2 {
    @apply text-xl font-serif font-bold;
  }

  h3 {
    @apply text-lg font-semibold font-serif;
  }
</style>