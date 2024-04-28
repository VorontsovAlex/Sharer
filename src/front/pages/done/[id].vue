<template>
  <div class="done">
    <div class="done__container">
      <img
          src="~/assets/icons/alert.svg"
          alt="Внимание!"
          class="done__alert"
      >
      <p class="done__id">
        ID: {{ randomOrder }}
      </p>
      <p class="done__status">
        {{ offer.status }}
      </p>
      <ul class="done__info done-info">
        <li
            v-for="item in offer.info"
            :key="item.key"
            class="done-info__item"
        >
                    <span class="done-info__key">
                        {{ item.key }}
                    </span>
          <span class="done-info__value">
                        {{ item.value }}
                    </span>
        </li>
      </ul>

      <img
          :src="offer.format ? `/_nuxt/assets/images/offers/${offer.image}` : `/_nuxt/assets/images/offers/${offer.image}.jpg`"
          alt="Изображение товара"
          class="done__image"
      >
      <h3 class="done__title">
        {{ offer.title }}
      </h3>
      <ul class="done__description done-description">
        <li
            v-for="item in offer.description"
            :key="item"
            class="done-description__item"
        >
          {{ item }}
        </li>
      </ul>
      <div class="done__chat done-chat">
        <img
            src="~/assets/icons/smile.svg"
            alt=""
            class="done-chat__image"
        >
        <p class="done-chat__text">
          Перейдите в чат
        </p>
        <div class="done-chat-socials">
          <a
              v-for="item in offer.socials"
              :key="item.name"
              :href="item.href"
              class="done-chat-socials__link"
              target="_blank"
          >
            <img
                :src="`/_nuxt/assets/images/socials/${item.image}.png`"
                :alt="item.name"
            >
          </a>
        </div>
      </div>
    </div>
    <Navbar />
  </div>
</template>

<script lang="ts">
import {offers} from '~/components/constants/offers'
export default {
  setup() {

    const route = useRoute();
    const productId = computed(() => route.params.id)

    const offer = unref(offers).find((itemOffer) => {
      return Number(itemOffer.id) === Number(unref(productId))
    })

    const randomOrder = computed(() => {
      return  Math.floor(Math.random() * 100)+10;
    })
    return {
      offer,
      randomOrder,
    };
  }
}
</script>

<style lang="scss" scoped>
@import "../styles/done/done";
</style>
