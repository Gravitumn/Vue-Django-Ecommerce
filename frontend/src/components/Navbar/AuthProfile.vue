<template>
  <div class="right-navbar">
    <div v-if="isAuthenticated">
      <div class="profile" v-on:click="toggleDropdown">
        <FontAwesomeIcon icon="shopping-cart" class="shopping-cart" />

        <div class="user-profile">
          <span>
            {{ user.username }}
          </span>

          <FontAwesomeIcon icon="user-circle" class="user" />
        </div>
      </div>
    </div>
    <div v-else>
      <div class="authen">
        <a class="sign-in" href="/login"> Sign-in </a>
        <div>|</div>
        <a class="register" href="/register"> Register </a>
      </div>
    </div>
  </div>
</template>

<script>
import { faShoppingCart } from "@fortawesome/free-solid-svg-icons";
import { faUserCircle } from "@fortawesome/free-solid-svg-icons";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
library.add(faUserCircle)
library.add(faShoppingCart)
export default {
  name: "AuthProfile",
  props: {
    isAuthenticated: {
      type: Boolean,
      required: true,
    },
    user: {
      type: Object,
      default: null,
    },
  },
  components:{
    FontAwesomeIcon,
  }
};
</script>

<style>
.right-navbar {
  width: auto;
  height: auto;
  display:flex;
  margin-right: 1.5vw;
}
.authen{
    display: flex;
    gap: 1.55vw;
    font-size: 1.5vw;
}
.sign-in{
    text-decoration: none;
    color:white;
}
.sign-in:hover{
    color: #f5be64;
}
.register{
    text-decoration: none;
    color:white;
}.register:hover{
    color: #f5be64;
}
</style>