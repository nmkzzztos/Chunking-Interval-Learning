<template>
  <div v-if="cardsToReview.length === 0" class="no-cards">
    <AppButton text="GO" width="50" height="50" disabled="true" />
  </div>
  <div v-else>
    <AppButton text="GO" width="50" height="50" link="study" />
  </div>
  <ProgressBar
    :progress="progress"
    :studied="cards.cards.length - cardsToReview.length"
    :to-review="cardsToReview.length"
  ></ProgressBar>
  <div class="buttons-container">
    <AppButton text="Add Card" link="add-card" />
    <AppButton text="Delete Card" link="delete-card" />
    <AppButton text="Logout" @event="logout" />
  </div>
</template>

<script lang="ts" scoped>
import { Card } from '@/types/Card';
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

  // Calculate progress based on number of cards studied and total number of cards
  get progress() {
    return (
      ((this.cards.cards.length - this.cardsToReview.length) /
        this.cards.cards.length) *
      100
    );
  }

  get cards() {
    return this.store.state.cards;
  }

  get user() {
    return this.store.state.user;
  }

  // Get cards that need to be reviewed (next_review date is in the past)
  get cardsToReview() {
    return this.cards.cards.filter((card: Card) => {
      return new Date(card.next_review).getTime() < new Date().getTime();
    });
  }

  // Delete user from store and local storage and redirect to login page
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
