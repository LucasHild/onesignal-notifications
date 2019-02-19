module.exports = {
    title: 'OneSignal-Notifications',
    description: 'OneSignal SDK for Python',
    head: [['link', { rel: 'icon', href: '/logo.png' }]],
    base: '/onesignal-notifications/',
    dest: './../docs',

    themeConfig: {
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Guide', link: '/guide/' },
            { text: 'GitHub', link: 'https://github.com/Lanseuo/onesignal-notifications' },
            { text: 'PyPi', link: 'https://pypi.org/project/onesignal-notifications/' }
        ],
        sidebar: {
            '/guide/': genSidebarConfig('Guide')
        }
    }
};

function genSidebarConfig(title) {
    return [
        {
            title,
            collapsable: false,
            children: [
                '',
                'send-notification',
                'cancel-notifications',
                'details-notification',
                'segment-notification',
                'filter-notification',
                'device-notification',
            ]
        }
    ]
}

