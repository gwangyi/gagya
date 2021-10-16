<template>
  <svg
    class="cell"
    :class="{ grey: type === 'grey', transparent: type === 'transparent' }"
    viewBox="0 0 10 10"
  >
    <rect
      x="0"
      y="0"
      width="10"
      height="10"
      fill="transparent"
      style="stroke: rgb(0, 0, 0); stroke-width: 1px"
      vector-effect="non-scaling-stroke"
    />
    <line
      x1="5"
      y1="0"
      x2="5"
      y2="10"
      style="stroke: rgb(192, 192, 192); stroke-width: 1px"
      vector-effect="non-scaling-stroke"
    />
    <line
      x1="0"
      y1="5"
      x2="10"
      y2="5"
      style="stroke: rgb(192, 192, 192); stroke-width: 1px"
      vector-effect="non-scaling-stroke"
    />
    <line
      x1="5"
      y1="0"
      x2="5"
      y2="10"
      style="stroke: rgb(192, 192, 192); stroke-width: 1px"
      vector-effect="non-scaling-stroke"
    />
    <text x="50%" y="50%" text-anchor="middle" dominant-baseline="central">
      {{ cell }}
    </text>
  </svg>
</template>

<script lang="ts">
import { Component, Vue, Prop } from "vue-property-decorator";

@Component
export default class WriteCell extends Vue {
  @Prop(String)
  private cell!: string;

  @Prop({ default: "" })
  private type!: string;
}
</script>

<style scoped>
svg.cell {
  margin: 0 -1px -1px 0;
}
svg.cell text {
  font-family: "Nanum Gothic";
  font-weight: 700;
  font-size: 8px;
}

.grey text {
  fill: #ccc;
}

.transparent text {
  fill: transparent;
}
</style>
