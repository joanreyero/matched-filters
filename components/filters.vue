<template>
  <div class="w-screen h-screen overflow-hidden bg-gray-100 p-0">
    <matrix :show="showMatrix" :filter="filter" @hideMatrix="hideMatrix()"/>
    <div class="main block lg:hidden text-center py-24">
      <p class="text-lg"> Currently the application is only supported on computer screens. </p>
    </div>
    <div class="main hidden lg:flex text-center flex-wrap">
      <h1 class="w-full pt-8"> Matched Filter Generator </h1>
      <div class="panel">
        <editor @updatePlot="updatePlot()" 
                :camera="camera" :orientation="orientation" :axis="axis"/>
      </div>
      <div class="panel">
        <plots :loading="loading" :active="activePlot" :src="plot" :directions="directions" 
               @changeActive="changeActive"/>
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
        fov: ['90', '45']
      },
      orientation: ['0.0', '0.0', '0.0'],
      axis: ['0.0', '0.0', '0.0'],
      showMatrix: false,
      activePlot: 'pos',
      directions: {
        camx: [0, 0, 0],
        camy: [0, 0, 0],
        camz: [0, 0, 0],
        axis: [0, 0, 0]
      },
      loading: false,
      nextUp: false
    }
  },

  methods: {    

    updatePlot() {
      let camera = this.camera;
      camera.orientation = this.orientation;
      camera.axis = this.axis;
      let url = this.activePlot == 'pos' ? '/pos' : '/plot';
      if (this.loading) {

        this.nextUp = {camera: camera, url: url}
      }
      else {
        this.loading = true;
        this.getPlot(camera, url)
      }
    },

    getPlot(camera, url) {
      let _vm = this;
      if (url == '/plot') {
        this.$axios.get(url, {responseType: 'blob', params: camera})
          .then(function(response) {
            let reader = new FileReader();
            reader.readAsDataURL(new Blob([response.data]));
            
            reader.onload = () => {
              if (!(_vm.nextUp)) {
                _vm.plot = reader.result;
                _vm.loading = false
              }
              else {
                let camera = _vm.nextUp.camera
                let url = _vm.nextUp.url
                _vm.nextUp = false
                _vm.getPlot(camera, url)
              }
            }
          });
      }
      else {
        this.$axios.get(url, {params: camera})
          .then(function(response) {
            _vm.directions = response.data
            _vm.loading = false
          });
      }
    },

    changeActive(n) {
      this.activePlot = n
      this.updatePlot()
    },

    hideMatrix() {
      this.showMatrix = false;
      this.filter = 'Loading'
    },

    getFilter() {
      let camera = this.camera;
      camera.orientation = this.orientation;
      camera.axis = this.axis;
      this.showMatrix = true
      let _vm = this;
      this.$axios.get('/matched_filter', {params: camera})
        .then(function(response) {
          _vm.filter = response.data
        });
    }
  },

  mounted() {
    this.updatePlot()
    //this.getPos()
  },

  watch: {
    orientation() {
      this.updatePlot()
    },

    axis() {
      this.updatePlot()
    }
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
    @apply w-1/2 py-8 overflow-scroll;
    height: calc(100vh - 86px)
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