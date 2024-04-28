<template>
    <div class="offer">
        <div class="offer__header">
            <button
                @click="goBack"
                type="button"
                class="offer-header-return"
            >
                <img
                    src="~/assets/icons/arrow-left.svg"
                    alt=""
                    class="offer-header-return__icon"
                >
                <span class="offer-header-return__text">Назад</span>
            </button>
            <button
                @click="likeOffer"
                type="button"
                class="offer-header-like"
                aria-label="Нравится"
                title="Нравится"
            >
                <img
                    src="~/assets/icons/heart.svg"
                    alt=""
                    class="offer-header-like__icon"
                >
            </button>
        </div>
        <Swiper
            :slides-per-view="1"
            :pagination="true"
            :modules="modules"
            class="offer__swiper"
        >
            <SwiperSlide
                v-for="image in offer.images"
                :key="image.id"
                class="offer__swipe"
            >
                <img
                    :src="`/_nuxt/assets/images/offers/${image.name}.jpg`"
                    :alt="offer.title"
                    class="offer__image"
                >
            </SwiperSlide>
        </Swiper>
        <div class="offer__info">
            <h2 class="offer__title">
                {{ offer.title }}
            </h2>
            <p class="offer__area">
                {{ offer.area }}
            </p>
            <p class="offer__price">
                {{ offer.price }}
            </p>
            <ul class="offer__tags offer-tags">
                <li
                    v-for="tag in offer.tags"
                    :key="tag.id"
                    class="offer-tags__item"
                    :class="{'offer-tags__item--is-accent': tag.isAccent}"
                >
                    <span class="offer-tags__text">
                        {{ tag.text }}
                    </span>
                </li>
            </ul>
        </div>

        <div class="offer__counts offer-counts">
            <div class="offer-counts__row">
                <span class="offer-counts__title">Количество</span>
                <span class="offer-counts__text">Доступно: <span class="offer-counts__count">{{ offer.availableCount }} шт.</span></span>
            </div>
            <div
                v-if="offer.availableCount > 1"
                class="offer-counts-settings"
            >
                <button
                    @click="offer.onMinusClick"
                    type="button"
                    aria-label="Убавить"
                    title="Убавить"
                    class="offer-counts-settings__button"
                >
                    <span class="offer-counts-settings__icon">-</span>
                </button>
                <p class="offer-counts-settings__value">
                    {{ offer.currentCount }}
                </p>
                <button
                    @click="offer.onPlusClick"
                    type="button"
                    aria-label="Прибавить"
                    title="Прибавить"
                    class="offer-counts-settings__button"
                >
                    <span class="offer-counts-settings__icon">+</span>
                </button>
            </div>
        </div>

        <div class="offer__dates offer-dates">
            <button
                @click="selectDate"
                type="button"
                class="offer-dates__select offer-dates-select"
            >
                <span class="offer-dates-select__text">
                    {{ offer.dates }}
                </span>
            </button>
            <button
                @click="reserveOffer"
                type="button"
                class="offer-dates__reserve offer-dates-reserve"
            >
                <span class="offer-dates-reserve__text">
                    Забронировать
                </span>
            </button>
        </div>

        <div class="offer__description offer-description">
            <h3 class="offer-description__title">
                Информация о вещи
            </h3>
            <ul class="offer-description__list">
                <li
                    v-for="el in offer.description"
                    :key="el"
                    class="offer-description__row"
                >
                    {{ el }}
                </li>
            </ul>
        </div>

        <ul class="offer__characteristics offer-characteristics">
            <li
                v-for="characteristic in offer.characteristics"
                :key="characteristic.key"
                class="offer-characteristics__item"
            >
                <span class="offer-characteristics__key">
                    {{ characteristic.key }}
                </span>
                <span class="offer-characteristics__value">
                    {{ characteristic.value }}
                </span>
            </li>
        </ul>

        <div class="offer__pricelist offer-pricelist">
            <h3 class="offer-pricelist__title">
                Стоимость аренды
            </h3>
            <ul class="offer-pricelist-list">
                <li
                    v-for="price in offer.pricelist"
                    :key="price.text"
                    class="offer-pricelist-list__item"
                >
                    <span class="offer-pricelist-list__key">
                        {{ price.key }}
                    </span>
                    <span class="offer-pricelist-list__value">
                        {{ price.value }}
                    </span>
                </li>
            </ul>
        </div>

        <div class="offer__addresses offer-addresses">
            <h3 class="offer-addresses__title">
                Адреса
            </h3>
            <ul class="offer-addresses-list">
                <li
                    v-for="address in offer.addresses"
                    :key="address.text"
                    class="offer-addresses-list__item"
                >
                    <span class="offer-addresses-list__key">
                        {{ address.key }}
                    </span>
                    <span class="offer-addresses-list__value">
                        {{ address.value }}
                    </span>
                </li>
            </ul>
        </div>

        <button
            @click="reserveOffer"
            type="button"
            class="offer__reserve offer-reserve"
        >
            <span class="offer-reserve__text">
                Забронировать
            </span>
        </button>
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
            const offer = {
                id: 0,
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
                title: 'Палатка на выходные Tramp Nishe 2',
                area: 'Mesa Geitonia (Лимасол)',
                dates: '4 - 31 Мая',
                price: '€14 / день',
                tags: [
                    {
                        id: 0,
                        text: 'Без залога',
                        isAccent: true,
                    },
                    {
                        id: 1,
                        text: 'Новая вещь',
                        isAccent: false,
                    },
                ],
                availableCount: 3,
                currentCount: 1,
                description: [
                    'Вместимость 3 человека',
                    'Двухслойная палатка',
                    'Вход внутренней палатки продублированы москитной сеткой',
                    'Вес: 3900гр',
                    'Внешний размер: 360x220x130см',
                ],
                characteristics: [
                    {
                        key: 'ID',
                        value: '14229482',
                    },
                    {
                        key: 'Количество мест',
                        value: '2',
                    },
                    {
                        key: 'Вес, кг.',
                        value: '1,8',
                    },
                    {
                        key: 'Тип',
                        value: 'Треккинг, Кемпинг',
                    },
                    {
                        key: 'Бренд',
                        value: 'Tramp',
                    },
                    {
                        key: 'Цвет',
                        value: 'Зеленый',
                    },
                    {
                        key: 'Пол',
                        value: 'Унисекс',
                    },
                    {
                        key: 'Количество входов',
                        value: '1',
                    },
                    {
                        key: 'Водостойкость дна, мм.',
                        value: '10000',
                    },
                    {
                        key: 'Водостойкость тента, мм.',
                        value: '6000',
                    },
                    {
                        key: 'Комплектация',
                        value: 'Чехол, тент, палатка, дуги 3 шт., колышки 14 шт.',
                    },
                ],
                pricelist: [
                    {
                        key: '3 дня',
                        value: '€36',
                    },
                    {
                        key: '1 неделя',
                        value: '€77',
                    },
                    {
                        key: '2 недели',
                        value: '€140',
                    },
                    {
                        key: '3 недели',
                        value: '€189',
                    },
                    {
                        key: '4 недели',
                        value: '€224',
                    },
                ],
                addresses: [
                    {
                        key: 'Меса Гитонья (Лимосол)',
                        value: '1400 м',
                    },
                    {
                        key: 'Айос Афанасиос (Лимасол)',
                        value: '2000 м',
                    },
                    {
                        key: 'Като Полемидия (Лимасол)',
                        value: '2750 м',
                    },
                ],
                onMinusClick: () => {
                },
                onPlusClick: () => {
                },
            };

            const goBack = () => {
                //
            };

            const likeOffer = () => {
                // 
            };

            const selectDate = () => {
                // 
            };

            const reserveOffer = () => {
                // 
            };

            return {
                offer,
                modules: [Pagination],
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/offer/offer";
</style>
