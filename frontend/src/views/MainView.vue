<template>
  <AppButton text="GO" width="50" height="50" />
  <ProgressBar :progress="progress" :studied="10" :to-review="40"></ProgressBar>
  <div class="buttons-container">
    <AppButton text="Add Card" link="add-card" />
    <AppButton text="Edit Card" link="edit-card" />
    <AppButton text="Settings" link="settings" />
  </div>
</template>

<script lang="ts" scoped>
import { Options, Vue } from 'vue-class-component';
import AppButton from '@/components/AppButton.vue';
import ProgressBar from '@/components/ProgressBar.vue';

@Options({
  name: 'MainView',
  components: {
    AppButton,
    ProgressBar,
  },
})
export default class MainView extends Vue {
  public progress = 20;
}
</script>

<style lang="scss">
.card-info {
  font-size: 16px;
  margin-top: 20px;
}

.buttons-container {
  display: flex;
  align-items: center;
  flex-direction: column;

  width: 200px;
}

.button:hover {
  background-color: #51ff4e;
}
</style>
