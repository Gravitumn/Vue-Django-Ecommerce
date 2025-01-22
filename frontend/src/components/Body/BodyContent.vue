<template>
  <div class="homepage-body">
    <background />
    <div class="content-overlay" @scroll="handleScroll">
      <div class="body-content">
        <div class="scrollable">
          <body-logo />
          <catalog />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Background from "./Background.vue";
import BodyLogo from "./BodyLogo.vue";
import Catalog from "./AdCatalog.vue";
export default {
  name: "BodyContent",
  components: {
    Background,
    BodyLogo,
    Catalog,
  },
};
</script>

<style>
.homepage-body {
  position: relative;
  top: 10.6vh;
  left: 0;
  width: 100vw;
  height: 100vh;
}
.content-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2;
  pointer-events: auto;
}
.body-content {
  position: fixed;
  top: 16.6vh;
  left: 0;
  width: 100vw;
  height: 82.54vh;
  overflow-y: auto;
}
.scrollable {
  display: flex;
  flex-direction: column;
  width: 100%;
  height:100%;
}
</style>