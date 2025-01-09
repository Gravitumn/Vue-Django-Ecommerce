<template>
  <div class="SecondNavBar" :class="{ 'with-shadow': scrolled}">
    <div class="menu">
      <div class="All">
        <FontAwesomeIcon icon="bars" class="bars-icon" />
        All
      </div>

      <div class="Deals">Today's Deals</div>

      <div class="trending">Trending</div>
    </div>
  </div>
</template>

<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faBars } from "@fortawesome/free-solid-svg-icons";

library.add(faBars);

export default {
  name: "SecondNavBar",
  components: {
    FontAwesomeIcon,
  },
  props: {
    scrolled: {
      type: Boolean,
      required: true,
    },
  },
}

</script>

<style>
.SecondNavBar {
  width: 100vw;
  height: 6.6vh;
  background-color: #3335e1;
  position: fixed;
  top: 10vh;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: left;
  padding-left: 2.4%;
  margin: 0 auto;
  color: white;
  transition: box-shadow 0.3s ease;
}

.SecondNavBar.with-shadow {
  box-shadow: 0px 10px 5px rgba(0, 0, 0, 0.25); /* Add shadow when scrolled */
}

.menu {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 5vw;
  width: auto;
}

.All {
  display: flex;
  width: auto;
  justify-content: center;
  align-items: center;
  gap: 3px;
  font-size: 2.7vh;
}

.bars-icon {
  height: 2.5vh;
  width: auto;
}

.Deals {
  font-size: 2.7vh;
  white-space: nowrap;
  width: auto;
}

.trending {
  font-size: 2.7vh;
}
</style>
