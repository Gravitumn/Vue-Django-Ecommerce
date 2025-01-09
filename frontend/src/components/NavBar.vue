<template>
  <div class="navbar">
    <div class="logo">LOFI SHOP</div>

    <div class="search-bar">
      <!-- filter button -->
      <div class="filter">
        All
        <span class="triangle-down"></span>
      </div>

      <!-- search box -->
      <div class="search-box">
        <div class="search-hint">Search product</div>
      </div>

      <!-- search submit -->
      <div class="submit">
        <FontAwesomeIcon icon="search" class="search-icon" />
      </div>
    </div>

    <div class="nav-bar-right">
        <div class = "sign-in">
            Sign-in
        </div>
        <div >|</div>
        <div class="register">
            Register
        </div>
    </div>
  </div>
</template>

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
library.add(faSearch);
export default {
  name: "NavBar",
  components:{
    FontAwesomeIcon,
  }
};
</script>

<style>
.navbar {
  width: 100vw;
  height: 10vh;
  background-color: #0f1359;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-left: 2%;
  padding-right: 2%;
  margin: 0 auto;
  overflow: hidden;
}

.logo {
  font-family: "Madimi One";
  font-size: 3vw;
  color: #d091a6;
  height: 50%;
  display: flex;
  align-items: center;
  -webkit-text-stroke: 10px white;
  letter-spacing: 7px;
  paint-order: stroke fill;
}

.fix-stroke {
  paint-order: stroke fill;
}

.search-bar {
  width: 55%;
  height: 60%;
  /* background-color:white; */
  display: flex;
  align-items: center;
}
.filter {
  width: 8.25%;
  height: 100%;
  justify-content: center;
  align-items: center;
  display: flex;
  background-color: #e8a1fd;
  border-radius: 20px 0px 0px 20px;
  font-size: 1.5vw;
}
.search-box {
  width: 83.5%;
  height: 100%;
  align-items: center;
  display: flex;
  background-color: white;
  
}
.search-box .search-hint{
    margin-left:3%;
    font-size: 1.5vw;
    color: #7d7d7d;
}
.submit {
  width: 8.25%;
  height: 100%;
  background-color: #f5be64;
  border-radius: 0px 20px 20px 0px;
  align-content: center;
  justify-content: center;
}
.search-icon{
    height:35%;
    width: auto;
}

.triangle-down {
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 5px solid black; /* Adjust the color of the triangle */
  margin-left: 5px; /* Space between text and triangle */
}

.nav-bar-right {
  width: 15%;
  height: 60%;
  /* background-color: white; */
  margin-right: 5%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap:10%;
  color:white;
  font-size:1.5vw;
}
</style>