<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input v-model="username" id="username" type="username" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input v-model="email" id="email" type="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <p v-if="error">{{ error }}</p>
    <p v-if="success">{{ success }}</p>
  </div>
</template>
  
  <script>
import { getCSRFToken } from "../store/auth";
import axios from '../axios.js';

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      error: "",
      success: "",
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post(
          "/api/register",
          {
            username: this.username,
            email: this.email,
            password: this.password,
          },
          {
            headers: {
              "X-CSRFToken": getCSRFToken(), // Pass CSRF token here
            },
            withCredentials: true, // Include credentials if necessary
          }
        );

        console.log('successful')

        if (response.status === 201) {
          this.success = "Registration successful! Please log in.";
          setTimeout(() => {
            console.log('Redirecting to login...');
            this.$router.push("/login");
          }, 1000);
        }
      } catch (err) {
        this.error =
          "An error occurred during registration: " +
            err.response?.data?.error || err.message;
      }
    },
  },
};
</script>
  