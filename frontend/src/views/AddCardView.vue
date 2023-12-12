<template>
  <div class="about">
    <form @submit.prevent="addCard">
      <input v-model="front" type="text" placeholder="Front of card" />
      <input v-model="back" type="text" placeholder="Back of card" />
      <AppButton text="Add Card" @emit="addCard" />
    </form>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import { Options, Vue } from 'vue-class-component';
import AppButton from '@/components/AppButton.vue';

@Options({
  name: 'AddCardView',
  components: {
    AppButton,
  },
})
export default class AddCardView extends Vue {
  front = '';
  back = '';

  async addCard() {
    try {
      const response = await axios.post('http://localhost:5000/cards', {
        front: this.front,
        back: this.back,
        labels: [],
        username: 'test',
      });
      console.log(response.data);
    } catch (error) {
      console.log(error);
    }
  }
}
</script>
