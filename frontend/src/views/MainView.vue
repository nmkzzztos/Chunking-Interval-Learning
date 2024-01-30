<template>
  <AppButton text="GO" width="50" height="50" />
  <ProgressBar :progress="progress" :studied="10" :to-review="40"></ProgressBar>
  <div class="buttons-container">
    <AppButton text="Add Card" link="add-card" />
    <AppButton text="Delete Card" link="delete-card" />
    <AppButton text="Logout" @event="logout" />
  </div>
</template>

<script lang="ts" scoped>
import { onBeforeMount } from 'vue';
import { Options, Vue } from 'vue-class-component';
import AppButton from '@/components/AppButton.vue';
import ProgressBar from '@/components/ProgressBar.vue';
import { useStore } from 'vuex';

@Options({
  name: 'MainView',
  components: {
    AppButton,
    ProgressBar,
  },
})
export default class MainView extends Vue {
  store = useStore();

  public progress = 20;

  learnedCards = 0;

  get cards() {
    return this.store.state.cards;
  }

  get user() {
    return this.store.state.user;
  }

  get cardsToReview() {
    return this.cards.cards.filter((card: any) => {
      console.log(new Date(card.next_review).getTime());
      return new Date(card.next_review).getTime() < new Date().getTime();
    });
  }

  beforeMount(): void {
    if (
      !this.store.getters.user &&
      localStorage.getItem('isLogged') === 'true'
    ) {
      this.store.commit('setUser', localStorage.getItem('user'));
      this.store.commit('setCards', {
        cards: JSON.parse(localStorage.getItem('cards') || ''),
        username: localStorage.getItem('user'),
      });
    }
  }

  logout() {
    this.store.commit('setUser', null);
    this.store.commit('deleteAllCards');
    this.$router.push('/login');
    localStorage.setItem('isLogged', 'false');
  }
}
</script>

<style lang="scss">
.card-info {
  font-size: 16px;
  margin-top: 20px;
}

.buttons-container {
  display: flex;
  align-items: center;
  flex-direction: column;

  width: 200px;
}

.button:hover {
  background-color: #51ff4e;
}
</style>
