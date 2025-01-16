<template>
  <CSidebar class="side-bar">
    <CSidebarNav>
      <CNavTitle class="side-bar-title"> Discover </CNavTitle>
      <CNavItem href="#" class="sidebar-item"> Lofi Music </CNavItem>
      <CNavItem href="#"> E-reading & books </CNavItem>

      <CNavTitle class="side-bar-title"> Shop by department </CNavTitle>
      <CNavItem v-for="category in superCategories" :key="category.id" class="department">{{ category.name }}</CNavItem>
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
  props:{
    superCategories:Array,
  }
};
</script>

<style>
.side-bar {
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
  width: 26.15vw;
  box-shadow:0 0 0 10000px rgba(0,0,0,.50) !important;
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
.department{
  display: flex;
  margin: 1.5vw;
}
</style>