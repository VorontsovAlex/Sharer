<template>
    <div class="navbar">
        <div
            v-for="item in navbarItems"
            :key="item.id"
            @click="router.push(item.to)"
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
    import router from "#app/plugins/router.js";

    export default {
      methods: {router},
        setup() {
          const router = useRouter()
            const navbarItems = [
                {
                    id: 0,
                    icon: 'search',
                    text: 'Поиск',
                    to: '/',
                },
                {
                    id: 1,
                    icon: 'heart',
                    text: ' Шеринг',
                    to: '/'
                },
                {
                    id: 2,
                    icon: 'account',
                    text: ' Профиль',
                    to: '/'
                },
            ];

            const selectItem = (id) => {
                console.log('selectItem: ', id);
            };

            return {
                navbarItems,
                selectItem,
                router,
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/navbar/navbar";
</style>
