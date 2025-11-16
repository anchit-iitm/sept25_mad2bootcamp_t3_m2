<template>
    <h1>Welcome to the Home View</h1>
    <div class="search-person"><input type="text" v-model="searchQuery" placeholder="find any person with name"></div>
    <table>
        <thead>
            <tr>
            <th>id</th>
            <th>Name</th>
            <th>Age</th>
            <th>actions</th>
            </tr>   
        </thead>
        <tbody>

          <tr v-for="person in filteredPersons" :key="person.id">
            <td>{{ person.id }}</td>
            <td>{{ person.name }}</td>
            <td>{{ person.age }}</td>
            <td><button type="button" @click="edit_person(person.id, person.name, person.age)">edit</button> | <button type="button" @click="delete_person(person.id)">delete</button></td>
          </tr>
        </tbody>
    </table>
</template>
<script>
import axios from 'axios';
export default {
  name: 'adminView',
  data() {
    return {
      persons: [],
      token: null,
      searchQuery: ''
    }
  },
  computed: {
    filteredPersons() {
      return this.persons.filter(person =>
        person.name.toLowerCase().includes(this.searchQuery.toLowerCase()),
        console.log(this.searchQuery)
      );
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
        .get("http://localhost:8080/api/user",
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
    },
    delete_person(id){
      if (!confirm("Are you sure you want to delete this person?")) {
        return;
      }
      if (!this.token) {
        this.$router.push({ name: "login" });
      }
      if (!id) {
        alert("Invalid person ID");
        return;
      }
      axios
        .delete(`http://localhost:8080/api/users`,
        {
          headers: {
            'Authorization': `${this.token}`,
            'id': `${id}`
          }
        },
        )
        .then(response => {
          this.fetch_all_person();
        })
        .catch(error => {
          console.error("There was an error deleting the person:", error);
        });
      },
      edit_person(id, name, age){
        name = prompt("name", name);
        age = prompt("age", age);
        axios
          .put(`http://localhost:8080/api/users`,
          {
            name: name,
            age: age,
            id: id
          },
          {
            headers: {
              'Authorization': `${this.token}`,
            }
          },
          )
          .then(response => {
            this.fetch_all_person();
          })
          .catch(error => {
            console.error("There was an error editing the person:", error);
          });

       

      }
  }
}
</script>

