import { User } from '@/types/User';

export interface UserState {
  user: User | null;
}

const state: UserState = {
  user: null,
};

const getters = {
  user: (state: UserState) => state.user,
  cards: (state: UserState) => state.user?.cards,
};

const mutations = {
  setUser: (state: UserState, user: User) => (state.user = user),
  setCards: (state: UserState, cards: User['cards']) => {
    console.log('setCards', cards);
    if (state.user) {
      console.log(state.user);
    }
  },
};

const actions = {
  setUser: ({ commit }: any, user: User) => commit('setUser', user),
};

export default {
  state,
  getters,
  mutations,
  actions,
};
