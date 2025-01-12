<template>
  <div class="home-page" @click.stop>
    <div ref="sidebarRef" class="sidebar-container">
      <sidebar v-if="showSidebar" />
    </div>
    
    <main-nav-bar />
    <sub-navbar v-model:showSidebar="showSidebar"/>
    <body-content />
  </div>
</template>

<script>
import MainNavBar from "../components/Navbar/MainNavbar.vue";
import BodyContent from "../components/Body/BodyContent.vue";
import SubNavbar from "../components/SubNavbar/SubNavbar.vue";
import Sidebar from "../components/SubNavbar/Sidebar.vue";
import { ref } from "vue";
import { onClickOutside } from "@vueuse/core";
export default {
  components: {
    MainNavBar,
    SubNavbar,
    BodyContent,
    Sidebar,
  },
  setup() {
    const showSidebar = ref(false);

    const sidebarRef = ref(null);

    // Detect clicks outside the sidebar
    onClickOutside(sidebarRef, () => {
      console.log(sidebarRef)
      if (showSidebar.value) {
        showSidebar.value = false;
      }
    });

    return {
      showSidebar,
      sidebarRef,
    };
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Madimi+One&display=swap");
.home-page {
  width: 100vw;
  height: 100vh;
  font-family: "Madimi One";
}
.sidebar-container{
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
  widows: 26.15vw;
  z-index: 1100;
}
</style>