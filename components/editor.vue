<template>
  <div class="w-full relative">
    <div @click="editCamera=true"
         class="border-2 bg-gray-200 rounded-lg w-5/6 h-16 shadow-md text-center mx-auto pt-5 cursor-pointer hover:bg-gray-300"> 
      <h2> Edit camera parameters </h2>
    </div>
    <div v-if="editCamera" class="edit-params-cont"> </div>
    <div v-if="editCamera" 
         class="absolute left-0 right-0 mx-auto w-5/6 py-10 bg-gray-100 rounded-lg shadow-lg text-center z-50">
      <div>
        <h2 class="mb-5"> Enter camera parameters </h2>
        <h3 class="pb-3"> Resolution (px) </h3>
        </ul> 
          <li> x: <input class="input" v-model="camera.x"/> </li>
          <li> y: <input class="input" v-model="camera.y"/> </li>
        </ul>
        <h3 class="pt-5 pb-2"> Field of view </h3> 
        <p class="mb-3">Enter the fields of view in degrees:</p>
        <ul>
          <li> FOV x: <input class="input" v-model="camera.fov[0]"/> </li>
          <li> FOV y: <input class="input" v-model="camera.fov[1]"/> </li>
        </ul>
      </div>
      <button class="bg-gray-100 mt-32 text-base font-medium border-2 border-blue-500 
                     text-blue-500 rounded-md w-40 h-12
                     hover:font-bold hover:shadow-md"
              @click="stopEditingCamera()">
        Done
      </button>
    </div>
    <div class="w-5/6 shadow-lg rounded-md mx-auto text-center mt-8 border-2 pb-20 pt-8">
      <h2> Orientation of the camera </h2>
      <p class="mt-3"> Euler angles in  degrees </p>
      <ul class="mt-2">
        <li> Roll (x): <input class="input-lg" v-model="orientation[0]"/></li>
        <li> Pich (y): <input class="input-lg" v-model="orientation[1]"/></li>
        <li> Yaw (z): <input class="input-lg" v-model="orientation[2]"/></li>
      </ul> 
      <div class="w-3/4 mx-auto text-center mt-4">
        <p> x axis rotation (roll): </p>
        <vue-slider :lazy="true" :min="0" :max="365"
                    v-model="orientation[0]"></vue-slider>
      </div>
      <div class="w-3/4 mx-auto text-center">
        <p> y axis rotation (pitch): </p>
        <vue-slider :lazy="true" :min="0" :max="365"
                    v-model="orientation[1]"></vue-slider>
      </div>
      <div class="w-3/4 mx-auto text-center">
        <p> z axis rotation (yaw): </p>
        <vue-slider :lazy="true" :min="0" :max="365"
                    v-model="orientation[2]"></vue-slider>
      </div>
      <h2 class="mt-6"> Filter's prefered axis </h2>
      <p class="mt-3"> Euler angles in  degrees </p>
      <ul class="mt-2">
        <li> Roll (x): <input class="input-lg" v-model="axis[0]"/></li>
        <li> Pitch (y): <input class="input-lg" v-model="axis[1]"/></li>
        <li> Yaw (z): <input class="input-lg" v-model="axis[2]"/></li>
      </ul>
      <div class="w-3/4 mx-auto text-center mt-4">
        <p> x axis rotation (roll): </p>
        <vue-slider :lazy="true" :min="0" :max="365"
                    v-model="axis[0]"></vue-slider>
      </div>
      <div class="w-3/4 mx-auto text-center">
        <p> y axis rotation (pitch): </p>
        <vue-slider :lazy="true" :min="0" :max="365"
                    v-model="axis[1]"></vue-slider>
      </div>
      <div class="w-3/4 mx-auto text-center">
        <p> z axis rotation (yaw): </p>
        <vue-slider :lazy="true" :min="0" :max="365"
                    v-model="axis[2]"></vue-slider>
      </div>
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
    },
    orientation: {
      required: true
    },
    axis: {
      required: true
    }
  },
  
  methods: {
    updatePlot() {
      this.$emit('updatePlot')
    },

    stopEditingCamera() {
      this.editCamera = false
      this.updatePlot()
    }
  },

}
</script>

<style scoped>

.edit-params-cont {
  @apply absolute bg-gray-800 opacity-75 w-11/12 left-0 right-0 mx-auto top-0 z-40 rounded-lg shadow-xl;
  height: calc(95vh - 86px)
}

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