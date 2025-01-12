<template>
  <CNavbar expand="lg" color-scheme="light" class="custom-navbar">
    <CContainer fluid class="custom-container">
      <navbar-logo/>
      <search-bar/>
      <auth-profile :is-authenticated="authStore.isAuthenticated" :user="authStore.user"/>
    </CContainer>
  </CNavbar>
</template>

<script>
import NavbarLogo from './NavbarLogo.vue';
import SearchBar from './SearchBar.vue';
import AuthProfile from './AuthProfile.vue';
import { CContainer, CNavbar } from '@coreui/vue';
import { useAuthStore } from "../../store/auth.js";
import { useRouter } from "vue-router";

export default {
  name:"MainNavbar",
  components:{
    NavbarLogo,
    SearchBar,
    AuthProfile,
    CNavbar,
    CContainer,
  },
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();

    return {
      authStore,
      router,
    };
  },
  async mounted() {
    await this.authStore.fetchUser();
  },
};
</script>

<style>
.custom-navbar {
  position: fixed !important;
  top: 0;
  left: 0;
  background-color: #0f1359;
  height: 10.87vh;
  width: 100%;
  z-index: 1000 !important;
}
.custom-container{
  width: 100vw;
  height: 100%;
  display: flex;
  align-items: center;
}
</style>