<template>
  <div class="w-11/12 mx-auto max-w-3xl">
    <img :src="plot" class="rounded-lg mx-auto shadow-lg w-full"/>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      plot: '' 
    }
  },

  mounted() {
    let _vm = this;
     this.$axios.get('/plot', {responseType: 'blob'})
         .then(function(response) {
           //_vm.plot = response.data
           let reader = new FileReader();
            reader.readAsDataURL(new Blob([response.data])); 
            reader.onload = () => {
              _vm.plot = reader.result;
            }
         });
  }
}
</script>

<style>

</style>