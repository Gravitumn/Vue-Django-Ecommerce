<template>
  <div class="user-management">
    <div ref="sidebarRef" class="sidebar-container">
      <sidebar v-if="showSidebar" :superCategories="superCategories"/>
    </div>
    
    <main-nav-bar :user="authStore.user" :isAuthenticated="authStore.isAuthenticated" @logout="logout"  :superCategories="superCategories"/>
    <sub-navbar v-model:showSidebar="showSidebar"/>
    <h1>User Management</h1>

    <!-- Add User Form -->
    <form @submit.prevent="addUser">
      <h2>Add New User</h2>
      <input v-model="newUser.username" placeholder="Username" required />
      <input
        v-model="newUser.email"
        type="email"
        placeholder="Email"
        required
      />
      <input
        v-model="newUser.password"
        type="password"
        placeholder="Password"
        required
      />
      <button type="submit">Add User</button>
    </form>

    <!-- User Table -->
    <h2>All Users</h2>
    <table>
      <thead>
        <tr>
          <th>Username</th>
          <th>Email</th>
          <th>Role</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.role }}</td>
          <td>
            <button @click="editUser(user)">Edit</button>
            <button @click="deleteUser(user.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Edit User Modal -->
    <div v-if="editingUser" class="modal">
      <h2>Edit User</h2>
      <input v-model="editingUser.username" placeholder="Username" />
      <input v-model="editingUser.email" type="email" placeholder="Email" />
      <select v-model="editingUser.role">
        <option value="user">User</option>
        <option value="admin">Admin</option>
        <option value="developer">Developer</option>
      </select>
      <button @click="updateUser">Save Changes</button>
      <button @click="cancelEdit">Cancel</button>
    </div>
  </div>
</template>
  
  <script>
  import MainNavBar from "../components/Navbar/MainNavbar.vue";
import SubNavbar from "../components/SubNavbar/SubNavbar.vue";
import Sidebar from "../components/SubNavbar/Sidebar.vue";
import { ref } from "vue";
import { onClickOutside } from "@vueuse/core";
import { useAuthStore } from "../store/auth.js";
import { useRouter } from "vue-router";
import axios from "../axios.js";
import { getCSRFToken } from "../store/auth";

export default {
  components: {
    MainNavBar,
    SubNavbar,
    Sidebar,
  },
  setup() {
    const showSidebar = ref(false);
    const authStore = useAuthStore();
    const router = useRouter();
    const sidebarRef = ref(null);

    onClickOutside(sidebarRef, () => {
      console.log(sidebarRef)
      if (showSidebar.value) {
        showSidebar.value = false;
      }
    });

    return {
      showSidebar,
      sidebarRef,
      authStore,
      router,
    };
  },
  data() {
    return {
      users: [],
      newUser: {
        username: "",
        email: "",
        password: "",
      },
      editingUser: null, // Stores the user currently being edited
      superCategories: [],
    };
  },
  methods: {
    async fetchSuperCategories(){
      try{
        const response = await axios.get("/api/get_super_category");
        this.superCategories = response.data;
        console.log(this.superCategories);
      }catch(error){
        console.error("Error fetching super categories:", error);
      }
    },
    async logout() {
      try {
        await this.authStore.logout(this.$router);
      } catch (error) {
        console.error(error);
      }
    },
    // Fetch all users
    async fetchUsers() {
      try {
        const response = await axios.get("/api/get_all_users");
        this.users = response.data;
        console.log(this.users);
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    },
    // Add a new user
    async addUser() {
      try {
        const response = await axios.post(
          "/api/register",
          {
            username: this.newUser.username,
            email: this.newUser.email,
            password: this.newUser.password,
          },
          {
            headers: {
              "X-CSRFToken": getCSRFToken(), // Pass CSRF token here
            },
            withCredentials: true, // Include credentials if necessary
          }
        );

        if (response.status === 201) {
          this.newUser.username = "";
          this.newUser.email = "";
          this.newUser.password = "";
          this.fetchUsers();
        }
      } catch (err) {
        this.error =
          "An error occurred during registration: " +
            err.response?.data?.error || err.message;
      }
    },
    // Edit a user
    editUser(user) {
      this.editingUser = { ...user }; // Clone the user object to avoid direct mutations
    },
    // Cancel editing
    cancelEdit() {
      this.editingUser = null;
    },
    // Update user data
    async updateUser() {
      try {
        const response = await axios.put(
          `/api/update_user/${this.editingUser.id}/`,
          this.editingUser,
          {
            headers: {
              "X-CSRFToken": getCSRFToken(), // Pass CSRF token here
            },
            withCredentials: true, // Include credentials if necessary
          }
        );
        if (response.status === 200) {
          this.editingUser = null; // Close the modal
          this.fetchUsers(); // Refresh the user list
        } else {
          const errorData = await response.json();
          console.error("Error updating user:", errorData.message);
        }
      } catch (error) {
        console.error("Error updating user:", error);
      }
    },
    // Delete a user
    async deleteUser(userId) {
      try {
        await axios.delete(`/api/delete_user/${userId}/`, {
          headers: {
            "X-CSRFToken": getCSRFToken(), // Pass CSRF token here
          },
          withCredentials: true, // Include credentials if necessary
        });
        this.fetchUsers(); // Refresh the user list
      } catch (error) {
        console.error("Error deleting user:", error);
      }
    },
  },
  async mounted() {
    await this.fetchUsers(); // Fetch users on component mount
    await this.authStore.fetchUser();
    await this.fetchSuperCategories();
  },
};
</script>
  
  <style>
.user-management {
  position: relative;
  padding-top: 20vh;
  /* margin: auto; */
  font-family: "Madimi One";
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
  