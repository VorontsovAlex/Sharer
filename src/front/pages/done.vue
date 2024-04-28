<template>
    <div class="done">
        <div class="done__container">
            <img
                src="~/assets/icons/alert.svg"
                alt="Внимание!"
                class="done__alert"
            >
            <p class="done__id">
                ID: {{ offer.id }}
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
                :src="`/_nuxt/assets/images/offers/${offer.image}.jpg`"
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

<script>
    export default {
        setup() {
            const offer = ref({
                id: '000000001',
                status: 'Подтверждено',
                info: [
                    {
                        key: 'Дата',
                        value: '1 - 3 мая',
                    },
                    {
                        key: 'Количество',
                        value: '1 шт.',
                    },
                    {
                        key: 'Стоимость',
                        value: '€36 / 3 дня',
                    },
                ],
                image: 'offer-0',
                title: 'Палатка на выходные Tramp Nishe 2',
                description: [
                    'Вместимость 3 человека',
                    'Двухслойная палатка',
                    'Вход внутренней палатки продублированы москитной сеткой',
                    'Вес: 3900гр',
                    'Внешний размер: 360x220x130см',
                ],
                socials: [
                    {
                        name: 'Reddy',
                        href: 'https://reddy.team',
                        image: 'rd',
                    },
                    {
                        name: 'Telegram',
                        href: 'https://web.telegram.org',
                        image: 'tg',
                    },
                    {
                        name: 'WhatsApp',
                        href: 'https://www.whatsapp.com',
                        image: 'wt',
                    },
                ]
            });

            return {
                offer,
            };
        }
    }
</script>

<style lang="scss" scoped>
  @import "./styles/done/done";
</style>
