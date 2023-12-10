<template>
  <div class="app-container">
    <header>
      <!-- You can use svg or img tag for logo -->
      <img src="./assets/pink_logo.svg" alt="Logo" class="logo" />
    </header>
    <div class="content">
      <router-view />
    </div>
    <footer class="card-info">
      <AppButton
        v-show="showReturnButton"
        class="return-to-home-button"
        width="50"
        height="40"
        link="/"
        :returnBtn="true"
      ></AppButton>
      <div v-show="showCardInfo" class="card-info">
        <p>Added Cards: 78</p>
        <p>Learned Cards: 19</p>
      </div>
    </footer>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import AppButton from '@/components/AppButton.vue';

@Options({
  name: 'App',
  components: { AppButton },
})
export default class App extends Vue {
  get showReturnButton() {
    if (
      this.$route.path === '/' ||
      this.$route.path === '/login' ||
      this.$route.path === '/register'
    ) {
      return false;
    }
    return true;
  }

  get showCardInfo() {
    if (this.$route.path === '/login' || this.$route.path === '/register') {
      return false;
    }
    return true;
  }
}
</script>

<style lang="scss">
#app {
  height: 100vh;

  font-family: 'Inter', sans-serif;
  font-size: 24px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #02004f;
}

body {
  margin: 0;
  background-color: #338ef9;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.app-container {
  max-width: 450px;
  height: 600px;
  margin: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  top: 50%;
  transform: translateY(-50%);

  text-align: center;

  background-color: #0053b5;
  border-radius: 20px;
  color: white;
}

header {
  height: 10%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo {
  width: 62.5px;
}

.content {
  height: 80%;
  padding: 20px 0 20px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
}

.card-info {
  height: 10%;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.return-to-home-button {
  position: absolute;

  transform: translateY(-40px);
}

@media screen and (max-width: 450px) {
  .app-container {
    max-width: calc(100vw - 20px);
    width: 100%;
    height: 100%;
    border-radius: 0;
    padding: 0 10px 0 10px;
  }

  .content {
    padding: 100px 0 100px 0;
  }
}
</style>
