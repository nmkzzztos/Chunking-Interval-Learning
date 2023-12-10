<template>
  <div>
    <h1 class="title">Sign In</h1>
    <form @submit.prevent="login" class="form-login">
      <input
        v-model="username"
        type="text"
        placeholder="Username"
        class="input"
      />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        class="input"
      />
      <AppButton type="submit" text="Continue" @emit="login" />
      <p class="text-below">
        Don't have an account?<router-link to="register" class="link"
          >Sign up</router-link
        >
      </p>
    </form>
  </div>
</template>

<script lang="ts" scoped>
import axios from 'axios';
import { Options, Vue } from 'vue-class-component';
import AppButton from '@/components/AppButton.vue';
import { useStore } from 'vuex';

@Options({
  name: 'LoginView',
  components: {
    AppButton,
  },
})
export default class LoginView extends Vue {
  username = '';
  password = '';

  async login() {
    try {
      const response = await axios.post('http://localhost:5000/login', {
        username: this.username,
        password: this.password,
      });
      console.log(response.data);
      useStore().commit('setUser', response.data.user);
      this.$router.push('/');
    } catch (error) {
      console.log(error);
    }
  }
}
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 10px;
  font-size: 24px;
  font-weight: bold;
}
.form-login {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input {
  margin: 10px;
  padding: 10px;
  border-radius: 15px;
  border: 2px solid #000000;
  font-size: 16px;
  width: 200px;
}

.text-below {
  font-size: 12px;
  font-weight: bold;
}

.link {
  padding-left: 5px;
  color: #42b983;
  text-decoration: none;

  transition: all 0.1s ease-in-out;
}

.link:hover {
  color: #000000;
}
</style>
