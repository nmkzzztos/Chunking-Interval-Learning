<template>
  <div class="delete-card">
    <div class="search-bar">
      <input
        v-model="searchQuery"
        type="text"
        id="search"
        placeholder="Search Cards"
      />
    </div>
    <div class="cards-list">
      <div v-if="filteredCards.length === 0" class="no-cards-message">
        You have no cards.
      </div>
      <div v-else v-for="card in filteredCards" :key="card.id" class="card">
        {{ card.front }}
        <span
          class="delete-icon"
          @click="deleteCard(card.card_id, user['user'])"
          >❌</span
        >
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import { Options, Vue } from 'vue-class-component';
import { useStore } from 'vuex';
import { Card } from '@/types/Card';

@Options({
  name: 'DeleteCardView',
})
export default class DeleteCardView extends Vue {
  searchQuery = '';
  store = useStore();

  get user() {
    return this.store.state.user;
  }

  get cards() {
    return this.store.state.cards;
  }

  // Filter cards by search query (front of card)
  get filteredCards() {
    return this.cards.cards.filter((card: Card) => {
      return card.front.toLowerCase().includes(this.searchQuery.toLowerCase());
    });
  }

  // Delete card from database and store
  async deleteCard(cardId: number, username: string) {
    try {
      console.log(`Deleting card with id ${cardId} for user ${username}`);
      await axios.delete('http://localhost:5000/cards', {
        data: {
          card_id: cardId,
          username: username,
        },
      });
      this.store.commit('deleteCard', cardId);
    } catch (error) {
      console.log(error);
    }
  }
}
</script>

<style lang="scss" scoped>
.delete-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 450px;
  max-height: 450px;
}

.search-bar {
  margin-bottom: 20px;
}

input[type='text'] {
  width: 250px;
  padding: 10px;
  border: 3px solid #000000;
  border-radius: 15px;
  font-size: 18px;
  outline: none;
}

.cards-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-height: 400px;
  overflow-y: auto;

  &::-webkit-scrollbar {
    display: none;
  }

  scrollbar-width: none;
}

.card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 250px;
  margin-bottom: 10px;
  padding: 10px;
  background-color: #50bb4f;
  border: 3px solid #000000;
  border-radius: 15px;
  font-size: 18px;

  transition: all 0.1s ease-in-out;
}

.card:hover {
  background-color: #51ff4e;
}

.delete-icon {
  cursor: pointer;
}

.no-cards-message {
  font-size: 18px;
  color: #8f8f8f;
}
</style>
