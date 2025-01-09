<template>
  <div class="image">
  </div>
</template>

<script>
export default {
  name: "Background",
};
</script>

<style>
.image {
  position: fixed;
  top: 16.6vh;
  left: 0;
  width: 100vw;
  height: 100vh;

  background-image: url("../assets/Winter_Wallpaper.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>