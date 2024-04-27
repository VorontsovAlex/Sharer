<template>
    <div class="offers">
        <div
            v-for="offer in offers"
            :key="offer.id"
            class="offers__item"
        >
            <!-- TODO @programm1st: @click & :src -->
            <button
                @click="goToOffer(offer)"
                type="button"
                class="offers-item-element"
            >
                <Swiper
                    :slides-per-view="1"
                    :pagination="true"
                    :modules="modules"
                    class="offers-item-element__swiper"
                >
                    <SwiperSlide
                        v-for="image in offer.images"
                        :key="image.id"
                        class="offers-item-element__swipe"
                    >
                        <img
                            :src="`/_nuxt/assets/images/offers/${image.name}.jpg`"
                            :alt="offer.title"
                            class="offers-item-element__image"
                        >
                    </SwiperSlide>
                </Swiper>
                <div class="offers-item-element__description">
                    <p class="offers-item-element__title">
                        {{ offer.title }}
                    </p>
                    <p class="offers-item-element__area">
                        {{ offer.area }}
                    </p>
                    <p class="offers-item-element__dates">
                        {{ offer.dates }}
                    </p>
                    <p class="offers-item-element__price">
                        {{ offer.price }}
                    </p>
                </div>
            </button>
        </div>
    </div>
</template>

<script>
    import { Swiper, SwiperSlide } from 'swiper/vue';
    import { Pagination } from 'swiper/modules';
    import 'swiper/css/bundle';
    import 'swiper/css/pagination';

    export default {
        components: {
            Swiper,
            SwiperSlide,
        },
        setup() {
            // TODO @programm1st
            const offers = ref([
                {
                    id: 0,
                    image: 'offer-0',
                    images: [
                        {
                            id: 0,
                            name: 'offer-0',
                        },
                        {
                            id: 1,
                            name: 'offer-0',
                        },
                    ],
                    title: 'Палатка на выходные',
                    area: 'Mesa Geitonia (Лимасол)',
                    dates: '1 - 4 Мая',
                    price: '€12 / день',
                },
                {
                    id: 1,
                    image: 'offer-0',
                    images: [
                        {
                            id: 0,
                            name: 'offer-0',
                        },
                    ],
                    title: 'Палатка на выходные',
                    area: 'Mesa Geitonia (Лимасол)',
                    dates: '4 - 31 Мая',
                    price: '€14 / день',
                },
                {
                    id: 2,
                    image: 'offer-0',
                    images: [
                        {
                            id: 0,
                            name: 'offer-0',
                        },
                        {
                            id: 1,
                            name: 'offer-0',
                        },
                        {
                            id: 2,
                            name: 'offer-0',
                        },
                    ],
                    title: 'Палатка на выходные',
                    area: 'Mesa Geitonia (Лимасол)',
                    dates: '4 - 31 Мая',
                    price: '€15 / день',
                },
            ]);

            return {
                offers,
                modules: [Pagination],
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/offers/offers";
</style>
