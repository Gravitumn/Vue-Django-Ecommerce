<template>
  <div class="products">
    <div ref="sidebarRef" class="sidebar-container">
      <sidebar v-if="showSidebar" :superCategories="superCategories" />
    </div>

    <main-nav-bar
      :user="authStore.user"
      :isAuthenticated="authStore.isAuthenticated"
      @logout="logout"
      :superCategories="superCategories"
    />
    <sub-navbar v-model:showSidebar="showSidebar" />
    <product-catalog/>
  </div>
</template>

<script>
import MainNavBar from "../components/Navbar/MainNavbar.vue";
import SubNavbar from "../components/SubNavbar/SubNavbar.vue";
import Sidebar from "../components/SubNavbar/Sidebar.vue";
import ProductCatalog from "../components/Body/ProductCatalog.vue";
import { ref } from "vue";
import { onClickOutside } from "@vueuse/core";
import { useAuthStore } from "../store/auth.js";
import { useRouter } from "vue-router";
import axios from "../axios.js";
export default {
  components: {
    MainNavBar,
    SubNavbar,
    Sidebar,
    ProductCatalog,
  },
  setup() {
    const showSidebar = ref(false);
    const authStore = useAuthStore();
    const router = useRouter();
    const sidebarRef = ref(null);

    onClickOutside(sidebarRef, () => {
      console.log(sidebarRef);
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
  data(){
    return {
      superCategories: [],
    }
  },
  methods: {
    async fetchSuperCategories(){
      try{
        const response = await axios.get("/api/get_super_category");
        this.superCategories = response.data;
        console.log(this.superCategories);
      }catch(error){
        console.error("Error fetching super categories:", error);
      }
    },
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
    await this.fetchSuperCategories();
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Madimi+One&display=swap");
.products {
  width: 100vw;
  height: 100vh;
  font-family: "Madimi One";
}
.sidebar-container{
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
  z-index: 1100;
}
</style>