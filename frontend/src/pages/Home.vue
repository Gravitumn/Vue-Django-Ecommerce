<template>
  <div class="home-page">
    <div ref="sidebarRef" class="sidebar-container">
      <sidebar v-if="showSidebar" />
    </div>
    
    <main-nav-bar :user="authStore.user" :isAuthenticated="authStore.isAuthenticated" @logout="logout" />
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
import { useAuthStore } from "../store/auth.js";
import { useRouter } from "vue-router";
export default {
  components: {
    MainNavBar,
    SubNavbar,
    BodyContent,
    Sidebar,
  },
  setup() {
    const showSidebar = ref(false);
    const authStore = useAuthStore();
    const router = useRouter();
    const sidebarRef = ref(null);

    onClickOutside(sidebarRef, () => {
      console.log(sidebarRef)
      if (showSidebar.value) {
        showSidebar.value = false;
      }
    });

    return {
      showSidebar,
      sidebarRef,
      authStore,
      router,
    };
  },
  methods: {
    async logout() {
      try {
        await this.authStore.logout(this.$router);
      } catch (error) {
        console.error(error);
      }
    },
  },
  async mounted() {
    await this.authStore.fetchUser();
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