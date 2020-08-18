<template>
  <div ref="mine">
    <vue-plotly :data="plotData" :layout="layout"/>
  </div>
</template>

<script>


export default {
  props: {
    directions: {
      type: Object,
      required: true,
    }
  },

  computed: {
    plotData () {
      return[{
        x: [0, 0.5],
        y: [0, 0],
        z: [0, 0],
        textposition: ["top right"],
        texttemplate: ['', 'x'],
        type:"scatter3d",
        mode: 'lines+markers+text',
        hoverinfo: 'none',
        showlegend: false,
        line: {
          width: 3,
          color: ['black']
        },
        marker: {
          size: 2,
          color: ['transparent',],
          symbol: 'diamond',
        }
      },
      {
        x: [0, 0],
        y: [0, 0.5],
        z: [0, 0],
        textposition: ["top right"],
        texttemplate: ['', 'y'],
        type:"scatter3d",
        mode: 'lines+markers+text',
        hoverinfo: 'none',
        showlegend: false,
        line: {
          width: 3,
        color: ['black']},
        marker: {
          size: 2,
          color: ['transparent',],
          symbol: 'diamond',
        }
      },
      {
        x: [0, 0],
        y: [0, 0],
        z: [0, 0.5],
        textposition: ["top right"],
        texttemplate: ['', 'z'],
        type:"scatter3d",
        mode: 'lines+markers+text',
        hoverinfo: 'none',
        showlegend: false,
        line: {
          width: 3,
          color: ['black']},
        marker: {
          size: 2,
          color: ['transparent',],
          symbol: 'diamond',
        }
      },
      // PDA
      {
        x: [0, this.directions.axis[0]],
        y: [0, this.directions.axis[1]],
        z: [0, this.directions.axis[2]],
        name: 'Filter axis',
        textposition: ["top right"],
        texttemplate: ['', 'PDA'],
        type:"scatter3d",
        mode: 'lines+markers+text',
        line: {
          width: 5,
          color: 'orange'},
        marker: {
          size: 4,
          color: ['transparent','gray'],
          symbol: 'diamond',
        }
      },
      // Camera x
      {
        x: [0, this.directions.camx[0]],
        y: [0, this.directions.camx[1]],
        z: [0, this.directions.camx[2]],
        name: 'Camera x',
        textposition: ["top right"],
        texttemplate: ['', 'cam x'],
        type:"scatter3d",
        mode: 'lines+markers+text',
        line: {
          width: 5,
          color: 'blue'},
        marker: {
          size: 4,
          color: ['transparent','blue'],
          symbol: 'diamond',
        }
      },
      // Camera y
      {
        x: [0, this.directions.camy[0]],
        y: [0, this.directions.camy[1]],
        z: [0, this.directions.camy[2]],
        name: 'Camera y',
        textposition: ["top right"],
        texttemplate: ['', 'cam y'],
        type:"scatter3d",
        mode: 'lines+markers+text',
        line: {
          width: 5,
          color: 'green'},
        marker: {
          size: 4,
          color: ['transparent','green'],
          symbol: 'diamond',
        }
      },
      {
        x: [0, this.directions.camz[0]],
        y: [0, this.directions.camz[1]],
        z: [0, this.directions.camz[2]],
        name: 'Camera z',
        textposition: ["top right"],
        texttemplate: ['', 'cam z'],
        type:"scatter3d",
        mode: 'lines+markers+text',
        line: {
          width: 5,
          color: 'red'},
        marker: {
          size: 4,
          color: ['transparent','red'],
          symbol: 'diamond',
        }
      }]
    },

    layout() {
      return {
        autosize: true,
        height: 800,
        scene: {
          
          camera: {
            // eye: {
            //   x: 1.5,
            //   y: 1.5,
            //   z: 1.5,
            // },
            center: {
              x: 0,
              y: 0,
              z: 0
            }
          },
          xaxis: {
            visible: false,
          },
          yaxis: {
            visible: false,
          },
          zaxis: {
            visible: false,
          },
        }
      }
    }
  }
}
</script>

<style>
.modebar{
      display: none !important;
}

</style>