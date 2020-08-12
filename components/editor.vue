<template>
  <div class="w-full relative">
    <div @click="editCamera=true"
         class="border-2 bg-gray-200 rounded-lg w-5/6 h-16 shadow-md text-center 
                mx-auto pt-5 cursor-pointer hover:bg-gray-300"> 
      <h2> Edit camera parameters </h2>
    </div>
    <div v-if="editCamera" 
         class="absolute left-0 right-0 top-0 mx-auto w-5/6 py-10 bg-gray-100 rounded-lg shadow-lg text-center z-50"
         style="height: 600px"> 
      <div>
        <h3 class="pb-3"> Resolution (px) </h3>
        </ul> 
          <li> x: <input class="input" v-model="camera.x"/> </li>
          <li> y: <input class="input" v-model="camera.y"/> </li>
        </ul>
        <h3 class="pt-5 pb-2"> Field of view </h3>
        <p class="font-medium"> Choose the input type </p>
        <div class="rounded-sm border-2 bg-gray-200 w-5/6 max-w-lg mx-auto mt-2 mb-4 flex items-center">
          <button @click="camera.fovType = 'K'"
                  class="w-1/2 block border-r-2 h-10 focus:outline-none
                         hover:bg-gray-300 hover:font-medium"
                  :class="{active: camera.fovType == 'K'}"> 
            Intrinsic Matrix 
          </button>
          <button @click="camera.fovType = 'fov'"
                  class="w-1/2 block h-10 focus:outline-none
                         hover:bg-gray-300 hover:font-medium"
                  :class="{active: camera.fovType == 'fov'}"> 
            Field of View 
          </button>
        </div>
      </div>
      <div v-if="camera.fovType == 'K'" class="w-full">
        <p class="mb-3"> Enter the Intrinsic Matrix: </p>
        <div class="matrix-row">
          <input class="matrix border-l-2 border-t-2 border-b" 
                 v-model="camera.fov[0]"/>
          <input class="matrix border-t-2 border-b border-l border-r" 
                 v-model="camera.fov[1]"/>
          <input class="matrix border-r-2 border-t-2 border-b" 
                 v-model="camera.fov[2]"/>
        </div>
        <div class="matrix-row">
          <input class="matrix border-l-2 border-b" 
                 v-model="camera.fov[3]"/>
          <input class="matrix border-b border-l border-r" 
                 v-model="camera.fov[4]"/>
          <input class="matrix border-r-2 border-b" 
                 v-model="camera.fov[5]"/>
        </div>
        <div class="matrix-row">
          <input class="matrix border-l-2 border-b-2" 
                 v-model="camera.fov[6]"/>
          <input class="matrix border-b-2 border-l border-r" 
                 v-model="camera.fov[7]"/>
          <input class="matrix border-r-2 border-b-2" 
                 v-model="camera.fov[8]"/>
        </div>
      </div>
      <div v-else class="w-full">
        <p class="mb-3">Enter the fields of view:</p>
        <ul>
          <li> FOV x: <input class="input" v-model="camera.fov[0]"/> </li>
          <li> FOV y: <input class="input" v-model="camera.fov[1]"/> </li>
        </ul>
      </div>
      <button class="bg-gray-100 mt-32 text-base font-medium border-2 border-blue-500 
                     text-blue-500 rounded-md w-40 h-12
                     hover:font-bold hover:shadow-md"
              @click="editCamera=false">
        Done
      </button>
    </div>
    <div class="w-5/6 shadow-lg rounded-md mx-auto text-center mt-8 border-2 pb-20 pt-8"
         style="height:500px">
      <h2> Orientation of the camera </h2>
      <p class="mt-3"> Respect to the world, and in  degrees </p>
      <ul class="mt-2">
        <li> Yaw: <input class="input-lg" v-model="camera.orientation[0]"/></li>
        <li> Pich: <input class="input-lg" v-model="camera.orientation[1]"/></li>
        <li> Roll: <input class="input-lg" v-model="camera.orientation[2]"/></li>
      </ul> 
      <h2 class="mt-6"> Filter's prefered axis </h2>
      <p class="mt-3"> A vector in world coordinate frame </p>
      <ul class="mt-2">
        <li> x: <input class="input-lg" v-model="camera.axis[0]"/></li>
        <li> y: <input class="input-lg" v-model="camera.axis[1]"/></li>
        <li> z: <input class="input-lg" v-model="camera.axis[2]"/></li>
      </ul> 

      <button class="absolute left-0 right-0 mx-auto bg-gray-100 mt-8 text-base 
                     font-medium border-2 border-blue-500 
                     text-blue-500 rounded-md w-48 h-16
                     hover:font-bold hover:shadow-md z-30"
              style="bottom: 25px"
              @click="updatePlot()">
        Plot
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      editCamera: false,
    }
  },

  props: {
    camera: {
      required: true
    }
  },
  
  methods: {
    updatePlot() {
      this.$emit('updatePlot')
    }
  }
}
</script>

<style scoped>

input:focus {
  outline: none;
}

input {
  @apply w-24 pl-2
}

.input {
  @apply border border-gray-300 rounded-md
}

.input-lg {
  @apply border border-gray-300 rounded-md w-32
}

.matrix {
  @apply block rounded-none border-gray-400
}

.matrix-row {
  @apply flex mx-auto items-center text-center;
  width: 18rem;
}

.active {
  @apply bg-gray-600 text-gray-100 font-medium
}

</style>