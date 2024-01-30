<template>
  <div class="about">
    <form @submit.prevent="addCard" class="form-add-card">
      <div class="section">
        <div class="inputs">
          <div class="input-container">
            <textarea v-model="front" type="text" id="front" placeholder="" />
            <label for="front">Front of card</label>
          </div>
          <div class="input-container">
            <textarea v-model="back" type="text" id="back" placeholder="" />
            <label for="back">Back of card</label>
          </div>
          <div class="input-container">
            <textarea v-model="labels" type="text" id="labels" placeholder="" />
            <label for="labels" class="last_label"
              >Labels (Lexica, Science ...)</label
            >
          </div>
        </div>
      </div>
      <AppButton text="Add Card" :disabled="!isFormValid" @emit="addCard" />
    </form>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import { Options, Vue } from 'vue-class-component';
import AppButton from '@/components/AppButton.vue';
import { useStore } from 'vuex';

@Options({
  name: 'AddCardView',
  components: {
    AppButton,
  },
})
export default class AddCardView extends Vue {
  front = '';
  back = '';
  labels = '';

  store = useStore();

  get isFormValid(): string {
    return this.front && this.back;
  }

  get cards() {
    return this.store.state.cards;
  }

  private convert_labels() {
    const reg_exp = /[\s,.]+/g;
    return this.labels.split(reg_exp).join(' ');
  }

  async addCard() {
    try {
      const front = this.front;
      const back = this.back;
      const labels = this.convert_labels();
      const username = this.store.state.user['user'];
      const next_review = new Date().toISOString();

      await axios.post('http://localhost:5000/cards', {
        front,
        back,
        labels,
        username,
        next_review,
      });
      this.store.commit('addCard', {
        front,
        back,
        labels,
        username,
        next_review,
        repeat_count: 0,
      });
    } catch (error) {
      console.log(error);
    }
  }
}
</script>

<style lang="scss" scoped>
.form-add-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}

.section {
  position: relative;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.inputs {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
}

textarea {
  width: 250px;
  height: 75px;
  padding: 10px;
  margin-top: 10px;

  border: 3px solid #000000;
  border-radius: 15px;
  outline: none;
  box-shadow: none;

  font-size: 20px;
  resize: none;
}

#labels {
  height: 25px;
}

.translate {
  position: relative;
  left: 10px;
}

label {
  position: absolute;
  bottom: 75px;
  left: 15px;
  pointer-events: none;
  color: #8f8f8f;
  font-size: 16px;
}

.last_label {
  bottom: 20px;
}

.input-container {
  position: relative;
}

textarea:focus + label,
textarea:not(:placeholder-shown) + label {
  visibility: hidden;
}
</style>
