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
                <span class="header-input-deco__placeholder">
                    Что ищем сегодня?
                </span>
            </div>
            <button
                @click="openFindPopup"
                type="button"
                class="header-input__find header-input-find"
            >
                <img
                    src="~/assets/icons/find.svg"
                    alt=""
                    class="header-input-find__icon"
                >
            </button>
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

            const openFindPopup = () => {
                console.log('openFindPopup');
            };

            watch(searchValue, (newValue) => {
              if (newValue.length > 3) {
                setSearchQuery(newValue);
              } else {
                setSearchQuery('');
              }
            })
            return {
                openSeachPopup,
                openFindPopup,
                searchValue,
            };
        },
    }
</script>

<style lang="scss" scoped>
  @use "./styles/header/header";
</style>
