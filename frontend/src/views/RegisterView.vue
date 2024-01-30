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
      <p v-if="userAlreadyExists" class="text-below error">
        User already exists. Please try again.
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
  userAlreadyExists = false;

  async register() {
    try {
      await axios.post('http://localhost:5000/register', {
        username: this.username,
        password: this.password,
      });
      this.$router.push('/login');
    } catch (error: any) {
      console.log(error);
      if (error.response.status === 409) {
        this.userAlreadyExists = true;
      }
    }
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

.error {
  color: #ff0000;
  position: absolute;
  top: 80%;
}
</style>
