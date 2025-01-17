<template>
  <CNavbarBrand class="logo">
    <router-link to="/" class="logo-text">LOFI SHOP</router-link>
  </CNavbarBrand>
</template>

<script>
import {CNavbarBrand} from "@coreui/vue";
export default {
    name: "Navbar-Logo",
    components:{
        CNavbarBrand,
    }
};
</script>

<style>
.logo-text {
  margin-left: 1.54vw;
  text-decoration: none;
  color: #d091a6;
  font-size: 3vw;

  height: 50%;
  display: flex;
  align-items: center;
  -webkit-text-stroke: 7px white;
  letter-spacing: 5%;
  paint-order: stroke fill;
}
</style>