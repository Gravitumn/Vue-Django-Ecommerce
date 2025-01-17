<template>
  <div>
    <multi-selection v-model:categories="categories" :options="subCategories" />
    <button @click="showSelected">click</button>
  </div>
</template>

<script>
import axios from "../axios.js";
import MultiSelection from "../components/MultiSelection.vue";
export default {
  data() {
    return{
        subCategories: [],
        selected: [],
        categories:[],
    };
  },
  components: {
    MultiSelection,
  },
  methods: {
    showSelected(){
        console.log(this.categories);
    },
    async fetchSubCategories() {
      try {
        const response = await axios.get("/api/get_sub_category");
        this.subCategories = response.data;
        console.log(this.subCategories);
      } catch (error) {
        console.error("Error fetching super categories:", error);
      }
    },
  },
  mounted() {
    this.fetchSubCategories();
  },
};
</script>

<style>
</style>