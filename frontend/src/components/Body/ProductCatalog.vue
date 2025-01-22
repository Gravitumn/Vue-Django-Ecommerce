<template>
  <div class="product-catalog">
    <div
      class="products-row"
      v-for="(rowItems, rowIndex) in rows"
      :key="rowIndex"
    >
      <div
        class="products-box"
        v-for="(item, itemIndex) in rowItems"
        :key="itemIndex"
      >
        <img
          :src="item.image"
          alt="Product Image"
          style="width: 16vw; height: 20vh; object-fit: contain"
        />
        <div class="product-label">
          <a>{{ item.name }}</a>
          <a>{{ item.price }}$</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "../../axios";
export default {
  name: "ProductCatalog",
  data() {
    return {
      products: [],
    };
  },
  methods: {
    async fetchSuperCategoryProducts() {
      try {
        if (this.$route.params.superCategory) {
          const superCategory = this.$route.params.superCategory;
          const response = await axios.get(
            `api/get_super_category_products/${superCategory}`
          );
          this.products = response.data;
        } else {
          const response = await axios.get(`api/show_all_products`);
          this.products = response.data;
        }
        console.log("Products : ", this.products);
      } catch (error) {
        console.error("Error fetching super category products:", error);
      }
    },
  },
  computed: {
    rows() {
      const maxItemsPerRow = 5;
      const rows = [];
      for (let i = 0; i < this.products.length; i += maxItemsPerRow) {
        rows.push(this.products.slice(i, i + maxItemsPerRow));
      }
      return rows;
    },
  },
  mounted() {
    this.fetchSuperCategoryProducts();
  },
};
</script>

<style scoped>
.product-catalog {
  position: absolute;
  top: 16.6vh;
  display: flex;
  justify-content: left;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
  width: 100vw;
}
.products-row {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}
.products-box {
  width: 18vw !important;
  aspect-ratio: 18/25;
  aspect-ratio: 218/235;
  background-color: #f0f0f0;
  display: flex;
  flex-direction: column;
  align-items: center;
  /* justify-content: center; */
  border-radius: 8px;
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.5);
  text-align: center;
  gap: 5.95%;
  padding-top: 1%;
  font-size: 1.4vw;
  color: black;
}
.image-in-box {
  width: 69.4%;
  aspect-ratio: 1/1.05;
}
.product-label {
  font-size: 1.5vw;
  display: flex;
  flex-direction: column;
  width: 100%;
}
</style>