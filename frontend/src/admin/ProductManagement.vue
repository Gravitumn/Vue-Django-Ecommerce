<template>
  <div class="product-management">
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
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>
            <img
              :src="product.image"
              alt="Product Image"
              style="max-width: 100px; max-height: 100px; object-fit: contain"
            />
          </td>
          <td>{{ product.name }}</td>
          <td>{{ product.price }}</td>
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
        <input
          type="file"
          accept="image/*"
          @change="handleFileChange_onUpdate"
        />
        <button type="submit">Save Changes</button>
        <button @click="cancelEdit">Cancel</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "../axios.js";
import { getCSRFToken } from "../store/auth";
export default {
  data() {
    return {
      products: [],
      newProduct: {
        name: "",
        price: 0,
        image: null,
      },
      editingProduct: {
        id: 0,
        name: "",
        price: 0,
        image: null,
      },
    };
  },
  methods: {
    async fetchProduct() {
      try {
        const response = await axios.get("/api/get_all_products");
        this.products = response.data;
        console.log(this.products);
      } catch (error) {
        console.error("Error fetching products:", error);
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
      try {
        const formData = new FormData();
        formData.append("name", this.newProduct.name);
        formData.append("price", this.newProduct.price);
        if (this.newProduct.image) {
          formData.append("image", this.newProduct.image);
        }
        const response = await axios.post("api/addProduct", formData, {
          headers: {
            "X-CSRFToken": getCSRFToken(), // Pass CSRF token here
          },
          withCredentials: true, // Include credentials if necessary
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
          { name: this.editingProduct.name, price: this.editingProduct.price },
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