<template>
    <div class="registration">
        <img
            src="~/assets/icons/logo.svg"
            alt="SHARE logo"
            class="registration__logo"
        >
        <h2 class="registration__title">Регистрация</h2>
        <Form
            :is-registered="false"
            class="registration__form"
        />
    </div>
</template>

<script>
</script>

<style lang="scss" scoped>
  @use "./styles/registration/registration";
</style>
