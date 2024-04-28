<template>
  <div class="header">
    <div class="header__input header-input">
        <input
            @click="openSeachPopup"
            v-model="searchValue"
            type="text"
            class="header-input__input"
        >
        <div class="header-input__container">
            <img
                src="~/assets/icons/search.svg"
                class="header-input__icon"
            >
            <div v-if="!searchValue" class="header-input-deco">
                <span class="header-input-deco__text header-input-deco__text--top">Что?</span>
                <span class="header-input-deco__text header-input-deco__text--bottom">Искать везде, неделя, рядом</span>
            </div>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
    import {useProductsStore} from "~/store/products.js";

    export default {
        setup() {
          const  {setSearchQuery} = useProductsStore();
          const searchValue = ref('')
            const openSeachPopup = () => {
                console.log('openSeachPopup');
            }

            watch(searchValue, (newValue) => {
              if (newValue.length > 3) {
                setSearchQuery(newValue);
              } else {
                setSearchQuery('');
              }
            })
            return {
                openSeachPopup,
                searchValue,
            };
        },
    }
</script>

<style lang="scss" scoped>
  @use "./styles/header/header";
</style>
