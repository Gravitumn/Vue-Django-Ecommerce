<template>
  <div class="catalog">
    <div class="row" v-for="(rowItems, rowIndex) in rows" :key="rowIndex">
      <div class="box" v-for="(item, itemIndex) in rowItems" :key="itemIndex">
        {{ text[itemIndex+(rowIndex*4)] }}
        <img :src = "getImagePath(itemIndex,rowIndex)" :alt="`Image ${itemIndex}`" class="image-in-box"/>
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
      items: Array.from({ length: 8 }, (_, i) => `Item ${i + 1}`), // Mock items
      scrolled: false,
      text:[
        "Electronics","Home & Kitchen", "Fashions","Health & Fitness", "Gaming", "Beauty & Cares", "Reading & Books", "Stationary"
      ],
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
  methods:{
    getImagePath(index,row){
      return new URL(`../../assets/images/image${index + 1+(row*4)}.jpg`, import.meta.url).href;
    }
  }
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
  flex-direction: column;
  align-items: center;
  /* justify-content: center; */
  border-radius: 8px;
  box-shadow: 10px 10px 10px rgba(0, 0, 0, 0.5);
  text-align: center;
  gap:5.95%;
  padding-top:1%;
  font-size:1.4vw;
  color:black;
}
.image-in-box{
  width: 69.4%;
  aspect-ratio: 1/1.05;
}
</style>