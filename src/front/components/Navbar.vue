<template>
    <div class="navbar">
        <div
            v-for="item in navbarItems"
            :key="item.id"
            class="navbar__item navbar-item"
        >
            <button
                @click="selectItem(item.id)"
                type="button"
                class="navbar-item__button"
            >
                <img
                    :src="`/_nuxt/assets/icons/${item.icon}.svg`"
                    alt=""
                    class="navbar-item__icon"
                >
                <span class="navbar-item__text">
                    {{ item.text }}
                </span>
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        setup() {
            const navbarItems = [
                {
                    id: 0,
                    icon: 'search',
                    text: 'Поиск',
                },
                {
                    id: 1,
                    icon: 'heart',
                    text: ' Шеринг',
                },
                {
                    id: 2,
                    icon: 'account',
                    text: ' Профиль',
                },
            ];

            const selectItem = (id) => {
                console.log('selectItem: ', id);
            };

            return {
                navbarItems,
                selectItem,
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/navbar/navbar";
</style>
