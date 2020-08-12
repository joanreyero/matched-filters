<template>
  <div class="w-screen h-screen overflow-hidden bg-gray-300 p-10">
    <matrix :show="showMatrix" :filter="filter" @hideMatrix="hideMatrix()"/>
    <div class="main block lg:hidden text-center py-24">
      <p class="text-lg"> Currently the application is only supported on computer screens. </p>
    </div>
    <div class="main hidden lg:flex text-center flex-wrap">
      <h1 class="w-full pt-10"> Matched Filter Generator </h1>
      <div class="panel overflow-scroll">
        <editor @updatePlot="getPlot()" :camera="camera"/>
      </div>
      <div class="panel">
        <plot :src="plot"/>
        <div class="w-full pt-10 text-center">
          <button class="bg-blue-500 text-base font-medium border-2 border-gray-100 
                         text-gray-100 rounded-md w-48 h-16
                         hover:border-blue-500 hover:font-bold hover:shadow-md"
                  @click="getFilter()">
            Get matrix
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      plot: '',
      filter: 'Loading',
      camera: {
        x: 640,
        y: 360,
        fovType: 'K',
        fov: ['205.46963709898583', '0.0', '320.5',
              '0.0', '205.46963709898583', '180.5',
              '0.0', '0.0', '1.0'],
        orientation: ['0.0', '0.0', '0.0'],
        axis: ['1.0', '0.0', '0.0']
      },
      showMatrix: false
    }
  },

  methods: {    
    getPlot() {
    let _vm = this;
     this.$axios.get('/plot', {responseType: 'blob', params: this.camera})
        .then(function(response) {
          let plot = response.data[0];
          console.log(response.data)
          let matrix = response.data[1];
          let threeD = response.data[2];
          //_vm.plot = response.data
          let reader = new FileReader();
          reader.readAsDataURL(new Blob([response.data])); 
          reader.onload = () => {
            _vm.plot = reader.result;
          }
        });
    },

    hideMatrix() {
      this.showMatrix = false;
      this.filter = 'Loading'
    },

    getFilter() {
      this.showMatrix = true
      let _vm = this;
      this.$axios.get('/matched_filter', {params: this.camera})
        .then(function(response) {
          _vm.filter = response.data
        });
    }
  },

  mounted() {
    this.getPlot()
  }
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