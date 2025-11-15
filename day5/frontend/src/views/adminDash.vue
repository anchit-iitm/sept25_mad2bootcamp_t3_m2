<template>
    <h1>Welcome to the Home View</h1>
    <table>
        <thead>
            <tr>
            <th>id</th>
            <th>Name</th>
            <th>Age</th>
            </tr>   
        </thead>
        <tbody>

        </tbody>
    </table>
</template>
<script>
import axios from 'axios';
export default {
  name: 'HomeView',
  data() {
    return {
      persons: [],
      token: null
    }
  },
  created() {
    this.token = localStorage.getItem('authToken');
    if (!this.token) {
        this.$router.push({ name: "login" });
    }
    this.fetch_all_person();    
  },
  methods: {
    fetch_all_person(){
      axios
        .get("http://localhost:8080/api/users",
          {
            headers: {
              'Authorization': `${this.token}`
            }
          }
        )
        .then(response => {
          this.persons = response.data.data;
        })
        .catch(error => {
          console.error("There was an error fetching the persons:", error);
        });
    }
  }
}
</script>

