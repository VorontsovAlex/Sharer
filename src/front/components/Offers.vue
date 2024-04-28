<template>
    <div class="offers">
        <div
            v-for="offer in sortedOffers"
            :key="offer.id"
            class="offers__item"
        >
            <!-- TODO @programm1st: @click & :src -->
            <button
                @click="goToOffer(offer.id)"
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
                            :src="image.format ? `/_nuxt/assets/images/offers/${image.name}` : `/_nuxt/assets/images/offers/${image.name}.jpg`"
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

<script lang="ts">
    import { Swiper, SwiperSlide } from 'swiper/vue';
    import { Pagination } from 'swiper/modules';
    import 'swiper/css/bundle';
    import 'swiper/css/pagination';
    import {useProductsStore} from "~/store/products.js";
    import {offers} from '~/components/constants/offers'
    import {useUserStore} from "~/store/user";

    export default {
        components: {
            Swiper,
            SwiperSlide,
        },
        setup() {
          const router = useRouter()
          const {searchQuery} = useProductsStore()
          const {selectedGroup} = useUserStore()

            const sortedOffers = computed(() => {
              if (unref(searchQuery)) {
                return  unref(offers).filter((offer) => {
                  return offer.title?.toLowerCase().includes(unref(searchQuery)?.toLowerCase())
                })
              }

              return unref(offers)
            })
            const sortedOffersByAll = computed(() => {
              debugger
              if (unref(selectedGroup) === 0) {
                let asd = unref(offers)[0]
                debugger
                return
              }
            })
            const goToOffer = (id: number) => {
                router.push(`/offer/${id}`)
            }

            return {
                sortedOffersByAll,
                offers,
                sortedOffers,
                searchQuery,
                modules: [Pagination],
                goToOffer,
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/offers/offers";
</style>
