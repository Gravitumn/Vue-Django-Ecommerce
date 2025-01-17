<template>
  <div class="admin-product-management">
    <h1>Product Management</h1>

    <!-- Add Product Form -->
    <form @submit.prevent="addProduct">
      <h2>Add New Product</h2>
      <input v-model="newProduct.name" placeholder="Product_name" required />
      <input
        v-model="newProduct.price"
        type="number"
        step="0.01"
        min="0"
        placeholder="Price"
        required
      />
      <multi-selection
        :options="subCategories"
        v-model:categories="newProduct.categories"
      />
      <input
        type="file"
        accept="image/*"
        @change="handleFileChange_onCreate"
        required
      />

      <button type="submit">Add new Product</button>
    </form>

    <!-- Product Table -->
    <h2>All Product</h2>
    <table>
      <thead>
        <tr>
          <th>Image</th>
          <th>Product Name</th>
          <th>Price</th>
          <th>User</th>
          <th>Category</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(product, index) in products" :key="product.id">
          <td>
            <img
              :src="product.image"
              alt="Product Image"
              style="max-width: 100px; max-height: 100px; object-fit: contain"
            />
          </td>
          <td>{{ product.name }}</td>
          <td>{{ product.price }}</td>
          <td>{{ product.user }}</td>
          <td>
            {{ getCategories(index) }}
          </td>
          <td>
            <button @click="editProduct(product)">Edit</button>
            <button @click="deleteProduct(product.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Edit User Modal -->
    <div v-if="editing()" class="modal">
      <h2>Edit Product</h2>
      <form @submit.prevent="updateProduct" enctype="multipart/form-data">
        <input v-model="editingProduct.name" placeholder="Product Name" />
        <input
          v-model="editingProduct.price"
          type="number"
          step="0.01"
          min="0"
          placeholder="Price"
        />
        <multi-selection
          :options="subCategories"
          v-model:selected="editingProduct.categories"
        />
        <input
          type="file"
          accept="image/*"
          @change="handleFileChange_onUpdate"
        />
        <button type="submit">Save Changes</button>
        <button @click="cancelEdit">Cancel</button>
      </form>
    </div>
    <button @click="showData">click</button>
  </div>
</template>

<script>
import MultiSelection from "../components/MultiSelection.vue";
import axios from "../axios.js";
import { getCSRFToken } from "../store/auth.js";
export default {
  data() {
    return {
      products: [],
      newProduct: {
        name: "",
        price: 0,
        image: null,
        categories: [],
      },
      editingProduct: {
        id: 0,
        name: "",
        price: 0,
        image: null,
        categories: [],
      },
      subCategories: [],
    };
  },
  components: {
    MultiSelection,
  },
  methods: {
    getCategories(index) {
      let newCategories = "";
      for (let i = 0; i < this.products[index].categories.length; i++) {
        var temp = this.subCategories.find(
          ({ id }) => id === this.products[index].categories[i]
        );
        // console.log("temp=",temp);
        if (temp) {
          newCategories = newCategories.concat(", ",temp.name);
        }
      }
      return newCategories;
    },
    showData() {
      console.log(this.products.length);
      console.log(this.products);
    },
    async fetchProduct() {
      try {
        const response = await axios.get("/api/admin_get_all_products");
        this.products = response.data.reduce((acc, product) => {
          const existingProduct = acc.find((item) => item.id === product.id);

          if (existingProduct) {
            if (!existingProduct.categories.includes(product.category)) {
              existingProduct.categories.push(product.category);
            }
          } else {
            acc.push({
              ...product,
              categories: [product.category],
            });
          }

          return acc;
        }, []);
        // console.log(this.products[0]);
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    },
    async fetchSubCategories() {
      try {
        const response = await axios.get("/api/get_sub_category");
        this.subCategories = response.data;
        // console.log(this.subCategories);
      } catch (error) {
        console.error("Error fetching super categories:", error);
      }
    },
    handleFileChange_onCreate(event) {
      const file = event.target.files[0];
      if (file) {
        console.log(file);
        this.newProduct.image = file;
      } else {
        console.error("No file selected");
      }
    },
    handleFileChange_onUpdate(event) {
      const file = event.target.files[0];
      if (file) {
        console.log(file);
        this.editingProduct.image = file;
      } else {
        console.error("No file selected");
      }
    },
    async addProduct() {
      console.log("ok");
      console.log(this.newProduct.categories);
      try {
        const authState = JSON.parse(localStorage.getItem("authState"));
        const category_data = JSON.parse(
          JSON.stringify(this.newProduct.categories)
        );
        let arr = [];
        for (let i = 0; i < category_data.length; i++) {
          arr.push(category_data[i].id);
        }
        console.log(arr);
        console.log(authState.user);

        const formData = new FormData();
        formData.append("name", this.newProduct.name);
        formData.append("price", this.newProduct.price);
        formData.append("user", authState.user.id);
        formData.append("category", JSON.stringify(arr));
        if (this.newProduct.image) {
          formData.append("image", this.newProduct.image);
        }
        const response = await axios.post("api/addProduct", formData, {
          headers: {
            "X-CSRFToken": getCSRFToken(),
          },
          withCredentials: true,
        });

        if (response.status === 201) {
          this.newProduct.name = "";
          this.newProduct.price = 0;
          this.fetchProduct();
        }
      } catch (err) {
        console.error("Error uploading product:", err);
      }
    },
    editing() {
      return (
        this.editingProduct.name != "" &&
        this.editingProduct.price != 0 &&
        this.editingProduct.image != null
      );
    },
    editProduct(product) {
      console.log("editing");
      this.editingProduct = {
        id: product.id,
        name: product.name,
        price: product.price,
        image: product.image,
      };
    },
    cancelEdit() {
      this.editingProduct = {
        id: 0,
        name: "",
        price: 0,
        image: null,
      };
    },
    async updateProduct() {
      try {
        const Jsonresponse = await axios.put(
          `/api/update_product/${this.editingProduct.id}/`,
          {
            name: this.editingProduct.name,
            price: this.editingProduct.price,
            categories: this.editingProduct.categories,
          },
          {
            headers: {
              "X-CSRFToken": getCSRFToken(), // Pass CSRF token here
            },
            withCredentials: true, // Include credentials if necessary
          }
        );

        var formDataResponse = null;
        if (this.editingProduct.image) {
          console.log(this.editingProduct.image);
          const formData = new FormData();
          formData.append("image", this.editingProduct.image);
          formDataResponse = await axios.post(
            `/api/update_product_image/${this.editingProduct.id}/`,
            formData,
            {
              headers: {
                "X-CSRFToken": getCSRFToken(),
              },
              withCredentials: true,
            }
          );
        }

        if (Jsonresponse.status === 200 && formDataResponse?.status === 200) {
          console.log("Product updated successfully");
          this.cancelEdit();
          this.fetchProduct();
        }
      } catch (err) {
        console.error("Error updating product:", err);
      }
    },
    async deleteProduct(productId) {
      try {
        await axios.delete(`/api/delete_product/${productId}/`, {
          headers: {
            "X-CSRFToken": getCSRFToken(), // Pass CSRF token here
          },
          withCredentials: true, // Include credentials if necessary
        });
        this.fetchProduct(); // Refresh the user list
      } catch (error) {
        console.error("Error deleting product:", error);
      }
    },
  },
  mounted() {
    this.fetchProduct();
    this.fetchSubCategories();
  },
};
</script>

<style>
.product-management {
  max-width: 800px;
  margin: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #fff;
  padding: 20px;
  border: 1px solid #ddd;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>