import { Card } from '@/types/Card';

export interface CardsState {
  cards: Card[];
}

const state: CardsState = {
  cards: [],
};

const getters = {
  cards: (state: CardsState) => state.cards,
};

const mutations = {
  addCard: (state: CardsState, card: Card) => {
    state.cards.push(card);
    localStorage.setItem('cards', JSON.stringify(state.cards));
  },
  setCards: (
    state: CardsState,
    payload: { cards: Card[]; username: string }
  ) => {
    for (const value of Object.values(payload.cards)) {
      const card: Card = {
        card_id: value.card_id,
        front: value.front,
        back: value.back,
        labels: value.labels,
        next_review: value.next_review,
        user_name: payload.username,
        repeat_count: value.repeat_count,
      };
      state.cards.push(card);
    }
  },
  deleteCard: (state: CardsState, card_id: number) => {
    state.cards = state.cards.filter((card) => card.card_id !== card_id);
    localStorage.setItem('cards', JSON.stringify(state.cards));
  },
  deleteAllCards: (state: CardsState) => {
    state.cards = [];
    localStorage.setItem('cards', JSON.stringify(state.cards));
  },
  updateCard: (
    state: CardsState,
    payload: { card_id: number; repeat_count: number; next_review: string }
  ) => {
    state.cards.forEach((card) => {
      if (card.card_id === payload.card_id) {
        card.repeat_count = payload.repeat_count;
        card.next_review = payload.next_review;
        return;
      }
    });
    localStorage.setItem('cards', JSON.stringify(state.cards));
  },
};

const actions = {
  setCards: ({ commit }: any, cards: Card[]) => commit('setCards', cards),
};

export default {
  state,
  getters,
  mutations,
  actions,
};
