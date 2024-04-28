<template>
  <div class="directions">
    <div class="directions__container">
        <div
            v-for="direction in directions"
            :key="direction.id"
            class="directions__item directions-item"
        >

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

<script lang="ts">
    import {useUserStore} from "~/store/user.js";

    export default {
        setup() {
          const {setSelectedGroup, selectedGroup} = useUserStore()
            const directions = [
                {
                    id: 0,
                    text: 'Кемпинг',
                    image: 'kamp',
                },
                {
                    id: 2,
                    text: 'Для дома',
                    image: 'tex',
                },
                {
                    id: 4,
                    text: 'Стройка',
                    image: 'tex2',
                },

            ];

            const selectDirection = (id) => {
              setSelectedGroup(id)
            };

            return {
                directions,
                selectDirection,
              selectedGroup
            };
        }
    }
</script>

<style lang="scss" scoped>
  @use "./styles/directions/directions";
</style>
