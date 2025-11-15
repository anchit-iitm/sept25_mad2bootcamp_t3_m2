<template>
    <div class="login-comp">
        <h1>login in to the app</h1>
        <div class="login-form">
            <div class="user-id">
                <label for="userid">User ID: </label>
                <input type="text" id="userid" v-model="this.userId" required>
            </div>
            <div class="password">
                <label for="password">Password: </label>
                <input type="password" id="password" v-model="this.password" required>
            </div>
            <button @click="this.login">Login</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: "login-comp",
    data() {
        return {
            userId: "",
            password: ""
        }
    },
    methods: {
        login() {
            if (this.userId === "" || this.password === "") {
                alert("User ID and Password cannot be empty");
                return;
            }
            if ( this.userId.includes("@")) {
                axios
                .post("http://localhost:8080/api/login", 
                    {
                        email: this.userId,
                        password: this.password
                    }
                )
                .then((response) => {
                    if (response.data.message === "Login successful.") {
                        localStorage.setItem('authToken', response.data.authToken);
                        if (localStorage.getItem('authToken') !== null) {
                            this.$router.push({ name: "home" });
                        }
                        this.$router.push({ name: "home" });
                    }
                })
                .catch((error) => {
                    alert("Invalid User ID or Password, please try again.");
                    console.error(error);
                });
            } else {
                alert("Invalid User ID or Password");
            }
        }
    }
}
</script>