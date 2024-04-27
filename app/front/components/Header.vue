<template>
  <div class="header">
    <div class="header__logo">logo</div>
    <div
        v-if="!isRegistered"
        class="header__nav"
    >
        <button
            @click="openLoginForm"
            type="button"
            class="header__button"
        >
            <span>Вход</span>
        </button>
        <button
            @click="openRegistrationForm"
            type="button"
            class="header__button"
        >
            <span>Регистрация</span>
        </button>
    </div>
    <div
        v-else
        class="header__profile"
    >
        <button
            @click="goToProfile"
            type="button"
            class="header__profile"
        >
            Иконка
        </button>
    </div>
  </div>
</template>

<script>
    export default {
        props: {
            isRegistered: {
                type: Boolean,
                default: false,
            },
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/header/header";
</style>
