<template>
    <div class="edit-person">
        <h1>Edit Person Component</h1>
        <div class="edit-person-form">
            <div class="form-group" id="person-name">
                <label for="name">Name: </label>
                <input type="text" id="name" v-model="this.name" required>
            </div>
            <div class="form-group" id="person-age">
                <label for="age">Age: </label>
                <input type="number" id="age" v-model="this.age" required>
            </div>
            <button id="edit-person-button" @click="editPerson">Edit Person</button>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    name: "edit-person",
    data() {
        return {
            token: null,
            name: "",
            age: ""
        }
    },
    created() {
        this.token = localStorage.getItem('authToken');
        if (this.token === null) {
            this.$router.push({ name: "login" });
        }
    },
    methods: {
        editPerson() {
            if (this.name === "" || this.age === "") {
                alert("Name and Age cannot be empty");
                return;
            }
            axios
            .put("http://localhost:8080/api/users", 
                {
                    name: this.name,
                    age: this.age
                },
                {
                    headers: {
                        'Authorization': `${this.token}`
                    }
                }
            )
            .then(response => {
                if (response.status === 201) {                alert("Person edited successfully!");
                this.name = "";
                this.age = "";
                this.$router.push({ name: "home" });}
            })
            .catch((error) => {
                alert("Error editing person, please try again.");
                console.error(error);
            });
        }
    },

}
</script>