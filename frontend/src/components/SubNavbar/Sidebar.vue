<template>
  <CSidebar class="side-bar">
    <CSidebarNav>
      <CNavTitle class="side-bar-title"> Discover </CNavTitle>
      <CNavItem href="/Products">All Products</CNavItem>
      <CNavItem href="#" class="sidebar-item"> Lofi Music </CNavItem>
      <CNavItem href="#"> E-reading & books </CNavItem>

      <CNavTitle class="side-bar-title"> Shop by department </CNavTitle>
      <CNavItem
        v-for="category in superCategories"
        :key="category.id"
        class="department"
        @click="navigateTo(category.id)"
        >{{ category.name }}</CNavItem
      >
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
  props: {
    superCategories: Array,
  },
  methods: {
    navigateTo(route) {
      console.log(route);
      const url = `/Products/${route}`;
      this.$router.push(url).then(() => {
        this.$router.go(0); // Reloads the current page
      });
    },
  },
};
</script>

<style>
.side-bar {
  position: fixed !important;
  top: 0;
  left: 0;
  height: 100vh;
  width: 26.15vw;
  box-shadow: 0 0 0 10000px rgba(0, 0, 0, 0.5) !important;
}
.side-bar-title {
  color: black !important;
  font-size: 120% !important;
  justify-self: left !important;
  padding: 0 0 !important;
  display: flex;
  justify-content: left;
  margin-left: 5%;
}
.department {
  display: flex;
  /* margin: 1.5vw; */
  width: 100%;
  padding: 5%;
}
</style>

<style scoped>
.nav-item:hover {
  background-color: #f5be64 !important;
}
</style>