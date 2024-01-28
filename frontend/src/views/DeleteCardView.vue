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
        <span class="delete-icon" @click="deleteCard(card.id)">❌</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import { Options, Vue } from 'vue-class-component';
import { useStore } from 'vuex';

@Options({
  name: 'DeleteCardView',
})
export default class DeleteCardView extends Vue {
  searchQuery = '';
  store = useStore();

  get filteredCards() {
    return this.store.state.cards.filter((card: { front: string }) =>
      card.front.toLowerCase().includes(this.searchQuery.toLowerCase())
    );
  }

  async deleteCard(cardId: any) {
    try {
      await axios.delete(`http://localhost:5000/cards/${cardId}`, {
        headers: {
          Authorization: `Bearer ${this.store.state.user.token}`,
        },
      });
      console.log(`Card with ID ${cardId} deleted successfully.`);
      // You may want to update your store to remove the deleted card from the state here
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
}

.card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 250px;
  margin-bottom: 10px;
  padding: 10px;
  border: 3px solid #000000;
  border-radius: 15px;
  font-size: 18px;
}

.delete-icon {
  cursor: pointer;
}

.no-cards-message {
  font-size: 18px;
  color: #8f8f8f;
}
</style>
