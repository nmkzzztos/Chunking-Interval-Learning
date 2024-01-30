import { createStore } from 'vuex';
import user from './user';
import cards from './cards/cards';

export default createStore({
  modules: {
    user,
    cards,
  },
});
