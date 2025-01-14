<template>
  <div class="right-navbar">
    <div v-if="isAuthenticated">
      <div class="profile" v-on:click="toggleDropdown">
        <FontAwesomeIcon icon="shopping-cart" class="shopping-cart" />

        <div class="user-profile">
          <span class="username-text">
            {{ truncatedUsername }}
          </span>
          <CDropdown :popper="true">
            <CDropdownToggle :caret="false" class="frame">
              <FontAwesomeIcon icon="user-circle" class="user" />
            </CDropdownToggle>
            <CDropdownMenu>
              <CDropdownItem href="/ProductManagement" class="dropdown-button"
                >Add your products</CDropdownItem
              >
              <CDropdownItem
                v-if="isAdmin"
                href="/admin/ProductManagement"
                class="dropdown-button"
                >manage products(admin)</CDropdownItem
              >
              <CDropdownItem
                v-if="isAdmin"
                href="/admin/UserManagement"
                class="dropdown-button"
                >manage users(admin)</CDropdownItem
              >
              <CDropdownItem @click="logout" class="dropdown-button"
                >Log out</CDropdownItem
              >
            </CDropdownMenu>
          </CDropdown>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="authen">
        <a class="sign-in" href="/login"> Sign-in </a>
        <div style="color: #f5be64">|</div>
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
import {
  CDropdownToggle,
  CDropdownMenu,
  CDropdownItem,
  CDropdown,
} from "@coreui/vue";
library.add(faUserCircle);
library.add(faShoppingCart);
export default {
  name: "AuthProfile",
  components: {
    FontAwesomeIcon,
    CDropdownItem,
    CDropdownMenu,
    CDropdownToggle,
    CDropdown,
  },
  props: {
    user: Object,
    isAuthenticated: Boolean,
  },
  computed: {
    truncatedUsername() {
      return this.user?.username.length > 8
        ? this.user?.username.slice(0, 8) + "..."
        : this.user?.username;
    },
    isAdmin() {
      return this.user?.role == "admin";
    },
  },
  methods: {
    logout() {
      this.$emit("logout");
    },
  },
};
</script>

<style>
.right-navbar {
  width: 15%;
  height: 60%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1.5vw;
}
.authen {
  display: flex;
  gap: 1.55vw;
  font-size: 1.5vw;
}
.sign-in {
  text-decoration: none;
  color: white;
}
.sign-in:hover {
  color: #f5be64;
}
.register {
  text-decoration: none;
  color: white;
}
.register:hover {
  color: #f5be64;
}
.profile {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5vw;
  color: white;
  font-size: 2.125vw;
}
.shopping-cart {
  color: #f19edc;
}
.user-profile {
  display: flex;
  color: #0f1359;
}
.username-text {
  margin-top: 1vh;
  font-size: 1.5vw;
  color: #f5be64;
}
.user {
  color: #f5be64;
  font-size: 2.2vw;
}
.btn-group {
  border-color: unset !important;
}
.dropdown-button:hover {
  background-color: #f5be64 !important;
}
</style>