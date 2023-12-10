<template>
  <div>
    <h1 class="title">Create Account</h1>
    <form @submit.prevent="register" class="form-register">
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
      <input
        v-model="confirmPassword"
        type="password"
        placeholder="Confirm password"
        required
        class="input"
        :class="{ 'input-error': !validatePassword }"
      />
      <AppButton type="submit" text="Sign up" @emit="register" />
      <p class="text-below">
        Already have an account?<router-link to="login" class="link"
          >Login</router-link
        >
      </p>
    </form>
  </div>
</template>

<script lang="ts" scoped>
import axios from 'axios';
import { Options, Vue } from 'vue-class-component';
import AppButton from '@/components/AppButton.vue';

@Options({
  name: 'LoginView',
  components: {
    AppButton,
  },
})
export default class LoginView extends Vue {
  username = '';
  password = '';
  confirmPassword = '';

  async register() {
    // TODO: implement login
  }

  get validatePassword() {
    return this.password === this.confirmPassword;
  }
}
</script>

<style lang="scss">
.title {
  margin-bottom: 10px;
  font-size: 24px;
  font-weight: bold;
}

.form-register {
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

.input-error {
  border: 2px solid #a50000;
}
</style>
