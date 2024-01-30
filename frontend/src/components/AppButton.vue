<template>
  <div v-if="link">
    <router-link :to="link" class="link">
      <button
        :class="btn_class"
        :style="style"
        :disabled="disabled"
        @click="$emit('event')"
      >
        <img v-if="returnBtn" src="../assets/return.svg" alt="" class="image" />
        <div v-if="text" class="text">{{ text }}</div>
      </button>
    </router-link>
  </div>
  <div v-else>
    <button
      :class="btn_class"
      :style="style"
      :disabled="disabled"
      @click="$emit('event')"
    >
      <img v-if="imagePath" :src="imagePath" alt="" />
      <div v-if="text" class="text">{{ text }}</div>
    </button>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  props: {
    text: {
      type: String,
      required: false,
    },
    width: {
      type: String,
      default: '150',
    },
    height: {
      type: String,
      default: '50',
    },
    backgroundColor: {
      type: String,
      default: '#60e25d',
    },
    link: {
      type: String,
      required: false,
    },
    returnBtn: {
      type: Boolean,
      default: false,
      required: false,
    },
    disabled: {
      type: Boolean,
      default: false,
      required: false,
    },
  },
  emits: ['event'],
})
export default class AppButton extends Vue {
  public text!: string;
  public width!: string;
  public height!: string;
  public backgroundColor!: string;
  public link!: string;
  public returnBtn!: boolean;
  public disabled!: boolean;

  get style() {
    return {
      width: `${this.width}px`,
      height: `${this.height}px`,
    };
  }

  get btn_class() {
    if (this.disabled) {
      return 'btn-disabled';
    }
    return 'btn';
  }

  public imagePath() {
    if (this.returnBtn) {
      return '../assets/return.svg';
    }
    return '';
  }
}
</script>

<style lang="scss" scoped>
.link {
  text-decoration: none;
}

.btn {
  padding: 10px 20px;
  margin: 10px 0;
  display: flex;
  align-items: center;
  justify-content: center;

  text-decoration: none;

  background-color: #60e25d;
  border: 3px solid #000000;
  border-radius: 30px;
  color: #000000;
  cursor: pointer;

  transition: all 0.3s ease;
}

.btn:hover {
  background-color: #51ff4e;

  transform: translate(-8px, -8px);
  box-shadow: 8px 8px #000000;
}

.btn-disabled {
  padding: 10px 20px;
  margin: 10px 0;
  display: flex;
  align-items: center;
  justify-content: center;

  text-decoration: none;

  background-color: #c7c7c7;
  border: 3px solid #000000;
  border-radius: 30px;
  color: #000000;
  cursor: not-allowed;

  transition: all 0.3s ease;
}

.image {
  position: relative;
}

.text {
  display: flex;
  align-items: center;
  justify-content: center;

  font-size: 16px;
  font-weight: 600;
}
</style>
