<template>
  <div class="body-logo">
        <div class="stroke-text">Winter Sales</div>
        <div class="shadow-text">Winter Sales</div>
      </div>
</template>

<script>
export default {
    name:"BodyLogo",
}
</script>

<style>
.body-logo{
    flex: 0 0 37.7vh;
}
.stroke-text {
  margin-left: 15vw;
  font-size: calc(10vw + 5vh);
  color: #8194fa;
  -webkit-text-stroke: 2vw white;
  paint-order: stroke fill;
  position: absolute;
  z-index: 2;
  white-space: nowrap;
}

.shadow-text {
  margin-left: 15vw;
  font-size: calc(10vw + 5vh);
  color: #8194fa;
  text-shadow: 0.125em 0.15em 0.05em rgba(0, 0, 0, 0.6);
  position: absolute;
  z-index: 1;
  white-space: nowrap;
}
</style>