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
                :class="{'offer-header-like--liked': offer.liked}"
                aria-label="Нравится"
                title="Нравится"
            >
                <svg
                    width="800"
                    height="800"
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                    class="offer-header-like__icon"
                >
                    <path
                        clip-rule="evenodd"
                        d="M12 6c-1.8-2.1-4.8-2.7-7-.8a5.3 5.3 0 0 0-.9 7.4 83.6 83.6 0 0 0 8 7.4l.4-.3c1.4-1.3 5.9-5.2 7.3-7.1a5.3 5.3 0 0 0-.8-7.4c-2.2-2-5.2-1.3-7 .8Z" stroke="#000"
                        stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round"
                    />
                </svg>
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
                    :src="image.format ? `/_nuxt/assets/images/offers/${image.name}` : `/_nuxt/assets/images/offers/${image.name}.jpg`"
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
                    @click="minusItem"
                    type="button"
                    aria-label="Убавить"
                    title="Убавить"
                    class="offer-counts-settings__button"
                >
                    <span class="offer-counts-settings__icon">-</span>
                </button>
                <p class="offer-counts-settings__value">
                    {{ offerCountOrder }}
                </p>
                <button
                    @click="plusItem"
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

<script lang="ts">
    import { Swiper, SwiperSlide } from 'swiper/vue';
    import { Pagination } from 'swiper/modules';
    import 'swiper/css/bundle';
    import 'swiper/css/pagination';
    import {reserveProduct} from "~/api/product.js";
    import {number} from "vue-types";
    import {offers} from "~/components/constants/offers";

    export default {
        components: {
            Swiper,
            SwiperSlide,
        },
      props: {
        id: {
          type: number,
          required: true
        }
      },
        setup(props) {
            const router = useRouter()
            const route = useRoute()
            const productId = computed(() => route.params.id)

            const offer = unref(offers).find((itemOffer) => {
              return Number(itemOffer.id) === Number(unref(productId))
            })
            const goBack = () => {
              router.go(-1);
            };

            const likeOffer = () => {
                unref(offer).liked = !unref(offer).liked;
            };

            const selectDate = () => {
                //
            };

            const reserveOffer = () => {
                reserveProduct(props.id)
                router.push(`/done/${props.id}`)
            };
            const offerCountOrder = ref(1)
          const isMinusBtmDisabled = ref(false);
            const minusItem = () => {
              if (offerCountOrder.value > 0) {
                isMinusBtmDisabled.value = false;
                return --offerCountOrder.value;
              }
              isMinusBtmDisabled.value = true;
            }
            const plusItem = () => ++offerCountOrder.value;

            return {
                offer,
                modules: [Pagination],
                offerCountOrder,
                minusItem,
                plusItem,
                goBack,
                likeOffer,
                reserveOffer,
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/offer/offer";
</style>
