import { User } from '@/types/User';

export interface UserState {
  user: User | null;
}

const state: UserState = {
  user: null,
};

const getters = {
  user: (state: UserState) => state.user,
};

const mutations = {
  setUser: (state: UserState, user: User) => (state.user = user),
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
