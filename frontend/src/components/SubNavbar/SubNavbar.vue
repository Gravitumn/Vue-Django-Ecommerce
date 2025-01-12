<template>
  <CNavbar expand="lg" color-scheme="light" class="custom-sub-navbar">
    <CContainer fluid class="sub-navbar-content">
      <CNavLink href="#" active @click="toggleShowSidebar" >
        <FontAwesomeIcon icon="bars" class="bars-icon"  />
        All
      </CNavLink>
      <CNavLink href="#" active> Today's Deals </CNavLink>
      <CNavLink href="#" active> Trending </CNavLink>
    </CContainer>
  </CNavbar>
</template>

<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import { CContainer, CNavbar, CNavItem, CNavLink } from "@coreui/vue";

library.add(faBars);
export default {
  name: "SubNavbar",
  components: {
    FontAwesomeIcon,
    CNavbar,
    CContainer,
    CNavItem,
    CNavLink,
  },
  props:{
    showSidebar:Boolean,
  },
  methods:{
    toggleShowSidebar(){
      console.log(this.showSidebar)
      this.$emit("update:showSidebar", !this.showSidebar);
      console.log("After toggle:", this.showSidebar);
    } 
  }
};
</script>

<style>
.custom-sub-navbar {
  position: absolute ;
  top: 10.87vh !important;
  left: 0;
  background-color: #3335e1;
  height: 6.59vh;
  width: 100%;
  z-index:500 !important;
}
.sub-navbar-content {
  justify-content: left !important;
  align-items: center;
  gap:4.2vw;
  margin-left: 2.36vw !important;
  color:white;
  font-size:2.7vh;
  z-index:600 !important;
}
</style>