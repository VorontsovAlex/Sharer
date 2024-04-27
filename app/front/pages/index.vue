<template>
    <div class="index">
        <Header />
        <h1>Press F</h1>
        <div class="index__item">
            <h2>Шаблон для формы регистрации</h2>
            <Form />
        </div>
        <div class="index__item">
            <h2>Шаблон для формы логина</h2>
            <Form isRegistered />
        </div>
        <div class="index__item">
            <h2>Шаблон для таблицы</h2>
            TODO
        </div>
        <div class="index__item">
            <h2>Шаблон для попапа</h2>
            TODO
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
  @import "./styles/index/index";
</style>
