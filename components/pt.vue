<template>
  <div ref="mine">
    <vue-plotly :data="plotData" :layout="layout"/>
  </div>
</template>

<script>


export default {
  props: {
    axis: {
      type: Array,
      required: false,
      default: [0, 0.5, 0.5]
    }
  },

  data: function() {
    return {
      plotData:[{
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
        x: [0, this.axis[0]],
        y: [0, this.axis[1]],
        z: [0, this.axis[2]],
        name: 'Filter axis',
        textposition: ["top right"],
        texttemplate: ['', 'PDA'],
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
      }],

      layout: {
        autosize: true,
        height: 800,
        scene: {
          domain: {
            x: [-1, 1],
            y: [-1, 1],
            z: [-1, 1]
          },
          camera: {
            eye: {
              x: 1.5,
              y: 1.5,
              z: 1.5,
            },
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