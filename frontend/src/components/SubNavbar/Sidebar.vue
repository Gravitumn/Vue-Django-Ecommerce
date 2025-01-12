<template>
  <CSidebar class="side-bar">
    <CSidebarNav>
      <CNavTitle class="side-bar-title"> Discover </CNavTitle>
      <CNavItem href="#" class="sidebar-item"> Lofi Music </CNavItem>
      <CNavItem href="#"> E-reading & books </CNavItem>

      <CNavTitle class="side-bar-title"> Shop by department </CNavTitle>
      <CNavItem href="#"> Gaming </CNavItem>
      <CNavItem href="#"> Decorations </CNavItem>
      <CNavItem href="#"> cloths & fashions </CNavItem>
      <CNavItem href="#"> Stationary </CNavItem>
      <CNavItem href="#"> Toy & Collection </CNavItem>
      <CNavItem href="#"> DIY </CNavItem>
    </CSidebarNav>
  </CSidebar>
</template>

<script>
import { CSidebar, CSidebarNav, CNavItem, CNavTitle } from "@coreui/vue";
export default {
  name: "Sidebar",
  components: {
    CSidebar,
    CSidebarNav,
    CNavItem,
    CNavTitle,
  },
};
</script>

<style>
.side-bar {
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
  widows: 26.15vw;
}
.side-bar-title{
  color:black !important;
  font-size:120% !important;
  justify-self: left !important;
  padding: 0 0 !important;
  display: flex;
  justify-content: left;
  margin-left: 5%;
}
</style>