/<template>
  <div class="home-test">
    <div class="navbar">
      <NavBar />
      <div class="second-navbar">
        <second-navbar :scrolled="scrolled"/>
      </div>
    </div>

    <background />
    <div class="content-overlay">
      <catalog @scroll="handleScrollTop"/>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import SecondNavbar from "../components/SecondNavbar.vue";
import Background from "../components/Background.vue";
import Catalog from "../components/Catalog.vue";
export default {
  components: {
    NavBar,
    SecondNavbar,
    Background,
    Catalog,
  },
  data(){
    return {
      scrolled: false,
    };
  },
  methods: {
    handleScrollTop(scrolled) {
      this.scrolled = scrolled;
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Madimi+One&display=swap");
.navbar{
  z-index: 999;
}
.home-test {
  width: 100vw;
  height: 100vh;
  font-family: "Madimi One";
}
.content-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 2;
  pointer-events: auto;
}
</style>