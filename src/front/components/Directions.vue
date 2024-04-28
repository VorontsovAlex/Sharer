<template>
  <div class="directions">
    <div class="directions__container">
        <div
            v-for="direction in directions"
            :key="direction.id"
            class="directions__item directions-item"
        >
            <!-- TODO @programm1st: @click & :src -->
            <button
                @click="selectDirection(direction.id)"
                type="button"
                class="directions-item__button"
            >
                <img
                    :src="`/_nuxt/assets/images/directions/${direction.image}.png`"
                    alt=""
                    class="directions-item__image"
                >
            </button>
            <span class="directions-item__text">
                {{ direction.text }}
            </span>
        </div>
    </div>
  </div>
</template>

<script>
    export default {
        setup() {
            // TODO @programm1st
            const directions = [
                {
                    id: 0,
                    text: 'Кемпинг',
                    image: 'kamp',
                },
                {
                    id: 1,
                    text: 'Хобби',
                    image: 'kamp',
                },
                {
                    id: 2,
                    text: 'Для дома',
                    image: 'kamp',
                },
                {
                    id: 3,
                    text: 'Электроника',
                    image: 'kamp',
                },
                {
                    id: 4,
                    text: 'Стройка',
                    image: 'kamp',
                },
                {
                    id: 5,
                    text: 'Кемпинг',
                    image: 'kamp',
                },
                {
                    id: 6,
                    text: 'Хобби',
                    image: 'kamp',
                },
                {
                    id: 7,
                    text: 'Для дома',
                    image: 'kamp',
                },
                {
                    id: 8,
                    text: 'Электроника',
                    image: 'kamp',
                },
                {
                    id: 9,
                    text: 'Стройка',
                    image: 'kamp',
                },
            ];

            const selectDirection = (id) => {
                console.log('selectDirection: ', id);
            };

            return {
                directions,
                selectDirection,
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/directions/directions";
</style>
