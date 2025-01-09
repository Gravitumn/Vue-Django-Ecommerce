<template>
  <div class="catalog" @scroll="handleScroll">
    <div class="scrollable">
      <div class="content">
        <div class="stroke-text">Winter Sales</div>
        <div class="shadow-text">Winter Sales</div>
      </div>
      <div class="catalog-table">
        <div class="row" v-for="(rowItems, rowIndex) in rows" :key="rowIndex">
          <div
            class="box"
            v-for="(item, itemIndex) in rowItems"
            :key="itemIndex"
          >
            {{ item }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "Catalog",
  data() {
    return {
      items: Array.from({ length: 8 }, (_, i) => `Item ${i + 1}`), // Mock items
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
  methods: {
    handleScroll(event) {
      this.scrolled = window.scrollY > 0;
      this.$emit("scroll", this.scrolled);
    },
  },
  created() {
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>
  
  <style>
.catalog {
  position: absolute;
  top: 16.6vh;
  left: 0;
  width: 100vw;
  overflow-y: auto;
}
.scrollable {
  display: flex;
  flex-direction: column;
  width: 100%;
}
.content {
  flex: 0 0 37.7vh;
}

.stroke-text {
  margin-left: 15vw;
  font-size: calc(10vw + 5vh);
  color: #8194fa;
  -webkit-text-stroke: 2vw white;
  paint-order: stroke fill;
  position: absolute;
  z-index: 2;
  white-space: nowrap;
}

.shadow-text {
  margin-left: 15vw;
  font-size: calc(10vw + 5vh);
  color: #8194fa;
  text-shadow: 0.125em 0.15em 0.05em rgba(0, 0, 0, 0.6);
  position: absolute;
  z-index: 1;
  white-space: nowrap;
}
.catalog-table {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
  margin-left: 3.9vw;
  margin-right: 3.9vw;
}

.row {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.box {
  flex: 1 1 calc(25% - 1rem);
  max-width: 17vw;
  min-width: 17vw;
  height: 36vh;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
}
</style>