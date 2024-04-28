export const offers = ref([
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
        title: 'Палатка на выходные в оченнь хороший прекрасный теплый день',
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
export const offer = ref({
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
    liked: false,
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
});
