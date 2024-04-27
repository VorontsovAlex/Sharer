<template>
  <div class="header">
    <div class="header__input header-input">
        <input
            @click="openSeachPopup"
            type="text"
            class="header-input__input"
        >
        <div class="header-input__container">
            <img
                src="~/assets/icons/search.svg"
                class="header-input__icon"
            >
            <div class="header-input-deco">
                <span class="header-input-deco__text header-input-deco__text--top">Что?</span>
                <span class="header-input-deco__text header-input-deco__text--bottom">Искать везде, неделя, рядом</span>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
    export default {
        setup() {
            const openSeachPopup = () => {
                console.log('openSeachPopup');
            }

            return {
                openSeachPopup,
            };
        },
    }
</script>

<style lang="scss" scoped>
  @use "./styles/header/header";
</style>
