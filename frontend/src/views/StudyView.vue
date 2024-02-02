<template>
  <div class="study-view">
    <div class="controls">
      <button @click="prevCard" :class="disabledPrevButton">Previous</button>
      <div v-if="!showBack" class="reveal" @click="revealBack">
        <button @click="revealBack">Reveal</button>
      </div>
      <div v-else class="reveal">
        <button @click="hideBack">Hide</button>
      </div>
      <button @click="nextCard" :class="disabledNextButton">Next</button>
    </div>
    <div v-if="currentCard" class="card">
      <div>{{ currentCard.front }}</div>
      <div v-if="showBack">{{ currentCard.back }}</div>
    </div>
    <div class="label">
      <div v-if="currentCard">{{ currentCard.labels }}</div>
    </div>
    <div class="actions">
      <button @click="markKnown(false)" class="unknown">Don't know</button>
      <button @click="markKnown(true)">Know</button>
    </div>
  </div>
</template>

<script lang="ts">
import { Card } from '@/types/Card';
import axios from 'axios';
import { Options, Vue } from 'vue-class-component';
import { useStore } from 'vuex';

@Options({
  name: 'StudyView',
})
export default class StudyView extends Vue {
  showBack = false;
  currentCardIndex = 0;
  store = useStore();

  get cards(): Card[] {
    return this.store.state.cards.cards;
  }

  get labels(): { [key: string]: number } {
    const labels: { [key: string]: number } = {};
    for (const card of this.cards) {
      if (labels[card.labels]) {
        labels[card.labels]++;
      } else {
        labels[card.labels] = 1;
      }
    }
    return labels;
  }

  get groupedCards(): Card[] {
    const groupedCards: [Card[]] = [[]];
    for (const label in this.labels) {
      const cards = this.cards.filter((card: Card) => {
        return card.labels === label;
      });
      groupedCards.push(cards);
    }
    return groupedCards.flat();
  }

  get currentCard() {
    return this.groupedCards[this.currentCardIndex];
  }

  get disabledPrevButton() {
    if (this.currentCardIndex === 0) {
      return 'disabled';
    }
    return '';
  }

  get disabledNextButton() {
    if (this.currentCardIndex === this.cards.length - 1) {
      return 'disabled';
    }
    return '';
  }

  revealBack() {
    this.showBack = true;
  }

  hideBack() {
    this.showBack = false;
  }

  prevCard() {
    this.showBack = false;
    if (this.currentCardIndex > 0) {
      this.currentCardIndex--;
    }
  }

  nextCard() {
    this.showBack = false;
    if (this.currentCardIndex < this.cards.length - 1) {
      this.currentCardIndex++;
    }
  }

  markKnown(known: boolean) {
    // Update the next review date based on the number of times the card has been repeated 1 = 1 hour, 2 = 8 hours, 3 = 24 hours, 4 = 3 days
    const updateBasedOnRepeat: { [key: number]: number } = {
      0: 1,
      1: 8,
      2: 24,
      3: 64,
      4: 192,
    };

    const next_review = new Date(
      new Date().getTime() +
        updateBasedOnRepeat[this.currentCard.repeat_count] * 60 * 60 * 1000
    );

    const repeat_count = this.currentCard.repeat_count + 1;

    if (known) {
      this.store.commit('updateCard', {
        card_id: this.currentCard.card_id,
        next_review,
        repeat_count,
      });

      axios.put('http://localhost:5000/cards', {
        card_id: this.currentCard.card_id,
        username: this.store.state.user['user'],
        next_review: next_review,
        repeat_count: repeat_count,
      });

      if (this.currentCardIndex == this.cards.length - 1) {
        this.$router.push('/');
      }
    }
    this.nextCard();
  }
}
</script>

<style lang="scss" scoped>
.study-view {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-weight: 600;
}

.controls,
.actions {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  width: 300px;
  min-height: 150px;
  padding: 20px;
  margin-bottom: 20px;
  border: 3px solid #000000;
  border-radius: 15px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-size: 18px;
  color: #000000;
  transition: background-color 0.3s ease;
}

.card:hover {
  background-color: #eef2f3;
}

.label {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 200px;
  height: 40px;
  margin-bottom: 20px;
  border: 3px solid #000000;
  border-radius: 15px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-size: 18px;
  color: #000000;
  transition: background-color 0.3s ease;
}

button {
  padding: 10px 15px;
  margin: 0 10px;
  min-width: 100px;
  border: 3px solid #000000;
  border-radius: 15px;
  background-color: #50bb4f;
  color: white;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  outline: none;
  transition: all 0.2s ease;
}

button:hover {
  background-color: #51ff4e;
  transform: translate(-8px, -8px);
  box-shadow: 8px 8px #000000;
}

.unknown {
  background-color: #a80303;
}

.unknown:hover {
  background-color: #ff0000;
}

.disabled {
  background-color: #8f8f8f;
  cursor: default;
  box-shadow: none;
}

.disabled:hover {
  background-color: #8f8f8f;
  transform: none;
  box-shadow: none;
}

.input-container {
  display: flex;
  flex-direction: column;
  position: relative;
  margin: 10px 0;
}

textarea,
input {
  width: 100%;
  padding: 10px;
  margin-top: 10px;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 16px;
}

label {
  position: absolute;
  left: 15px;
  top: -20px;
  background-color: #f5f5f5;
  padding: 0 5px;
  color: #8f8f8f;
  font-size: 14px;
  transition: all 0.2s ease;
}

textarea:focus,
input:focus {
  border-color: #42b983;
}

textarea:focus + label,
input:focus + label {
  color: #42b983;
}
</style>
