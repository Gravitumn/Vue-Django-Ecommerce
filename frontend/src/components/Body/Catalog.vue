<template>
  <div class="catalog">
    <div class="row" v-for="(rowItems, rowIndex) in rows" :key="rowIndex">
      <div class="box" v-for="(item, itemIndex) in rowItems" :key="itemIndex">
        {{ item }}
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from "./ProductCard.vue";
export default {
  name: "Catalog",
  components: {
    ProductCard,
  },
  data() {
    return {
      items: Array.from({ length: 10 }, (_, i) => `Item ${i + 1}`), // Mock items
      scrolled: false,
    };
  },
  computed: {
    rows() {
      const maxItemsPerRow = 4;
      const rows = [];
      for (let i = 0; i < this.items.length; i += maxItemsPerRow) {
        rows.push(this.items.slice(i, i + maxItemsPerRow));
      }
      return rows;
    },
  },
};
</script>

<style>
.catalog {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
  margin-left: 1vw;
  margin-right: 1vw;
}
.row {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}
.box {
  width: 18vw !important;
  aspect-ratio: 218/235;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.5);
  text-align: center;
}
</style>