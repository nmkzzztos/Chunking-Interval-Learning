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
  },
  setCards: (
    state: CardsState,
    payload: { cards: Card[]; username: string }
  ) => {
    for (const value of Object.values(payload.cards)) {
      const card: Card = {
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
  deleteAllCards: (state: CardsState) => {
    state.cards = [];
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
