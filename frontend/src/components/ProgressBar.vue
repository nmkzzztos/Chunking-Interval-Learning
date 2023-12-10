<template>
  <div class="progress-bar">
    <p class="studied">{{ studied }} studied</p>
    <div class="container">
      <div class="progress" :style="progressStyle"></div>
    </div>
    <p class="to-review">{{ toReview }} to review</p>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

@Options({
  name: 'ProgressBar',
  props: {
    progress: {
      type: Number,
      required: true,
    },
    studied: {
      type: Number,
      required: true,
    },
    toReview: {
      type: Number,
      required: true,
    },
  },
})
export default class ProgressCircle extends Vue {
  public progress!: number;
  public studied!: number;
  public toReview!: number;

  get progressStyle() {
    return {
      width: `${this.progress}%`,
    };
  }

  get text() {
    return `${this.progress}%`;
  }
}
</script>

<style lang="scss">
.progress-bar {
  width: 90%;
}
.container {
  background-color: #d9d9d9;
  height: 15px;
  border: 2px solid #000000;
  border-radius: 10px;
  display: flex;
  align-items: center;
  padding: 2px;

  animation: pulsate 2s infinite;
}

@keyframes pulsate {
  0% {
    box-shadow: 0 0 30px #60e25d;
  }
  50% {
    box-shadow: none;
  }
  100% {
    box-shadow: 0 0 30px #60e25d;
  }
}

.studied,
.to-review {
  position: relative;
  margin: 5px;

  font-size: 16px;
  color: white;
}

.studied {
  left: -40px;

  color: #60e25d;
}

.to-review {
  right: -40px;
  margin-bottom: 20px;

  color: #d9d9d9;
}

.progress {
  height: 80%;
  width: 0%;
  background-color: #60e25d;
  border-radius: 10px;
}
</style>
