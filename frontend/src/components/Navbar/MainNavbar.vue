<template>
  <CNavbar expand="lg" color-scheme="light" class="custom-navbar">
    <CContainer fluid class="custom-container">
      <navbar-logo/>
      <search-bar/>
      <auth-profile :user="user" :isAuthenticated="isAuthenticated" @logout="logout"/>
    </CContainer>
  </CNavbar>
</template>

<script>
import NavbarLogo from './NavbarLogo.vue';
import SearchBar from './SearchBar.vue';
import AuthProfile from './AuthProfile.vue';
import { CContainer, CNavbar } from '@coreui/vue';
export default {
  name:"MainNavbar",
  components:{
    NavbarLogo,
    SearchBar,
    AuthProfile,
    CNavbar,
    CContainer,
  },
  props: {
    user: Object,
    isAuthenticated: Boolean
  },
  methods: {
    logout() {
      this.$emit("logout");
    }
  }
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