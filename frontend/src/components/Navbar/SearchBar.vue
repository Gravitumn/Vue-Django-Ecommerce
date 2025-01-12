<template>
  <CForm class="d-flex search-bar">
    <CDropdown class="dropdown" :popper="false">
      <CDropdownToggle >All</CDropdownToggle>
      <CDropdownMenu class="dropdown-menu">
        <CDropdownItem href="#">Gaming</CDropdownItem>
        <CDropdownItem href="#">Decoration</CDropdownItem>
        <CDropdownItem href="#">E-reading & books</CDropdownItem>
      </CDropdownMenu>
    </CDropdown>
    <CFormInput
      type="search"
      class="search-box no-radius"
      placeholder="Search"
    />
    <CButton
      type="submit"
      color="success"
      variant="outline"
      class="search-button"
    >
      <FontAwesomeIcon
        icon="search"
        class="search-icon"
        style="font-size: 1.5vw"
      />
    </CButton>
  </CForm>
</template>

<script>
import {
  CForm,
  CFormInput,
  CButton,
  CDropdownMenu,
  CDropdown,
  CDropdownToggle,
  CDropdownItem,
} from "@coreui/vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
library.add(faSearch);
export default {
  name: "SearchBar",
  components: {
    CForm,
    CFormInput,
    CButton,
    FontAwesomeIcon,
    CDropdownMenu,
    CDropdown,
    CDropdownToggle,
    CDropdownItem,
  },
};
</script>

<style>
.search-bar {
  height: 6.59vh;
  width: 63.32vw;
  align-content: center;
  justify-content: center;
  z-index: 1500 !important;
}
.search-box {
  width: 62.15vw;
}
.no-radius {
  border-radius: 0 !important;
}
.search-button {
  border-radius: 0 calc(20 / 975 * 100vw) calc(20 / 975 * 100vw) 0 !important;
  height: 6.59vh !important;
  width: 4.61vw !important;
  display: flex;
  justify-content: center;
  align-items: center;
  color: black !important;
  background-color: #f5be64 !important;
  border: none !important;
}
.dropdown {
  height: 6.59vh !important;
  width: 4.61vw !important;
  background-color: #e8a1fd;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: calc(20 / 975 * 100vw) 0 0 calc(20 / 975 * 100vw) !important;
  
}
.dropdown-menu{
  position:absolute;
}
</style>